from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name="categories"),
    path('categories/', views.categories, name="categories"),
    path('categories/new', views.add_category),
    path('categories/<int:category_id>/delete',views.delete_category),
    path('categories/<int:category_id>/edit', views.edit_category)
]