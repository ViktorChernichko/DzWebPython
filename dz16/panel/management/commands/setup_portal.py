from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.db.models import Q

from accounts.utils import ADMIN_GROUP_NAME
from news.models import Article, SiteSettings

User = get_user_model()

ADMIN_USERNAMES = ["admin1", "admin2", "admin3"]
ADMIN_PASSWORD = "AdminPass123!"
READER_USERNAME = "reader"
READER_PASSWORD = "ReaderPass123!"

SAMPLE_ARTICLES = [
    (
        "City council approves new park project",
        "The city council has approved the construction of a new central park.\n\nThe project includes walking paths, a playground and a small lake. Construction is expected to start in spring.",
    ),
    (
        "Public transport schedule changes next month",
        "Starting next month, several bus routes will run more frequently during rush hours.\n\nThe city transport department says the change should reduce waiting times by almost a third.",
    ),
    (
        "Local library opens a digital reading room",
        "The main city library has opened a digital reading room with free access to e-books and online courses.\n\nResidents can register at the front desk using any ID document.",
    ),
    (
        "Weekend farmers market returns to the main square",
        "Local farmers and craftsmen will gather at the main square every Saturday.\n\nOrganizers expect more than fifty stalls with fresh produce, honey and handmade goods.",
    ),
]


class Command(BaseCommand):
    help = "Creates the administrators group, demo users and sample articles."

    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name=ADMIN_GROUP_NAME)
        permissions = Permission.objects.filter(
            Q(content_type__app_label="news")
            | Q(
                content_type__app_label="auth",
                content_type__model="user",
                codename__in=["add_user", "delete_user", "view_user"],
            )
        )
        group.permissions.set(permissions)

        for username in ADMIN_USERNAMES:
            user, created = User.objects.get_or_create(
                username=username, defaults={"email": f"{username}@example.com"}
            )
            if created:
                user.set_password(ADMIN_PASSWORD)
                user.save()
            user.groups.add(group)

        reader, created = User.objects.get_or_create(
            username=READER_USERNAME, defaults={"email": "reader@example.com"}
        )
        if created:
            reader.set_password(READER_PASSWORD)
            reader.save()

        if not Article.objects.exists():
            author = User.objects.get(username=ADMIN_USERNAMES[0])
            for title, content in SAMPLE_ARTICLES:
                Article.objects.create(title=title, content=content, author=author)

        SiteSettings.load()

        self.stdout.write(self.style.SUCCESS("Portal is ready."))
        self.stdout.write(f"Administrators: {', '.join(ADMIN_USERNAMES)} / {ADMIN_PASSWORD}")
        self.stdout.write(f"Regular user: {READER_USERNAME} / {READER_PASSWORD}")
