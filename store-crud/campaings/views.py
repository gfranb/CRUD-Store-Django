from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Campaing
from .forms import CreateNewCampaing

# Create your views here.
def campaings(request):
    return render(request,'campaings/list_campaings.html',{
        'campaings': Campaing.objects.all()
    })

def campaings_by_category(request, category_id):
    return render(request,'campaings/list_campaings.html',{
        'campaings': Campaing.objects.filter( category_id = category_id),
        'category_id': category_id
    })
    
def delete_campaing(request, category_id, campaing_id):
    Campaing.objects.filter(id = campaing_id).delete()
    return redirect(f'/campaings/{category_id}')

def add_campaing(request,category_id):
    if request.method == "GET":
        return render(request,'campaings/new_campaing.html',{
            'form': CreateNewCampaing,
            'category_id': category_id
        })
    else:
        Campaing.objects.create(
            name = request.POST["name"],
            category_id = category_id
            )
        return redirect(f"/campaings/{category_id}")
