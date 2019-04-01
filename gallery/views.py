from django.shortcuts import render
from django.views.generic import DetailView, ListView

from gallery.models import Album, AlbumImage


def main(request):
    return render(request, 'main.html', {})


class Albums(ListView):
    model = Album
    template_name = 'gallery/albums.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(is_visible=True).order_by('-created')
        return context


class AlbumDetail(DetailView):
    model = Album
    template_name = 'gallery/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        return context
