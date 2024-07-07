from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def my_hello_view(request):
  visitor_name = request.GET.get("visitor_name")
  greeting = f"Hello, {visitor_name}!"
  response = {"greeting": greeting}
  return JsonResponse(response)