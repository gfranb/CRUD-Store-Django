from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Campaing
from .forms import CreateNewCampaing

# Create your views here.
def campaings(request):
    return render(request,'campaings/list_campaings.html',{
        'campaings': Campaing.objects.all(),
        'nofilter': False
    })

def campaings_by_category(request, category_id):
    return render(request,'campaings/list_campaings.html',{
        'campaings': Campaing.objects.filter( category_id = category_id),
        'category_id': category_id,
        'nofilter': True
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

def edit_campaing(request, category_id, campaing_id):
    if request.method == 'GET':
        campaing_queryset = Campaing.objects.filter(id = campaing_id)
        if(campaing_queryset.exists()):
            campaing = campaing_queryset.first()
            initial_data = {
                'name' : campaing.name,
            }
        return render(request, "campaings/edit_campaing.html",{
            'form': CreateNewCampaing(initial=initial_data),
        })
    else:
        if request.method == 'POST' and request.POST.get('_method') == 'PUT':
            Campaing.objects.filter(id = campaing_id).update(
                name = request.POST['name']
            )
        return redirect(f'/campaings/{category_id}')
