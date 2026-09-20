from django.http import HttpResponse
from django.shortcuts import redirect

WRITERS = {
    "Hemingway": {
        "full_name": "Ernest Hemingway",
        "info": "American novelist and short story writer, Nobel Prize winner in Literature.",
        "books": {
            "The_Old_Man_and_the_Sea": {
                "title": "The Old Man and the Sea",
                "year": 1952,
                "info": "A short novel about an aging Cuban fisherman.",
            },
            "The_Sun_Also_Rises": {
                "title": "The Sun Also Rises",
                "year": 1926,
                "info": "A novel about American and British expatriates in Europe.",
            },
        },
    },
    "Shakespeare": {
        "full_name": "William Shakespeare",
        "info": "English playwright, poet and actor.",
        "books": {
            "Hamlet": {
                "title": "Hamlet",
                "year": 1600,
                "info": "A tragedy about Prince Hamlet of Denmark.",
            },
            "Macbeth": {
                "title": "Macbeth",
                "year": 1606,
                "info": "A tragedy about ambition and power.",
            },
        },
    },
}

TOP_BOOKS = {
    1: {"title": "The Old Man and the Sea", "author": "Hemingway"},
    2: {"title": "Hamlet", "author": "Shakespeare"},
    3: {"title": "The Sun Also Rises", "author": "Hemingway"},
}


def build_page(title, content):
    nav = """
    <nav>
        <a href="/">Home</a> |
        <a href="/writers/">Writers</a> |
        <a href="/books/">Top Books</a>
    </nav>
    <hr>
    """
    return f"<h1>{title}</h1>{nav}{content}"


def home(request):
    content = "<p>Welcome to the writers information website.</p>"
    return HttpResponse(build_page("Home", content))


def writers(request):
    writer_param = request.GET.get("writers")
    year_param = request.GET.get("year")

    if writer_param:
        writer = WRITERS.get(writer_param)
        if not writer:
            return redirect("writers")

        if year_param:
            matches = [
                book for book in writer["books"].values()
                if str(book["year"]) == year_param
            ]
            if not matches:
                return redirect("writer_detail", name=writer_param)

            items = "".join(f"<li>{book['title']} ({book['year']})</li>" for book in matches)
            content = f"<p>Books by {writer['full_name']} in {year_param}:</p><ul>{items}</ul>"
            return HttpResponse(build_page(f"{writer['full_name']} — {year_param}", content))

        return redirect("writer_detail", name=writer_param)

    items = "".join(
        f'<li><a href="/writers/{name}/">{data["full_name"]}</a></li>'
        for name, data in WRITERS.items()
    )
    content = f"<ul>{items}</ul>"
    return HttpResponse(build_page("Writers", content))


def writer_detail(request, name):
    writer = WRITERS.get(name)
    if not writer:
        return redirect("writers")

    items = "".join(
        f'<li><a href="/writers/{name}/{key}/">{book["title"]}</a> ({book["year"]})</li>'
        for key, book in writer["books"].items()
    )
    content = f"<p>{writer['info']}</p><ul>{items}</ul>"
    return HttpResponse(build_page(writer["full_name"], content))


def writer_book(request, name, book_key):
    writer = WRITERS.get(name)
    if not writer:
        return redirect("writers")

    book = writer["books"].get(book_key)
    if not book:
        return redirect("writer_detail", name=name)

    content = f"<p>Author: {writer['full_name']}</p><p>Year: {book['year']}</p><p>{book['info']}</p>"
    return HttpResponse(build_page(book["title"], content))


def books(request):
    items = "".join(
        f'<li><a href="/books/{position}/">{position}. {book["title"]}</a></li>'
        for position, book in TOP_BOOKS.items()
    )
    content = f"<ul>{items}</ul>"
    return HttpResponse(build_page("Top Books", content))


def book_by_position(request, position):
    book = TOP_BOOKS.get(position)
    if not book:
        return redirect("books")

    writer = WRITERS.get(book["author"])
    full_name = writer["full_name"] if writer else book["author"]
    content = f"<p>Position: {position}</p><p>Title: {book['title']}</p><p>Author: {full_name}</p>"
    return HttpResponse(build_page(book["title"], content))
