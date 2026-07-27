from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields="__all__"
    def clean(self):
        cleaned_data=super().clean()
        title=cleaned_data.get("title")
        author=cleaned_data.get("author")

        if title and author:
            books=Book.objects.filter(title=title,author=author)

            if self.instance.pk:
                books=books.exclude(pk=self.instance.pk)

            if books.exists():
                self.add_error("title","This book already exists.")
        return cleaned_data            
