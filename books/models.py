from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_year = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='books/', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title