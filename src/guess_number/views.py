from django.views.generic import View
from django.shortcuts import render, redirect

from store.store import Store
from guess_number.utils import build_context, assessmented_psychics

__all__ = [
    'MainView',
    'AssessmentPsychicsView',
]


class BaseView(View):
    template_name = 'guess_number/main.html'
    store = Store()
    context = build_context(store)


class MainView(BaseView):
    def get(self, request, *args, **kwargs):
        return render(request, 'guess_number/main.html', self.context)


class AssessmentPsychicsView(BaseView):
    def get(self, request, *args, **kwargs):
        assessment_psychics = assessmented_psychics(self.context['psychics'], request.GET.get('number_user'))
        self.store.set('history_numbers', self.store.get('history_numbers').append())
        return redirect('main')
