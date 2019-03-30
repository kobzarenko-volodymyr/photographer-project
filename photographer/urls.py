"""photographer URL Configuration."""

from django.contrib import admin
from django.urls import path  # include
from gallery.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('blog/', include('blog.urls')),
]
