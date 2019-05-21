from django.views.generic import TemplateView


__all__ = [
    'MainView'
]


class MainView(TemplateView):
    template_name = 'guess_number/main.html'
