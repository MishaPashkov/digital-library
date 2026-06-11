from django.shortcuts import redirect, render, get_object_or_404
from .models import Book, Category
from .forms import BookForm
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    query = request.GET.get("q")
    category_id = request.GET.get("category")
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
    if category_id:
        books = books.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, "books/home.html", {"books": books, "query": query, "categories": categories})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/book_detail.html", {"book": book})


@staff_member_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})



@staff_member_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", book.id)
    else:
        form = BookForm(instance=book)
    return render(request, "books/edit_book.html", {"form": form, "book": book})


@staff_member_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("home")
    return render(request, "books/delete_book.html", {"book": book})


def read_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "books/read_book.html", {"book": book})