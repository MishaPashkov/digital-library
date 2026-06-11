from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        
        fields = [
            "title",
            "description",
            "publication_year",
            "cover",
            "author",
            "category",
            "available",
            "pdf_file"
        ]