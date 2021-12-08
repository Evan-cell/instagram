from django.shortcuts import render
from .models import posts

# Create your views here.
def insta(request):
   return render(request, 'temps/insta.html')