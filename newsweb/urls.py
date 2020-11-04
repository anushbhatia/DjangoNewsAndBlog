from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.home,name='news'),
]