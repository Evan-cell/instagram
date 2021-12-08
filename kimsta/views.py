from django.shortcuts import render
from .models import posts #import photos model

def index(request):
    # imports photos and save it in database
    photo = posts.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'temps/insta.html', ctx)