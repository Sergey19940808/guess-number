from django.shortcuts import render, redirect

from libs.views import *
from guess_number.forms import *


__all__ = [
    'MainView',
    'AssessmentPsychicsView',
    'EffectivityView',
]


class MainView(BaseView):
    def get(self, request, *args, **kwargs):
        context = self.user.data.copy()
        self.clean_field_form()
        return render(request, 'guess_number/main.html', context)

    def clean_field_form(self):
        if self.user.data.get('form'):
            self.user.data.pop('form')
            self.sync_store()


class AssessmentPsychicsView(BaseView):
    def get(self, request, *args, **kwargs):
        assessment_psychics = self.assessmented_psychics(self.user.get('psychics'))

        self.user.set('is_assessment', True)
        self.user.set('assessments_map', assessment_psychics)
        self.user.set('assessments', [assessment for assessment in assessment_psychics.values()])
        self.user.set('psychics', self.user.psychic.update_assumptions(assessment_psychics))

        self.sync_store()

        return redirect('main')


class EffectivityView(BaseView):
    def get(self, request, *args, **kwargs):
        number = request.GET.get('number')
        form = NumberForm(data=request.GET)

        if form.errors:
            self.user.set('form', form)
            self.sync_store()
            return redirect('main')

        self.user.update_index_effectivity(number)

        self.user.set('numbers', self.user.get('numbers') + [number])

        self.user.remove('assessments')
        self.user.remove('assessments_map')
        self.user.remove('is_assessment')

        self.sync_store()

        return redirect('main')
