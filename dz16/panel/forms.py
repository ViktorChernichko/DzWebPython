from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from accounts.utils import ADMIN_GROUP_NAME
from news.models import Article, SiteSettings

User = get_user_model()


class ColorInput(forms.TextInput):
    input_type = "color"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "is_published"]
        widgets = {"content": forms.Textarea(attrs={"rows": 12})}
        labels = {"is_published": "Published"}


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=False)
    is_admin = forms.BooleanField(required=False, label="Portal administrator")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit and self.cleaned_data.get("is_admin"):
            group, _ = Group.objects.get_or_create(name=ADMIN_GROUP_NAME)
            user.groups.add(group)
        return user


class BanForm(forms.Form):
    DURATION_CHOICES = [
        ("day", "One day"),
        ("week", "One week"),
        ("month", "One month"),
        ("forever", "Permanently"),
    ]

    duration = forms.ChoiceField(choices=DURATION_CHOICES)
    reason = forms.CharField(max_length=255, required=False)


class AppearanceForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ["background_color", "font_color", "font_size"]
        widgets = {
            "background_color": ColorInput(),
            "font_color": ColorInput(),
            "font_size": forms.NumberInput(attrs={"min": 12, "max": 28}),
        }
        labels = {
            "background_color": "Background color",
            "font_color": "Font color",
            "font_size": "Font size (px, 12-28)",
        }
