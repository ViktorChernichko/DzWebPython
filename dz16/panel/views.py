from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from accounts.decorators import portal_admin_required
from accounts.models import Ban
from accounts.utils import BAN_DURATIONS, active_bans, get_active_ban, is_portal_admin
from news.models import Article, Comment, SiteSettings
from news.utils import paginate, redirect_back

from .forms import AppearanceForm, ArticleForm, BanForm, UserCreateForm

User = get_user_model()


@portal_admin_required
def dashboard(request):
    context = {
        "article_total": Article.objects.count(),
        "published_total": Article.objects.filter(is_published=True).count(),
        "user_total": User.objects.count(),
        "comment_total": Comment.objects.count(),
        "ban_total": active_bans().count(),
    }
    return render(request, "panel/dashboard.html", context)


@portal_admin_required
def article_list(request):
    articles = Article.objects.select_related("author")
    return render(
        request, "panel/article_list.html", {"page_obj": paginate(request, articles, 20)}
    )


@portal_admin_required
def article_create(request):
    form = ArticleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Article has been created.")
        return redirect("panel:article_list")
    return render(
        request, "panel/article_form.html", {"form": form, "title": "New article"}
    )


@portal_admin_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Article has been updated.")
        return redirect("panel:article_list")
    return render(
        request, "panel/article_form.html", {"form": form, "title": "Edit article"}
    )


@portal_admin_required
@require_POST
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    messages.success(request, "Article has been deleted.")
    return redirect("panel:article_list")


@portal_admin_required
def user_list(request):
    page_obj = paginate(request, User.objects.order_by("username"), 20)
    for user in page_obj:
        user.is_admin = is_portal_admin(user)
        user.active_ban = get_active_ban(user)
        user.can_delete = user != request.user and not user.is_superuser
        user.can_ban = user.can_delete and not user.is_admin
    return render(request, "panel/user_list.html", {"page_obj": page_obj})


@portal_admin_required
def user_create(request):
    form = UserCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "User has been created.")
        return redirect("panel:user_list")
    return render(request, "panel/user_form.html", {"form": form})


@portal_admin_required
@require_POST
def user_delete(request, pk):
    target = get_object_or_404(User, pk=pk)
    if target == request.user or target.is_superuser:
        messages.error(request, "This user cannot be deleted.")
    else:
        target.delete()
        messages.success(request, "User has been deleted.")
    return redirect("panel:user_list")


@portal_admin_required
def user_ban(request, pk):
    target = get_object_or_404(User, pk=pk)
    if target == request.user or is_portal_admin(target):
        messages.error(request, "Administrators cannot be banned.")
        return redirect("panel:user_list")
    form = BanForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        duration = BAN_DURATIONS[form.cleaned_data["duration"]]
        expires_at = timezone.now() + duration if duration else None
        target.bans.filter(lifted=False).update(lifted=True)
        Ban.objects.create(
            user=target, reason=form.cleaned_data["reason"], expires_at=expires_at
        )
        messages.success(request, f"User {target.username} has been banned.")
        return redirect("panel:user_list")
    return render(request, "panel/user_ban.html", {"form": form, "target": target})


@portal_admin_required
@require_POST
def user_unban(request, pk):
    target = get_object_or_404(User, pk=pk)
    target.bans.filter(lifted=False).update(lifted=True)
    messages.success(request, f"User {target.username} has been unbanned.")
    return redirect("panel:user_list")


@portal_admin_required
def comment_list(request):
    comments = Comment.objects.select_related("author", "article").order_by("-created_at")
    return render(
        request, "panel/comment_list.html", {"page_obj": paginate(request, comments, 20)}
    )


@portal_admin_required
@require_POST
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    messages.success(request, "Comment has been deleted.")
    return redirect_back(request, "panel:comment_list")


@portal_admin_required
def appearance(request):
    form = AppearanceForm(request.POST or None, instance=SiteSettings.load())
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Appearance settings have been saved.")
        return redirect("panel:appearance")
    return render(request, "panel/appearance.html", {"form": form})


@portal_admin_required
def statistics(request):
    context = {
        "by_views": Article.objects.order_by("-views", "-created_at")[:10],
        "by_comments": Article.objects.annotate(total=Count("comments", distinct=True))
        .order_by("-total", "-created_at")[:10],
        "by_saves": Article.objects.annotate(total=Count("saved_by", distinct=True))
        .order_by("-total", "-created_at")[:10],
    }
    return render(request, "panel/statistics.html", context)
