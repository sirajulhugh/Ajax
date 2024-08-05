from django.urls import path
from .import views

urlpatterns = [

    path('', views.home1, name='home1'),
    path('add_item',views.add_item,name='add_item'),
    path('get_items/', views.get_items, name='get_items'),
    path('edit_item',views.edit_item,name='edit_item'),
    path('update_item',views.update_item,name='update_item'),
    path('delete-item/', views.delete_item, name='delete_item'),

]