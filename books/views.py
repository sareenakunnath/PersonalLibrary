from django.shortcuts import render,redirect
from .models import Book,Category
from .form import BookForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def book_list(request):
    search=request.GET.get('search')
    category=request.GET.get('category')
    
    books = Book.objects.filter(owner=request.user)
   
    if search:
        books=books.filter(title__icontains=search)
    
    if category:
        books=books.filter(category__id=category)
       
    categories= Category.objects.all()
    paginator=Paginator(books,5)
    page_number=request.GET.get("page")
    books=paginator.get_page(page_number) 
    
       
    return render(request,"books/book_list.html",{"books":books,"categories":categories})

@login_required
def book_create(request):
    if request.method == "POST":
        form=BookForm(request.POST, request.FILES)

        if form.is_valid():
            book=form.save(commit=False)
            book.owner=request.user
            book.save()
            return redirect("book_list")
        
    else:
        form=BookForm()

    return render(request, "books/book_form.html", {"form":form}) 

@login_required
def book_update(request,pk):
    book=get_object_or_404(Book,pk=pk)
    
    if request.method == "POST":
        form=BookForm(request.POST,request.FILES,instance=book)

        if form.is_valid():
            form.save()
            return redirect("book_list")
        
    else:
        form=BookForm(instance=book)

    return render(request, "books/book_form.html", {"form":form})


@login_required
def book_delete(request,pk):
    book=get_object_or_404(Book,pk=pk)

    if request.method == "POST":
        book.delete()
       
        return redirect("book_list")
        
    return render(request, "books/book_confirm_delete.html", {"book":book})           