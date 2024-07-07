from django.urls import path
from . import views

urlpatterns = [
   path('api/hello/', views.my_hello_view, name='hello_api'),
]