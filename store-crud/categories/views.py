from django.shortcuts import render, redirect
from .models import Category
from .forms import CreateNewCategory

# Create your views here.
def categories(request):
    return render(request,'categories/list_categories.html',{
        'categories': Category.objects.all()
    })

def add_category(request):
    if request.method == "GET":
        return render(request,'categories/new_category.html',{
            'form': CreateNewCategory
        })
    else:
        Category.objects.create(
            name = request.POST["name"]
        )
        return redirect("/categories/")
        
def delete_category(request,category_id):
    Category.objects.filter(id = category_id).delete()
    return redirect("/categories/")
