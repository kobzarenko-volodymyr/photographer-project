from django.urls import path
# from gallery.views import gallery
import gallery.views
# app_name = 'gallery'

urlpatterns = [
    path('<str:slug>/', gallery.views.AlbumDetail.as_view(), name='album'),
]
