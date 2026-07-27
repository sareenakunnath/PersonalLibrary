from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    description=models.TextField()
    published_date=models.DateField()
    
    cover =models.ImageField(
        upload_to="book_covers/",
        null=True,
        blank=True)

    category=models.ForeignKey(Category,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )
    owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    def __str__(self):
        return self.title
    
