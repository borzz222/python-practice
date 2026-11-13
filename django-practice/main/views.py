from django.http import Http404, HttpResponse
from django.shortcuts import render

BOOKS = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "М. Булгаков", "year": 1967, "price": 650},
    {"id": 2, "title": "Преступление и наказание", "author": "Ф. Достоевский", "year": 1866, "price": 520},
    {"id": 3, "title": "Война и мир", "author": "Л. Толстой", "year": 1869, "price": 1250},
]


def index(request):
    return HttpResponse("Привет, это мой первый сайт на Django!")


def book_list(request):
    """Страница со списком всех книг."""
    return render(request, "main/book_list.html", {"books": BOOKS})


def book_detail(request, book_id):
    """Страница с информацией об одной книге."""
    for book in BOOKS:
        if book["id"] == book_id:
            return render(request, "main/book_detail.html", {"book": book})
    raise Http404("Книга не найдена")