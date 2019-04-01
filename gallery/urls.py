from django.urls import path
# from gallery.views import gallery
import gallery.views
# app_name = 'gallery'

urlpatterns = [
    path('', gallery.views.Albums.as_view(), name='albums'),
    path('<str:slug>/', gallery.views.AlbumDetail.as_view(), name='album_detail'),
]
