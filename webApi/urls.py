from django.urls import path

from . import views

urlpatterns = [
path('get',views.getData),
path('post/',views.postData),
path('delete/<int:pk>',views.delete_items),
path('update/<int:pk>/', views.update_items,),

]