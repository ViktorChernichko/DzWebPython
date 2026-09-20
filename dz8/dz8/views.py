from django.http import HttpResponse
from datetime import datetime, timedelta


def current_time(request):
    now = datetime.now()
    text = f"Поточна дата та час: {now.strftime('%d.%m.%Y %H:%M:%S')}"
    return HttpResponse(text)


def multiplication_table(request):
    rows = []
    for i in range(1, 11):
        row = ""
        for j in range(1, 11):
            row += f"<td>{i * j}</td>"
        rows.append(f"<tr>{row}</tr>")
    table = "".join(rows)
    html = f"<table border='1'>{table}</table>"
    return HttpResponse(html)


def programmers_day(request):
    year = datetime.now().year
    date = datetime(year, 1, 1) + timedelta(days=255)
    text = f"День програміста у {year} році: {date.strftime('%d.%m.%Y')}"
    return HttpResponse(text)
