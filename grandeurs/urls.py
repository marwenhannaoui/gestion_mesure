from django.urls import path

from . import views

#domain.com/meetings/...
urlpatterns=[
    path('<int:id>',views.detail, name="detail"),    
    path('grandeurs', views.grandeurs_list, name="grandeurs"),
    path('new', views.new, name="new"),
    path('delete-grandeur/<int:id>', views.DeleteGrandeur, name='delete-grandeur'),

]