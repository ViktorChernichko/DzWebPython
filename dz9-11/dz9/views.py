from django.http import HttpResponse


def build_page(title, content):
    nav = """
    <nav>
        <a href="/">Home</a> |
        <a href="/news/">News</a> |
        <a href="/management/">Management</a> |
        <a href="/facts/">Facts</a> |
        <a href="/contacts/">Contacts</a> |
        <a href="/history/">History</a>
    </nav>
    <hr>
    """
    return f"<h1>{title}</h1>{nav}{content}"


def home(request):
    content = "<p>Welcome to the official website of our city.</p>"
    return HttpResponse(build_page("Home", content))


def news(request, extra=None):
    content = "<p>Latest news about the city.</p>"
    return HttpResponse(build_page("City News", content))


def management(request, extra=None):
    content = "<p>Information about the city leadership.</p>"
    return HttpResponse(build_page("City Management", content))


def facts(request, extra=None):
    content = "<p>Interesting facts about the city.</p>"
    return HttpResponse(build_page("City Facts", content))


def contacts(request, extra=None):
    content = "<p>Phone numbers of the city services.</p>"
    return HttpResponse(build_page("Contact Phones", content))


def history(request, extra=None):
    content = """
    <p>General history of the city.</p>
    <p>
        <a href="/history/people/">Famous people</a> |
        <a href="/history/photos/">Historical photos</a>
    </p>
    """
    return HttpResponse(build_page("City History", content))


def history_people(request):
    content = "<p>Famous residents of the city.</p>"
    return HttpResponse(build_page("Famous People", content))


def history_photos(request):
    content = "<p>Historical photos of the city.</p>"
    return HttpResponse(build_page("Historical Photos", content))
