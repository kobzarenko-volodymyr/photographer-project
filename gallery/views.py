from django.shortcuts import render
from django.views.generic import DetailView

from gallery.models import Album, AlbumImage
# def home(request):
#     return render(request, 'gallery/home.html', {})


def home(request):
    albums = Album.objects.filter(is_visible=True).order_by('-created')
    return render(request, 'gallery/home.html', {'albums': albums})


class AlbumDetail(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context
