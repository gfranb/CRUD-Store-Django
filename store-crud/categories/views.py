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

def edit_category(request, category_id):
    if request.method == 'GET':
        category_queryset = Category.objects.filter(id = category_id)
        if(category_queryset.exists()):
            category = category_queryset.first()
            initial_data = {
                'name' : category.name,
            }
        return render(request, "categories/edit_category.html",{
            'form': CreateNewCategory(initial=initial_data),
        })
    else:
        if request.method == 'POST' and request.POST.get('_method') == 'PUT':
            Category.objects.filter(id = category_id).update(
                name = request.POST['name']
            )
        return redirect(f'/categories/')
