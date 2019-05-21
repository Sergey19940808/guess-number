from django.views.generic import View
from django.shortcuts import render, redirect

from store.store import Store

__all__ = [
    'MainView'
]


class MainView(View):
    PSYCHICS = [
        {'name': 'Vlad', 'index_effectivity': 0},
        {'name': 'Genady', 'index_effectivity': 0},
        {'name': 'Petr', 'index_effectivity': 0}
    ]
    template_name = 'guess_number/main.html'
    store = Store()

    def get(self, request, *args, **kwargs):
        psychics = self.create_or_get_psychics()
        if request.GET.get('number_user'):
            return redirect('main')
        else:
            return render(request, 'guess_number/main.html', {'psychics': psychics})

    def create_or_get_psychics(self):
        """
        Метод для создания и/или получения экстрасенсов
        :return:
        """
        if self.store.get('psychics'):
            return self.store.get('psychics')
        else:
            self.store.set('psychics', self.PSYCHICS)
            return self.store.get('psychics')
