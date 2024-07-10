
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name='index'),
    path("register/", views.register,name='register'),
    path("remove/<int:pk>/", views.remove,name='remove'),
    path("add_quotes/", views.add_quotes,name='add_quotes'),
    path("all_quotes/", views.all_quotes,name='all_quotes'),
    path("remove_quote/<int:pk>/", views.remove_quote,name='remove_quote'),
    
]