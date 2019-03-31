from django.shortcuts import render
# Create your views here.
from gallery.models import Album


# def home(request):
#     return render(request, 'gallery/home.html', {})

def home(request):
    albums = Album.objects.filter(is_visible=True).order_by('-created')
    return render(request, 'gallery/home.html', {'albums': albums})
