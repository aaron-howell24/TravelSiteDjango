# blog/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("about", views.blog_about, name="blog_about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

