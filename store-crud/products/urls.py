from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:campaing_id>',views.products_by_campaing, name="productos_by_campaing"),
    path('products/',views.products, name="products"),
    path('products/<int:campaing_id>/new', views.new_product, name="new_product"),
    path('products/<int:campaing_id>/<int:product_id>/delete', views.delete_product, name="delete_product"),
    path('products/<int:campaing_id>/edit/<int:product_id>', views.edit_product)
]
