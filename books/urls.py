from django.urls import path
from .views import home, book_detail, add_book, edit_book, delete_book, read_book

urlpatterns = [
    path("", home, name="home"),
    path("book/<int:book_id>/", book_detail, name="book_detail"),
    path("book/add/", add_book, name="add_book"),
    path("book/<int:book_id>/edit/", edit_book, name="edit_book"),
    path("book/<int:book_id>/delete/", delete_book, name="delete_book"),
    path("book/<int:book_id>/read/", read_book, name="read_book"),
]