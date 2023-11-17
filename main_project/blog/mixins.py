from photologue.models import Gallery


class ExtraContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = Gallery.objects.latest('id')
        return context
