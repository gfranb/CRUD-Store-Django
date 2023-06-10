from django.urls import path
from . import views

urlpatterns = [
    path('campaings/', views.campaings, name="campaings"),
    path('campaings/<int:category_id>', views.campaings_by_category, name="campaing_by_id"),
    path('campaings/<int:category_id>/<int:campaing_id>/delete', views.delete_campaing, name="delete_campaing"),
    path('campaings/<int:category_id>/new', views.add_campaing, name="add_campaing"),
    path('campaings/<int:category_id>/<int:campaing_id>/edit', views.edit_campaing)
]