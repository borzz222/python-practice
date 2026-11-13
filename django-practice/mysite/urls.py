from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
]