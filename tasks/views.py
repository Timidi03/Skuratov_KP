from django.shortcuts import render
from django.shortcuts import render

def index(request):
  return render(request, "index.html", {"FIREBASE_API_KEY":'1234'})
  