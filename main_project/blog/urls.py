"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageTemplateView, AboutPageTemplateView, ContactPageTemplateView, FilesView,\
    RulesAdmissionTemplateView, TherapeuticOfferTemplateView, NewsTemplateView, PersonnelTemplateView, BIPTemplateView, \
    FacebookTemplateView, RODOTemplateView, GalleryListView, GalleryDetailView, PhotoDetailView

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='blog-home'),
    path('about/', AboutPageTemplateView.as_view(), name='blog-about'),
    path('personnel/', PersonnelTemplateView.as_view(), name='blog-personnel'),
    path('news/', NewsTemplateView.as_view(), name='blog-news'),
    path('files/', FilesView.as_view(), name='download_file'),
    path('contact/', ContactPageTemplateView.as_view(), name='blog-contact'),
    path('offer/', TherapeuticOfferTemplateView.as_view(), name='blog-offer'),
    path('rules/', RulesAdmissionTemplateView.as_view(), name='blog-rules'),
    path('bip/', BIPTemplateView.as_view(), name='blog-bip'),
    path('facebook/', FacebookTemplateView.as_view(), name='blog-facebook'),
    # path('photos/', PhotosListView.as_view(), name='blog-photos'),
    path('gallery/', GalleryListView.as_view(), name='gallery-list'),
    path('gallery/<int:pk>/', GalleryDetailView.as_view(), name='gallery-detail'),
    path('gallery/<int:gallery_id>/photo/<int:photo_id>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('rodo/', RODOTemplateView.as_view(), name='blog-rodo'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
