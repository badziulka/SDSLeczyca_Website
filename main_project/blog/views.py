from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.staticfiles import finders
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views import View
import os
from django.conf import settings
from django.templatetags.static import static
# from .models import Photo
from django.views.generic import ListView, DetailView
from photologue.models import Gallery, Photo
from .models import GalleryPhoto



class HomePageTemplateView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Strona główna'
        return context


class AboutPageTemplateView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'O nas'
        return context


class NewsTemplateView(TemplateView):
    template_name = 'blog/bip.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Aktualności'
        return context


class TherapeuticOfferTemplateView(TemplateView):
    template_name = 'blog/offer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Oferta terapeutyczna'
        return context


class RulesAdmissionTemplateView(TemplateView):
    template_name = 'blog/rules.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Zasady przyjęcia'
        return context


class BIPTemplateView(TemplateView):
    template_name = 'blog/bip.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BIP ŚDS'
        return context


class RODOTemplateView(TemplateView):
    template_name = 'blog/rodo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'RODO'
        return context


class FacebookTemplateView(TemplateView):
    template_name = 'blog/facebook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Facebook'
        return context


class PersonnelTemplateView(TemplateView):
    template_name = 'blog/personnel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pracownicy'
        return context


class ContactPageTemplateView(TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Kontakt'
        return context


class FilesView(View):
    def get(self, request):
        file_path = os.path.join(settings.MEDIA_ROOT, 'zaswiadczenia_lekarzy_specjalistow.pdf')

        response = FileResponse(open(file_path, 'rb'))
        return render(request, 'blog/files.html')


# class PhotosTemplateView(TemplateView):
#     template_name = 'blog/photos.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         photos_directory = settings.MEDIA_ROOT
#         photos = os.listdir(photos_directory)
#
#         photos_list = []
#         for photo in photos:
#             if photo.endswith(('.jpg', '.png', '.jpeg', '.gif')):
#                 photos_list.append({
#                     'name': photo,
#                     'url': os.path.join(settings.MEDIA_URL, photo),
#                 })
#
#         context['photos'] = photos_list
#         return context

        # zrobic obj za kazde zdjecie i tutaj sie odwolac; wiele zdjec w jednym modelu
# class PhotosListView(ListView):
#     template_name = 'blog/photos.html'
#     model = PhotologuePhoto
#     # paginate_by = 10
#     context_object_name = 'photos'
#
#     def get_queryset(self):
#         return super().get_queryset().filter(title__isnull=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Zdjęcia naszego ośrodka'
#         return context

class GalleryListView(ListView):
    model = Gallery
    template_name = 'blog/gallery_list.html'
    context_object_name = 'galleries'


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'blog/gallery_detail.html'
    context_object_name = 'gallery'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        print("GalleryDetailView - Photos:", self.object.photos.all())
        return response

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'
    context_object_name = 'photo'

    def get_object(self, queryset=None):
        gallery = get_object_or_404(Gallery, pk=self.kwargs['gallery_id'])
        photo = get_object_or_404(Photo, pk=self.kwargs['photo_id'], galleries=gallery)
        return photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = get_object_or_404(Gallery, pk=self.kwargs['gallery_id'])
        context['gallery_photo'] = get_object_or_404(GalleryPhoto, gallery=context['gallery'], photo=context['photo'])
        return context
# class SearchPageTemplateView(ListView):
#     template_name = 'blog/search.html'
#     context_object_name = 'results'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         results = []
#
#
#         if query:
#             path = r'C:\Users\LENOVO\PycharmProjects\Django_sds_project'
#             for file in os.listdir(path):
#                 with open(os.path.join(path, file), 'r', encoding='utf-8') as file:
#                     data = file.read()
#                     if query.lower() in data.lower():
#                         results.append({'file_name': file, 'data': data})
#
#             return results