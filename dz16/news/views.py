from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.utils import is_portal_admin

from .forms import CommentForm
from .models import Article, SavedArticle
from .utils import paginate, redirect_back


def article_list(request):
    articles = (
        Article.objects.filter(is_published=True)
        .select_related("author")
        .annotate(comment_count=Count("comments", distinct=True))
        .order_by("-created_at")
    )
    page_obj = paginate(request, articles, 6)
    return render(request, "news/article_list.html", {"page_obj": page_obj})


def article_detail(request, pk):
    article = get_object_or_404(Article.objects.select_related("author"), pk=pk)
    if not article.is_published and not is_portal_admin(request.user):
        raise Http404

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f"/accounts/login/?next={request.path}")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return redirect("news:article_detail", pk=article.pk)
    else:
        form = CommentForm()
        viewed = request.session.get("viewed_articles", [])
        if article.pk not in viewed:
            Article.objects.filter(pk=article.pk).update(views=F("views") + 1)
            viewed.append(article.pk)
            request.session["viewed_articles"] = viewed
            article.refresh_from_db()

    is_saved = (
        request.user.is_authenticated
        and SavedArticle.objects.filter(user=request.user, article=article).exists()
    )
    comments = article.comments.select_related("author")
    return render(
        request,
        "news/article_detail.html",
        {
            "article": article,
            "comments": comments,
            "form": form,
            "is_saved": is_saved,
        },
    )


@login_required
@require_POST
def toggle_save(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    deleted, _ = SavedArticle.objects.filter(user=request.user, article=article).delete()
    if deleted:
        messages.success(request, "Article removed from your saved list.")
    else:
        SavedArticle.objects.create(user=request.user, article=article)
        messages.success(request, "Article saved for later reading.")
    return redirect_back(request, "news:article_detail", article.pk)


@login_required
def saved_list(request):
    saved = SavedArticle.objects.filter(user=request.user).select_related("article")
    return render(request, "news/saved_list.html", {"saved": saved})
