from django.shortcuts import render, redirect

from libs.views import *
from libs.utils import (
    build_context,
    assessmented_psychics,
    update_assumptions,
    update_index_effectivity,
)

__all__ = [
    'MainView',
    'AssessmentPsychicsView',
    'EffectivityView',
]


class MainView(BaseView):
    def get(self, request, *args, **kwargs):
        context = build_context(self.store)
        return render(request, 'guess_number/main.html', context)


class AssessmentPsychicsView(BaseView):
    def get(self, request, *args, **kwargs):
        number = request.GET.get('number_user')
        assessment_psychics = assessmented_psychics(self.context['psychics'], number)

        self.user['numbers'].append(number)
        self.user['psychics'] = update_assumptions(self.user['psychics'], assessment_psychics)
        self.user['is_assessment'] = True
        self.user['assessments_map'] = assessment_psychics
        self.user['assessments'] = [assessment for assessment in assessment_psychics.values()]
        self.user['number'] = number
        self.store.set(self.mac, self.user)
        return redirect('main')


class EffectivityView(BaseView):
    def get(self, request, *args, **kwargs):
        update_index_effectivity(self.user)

        self.user.pop('assessments')
        self.user.pop('assessments_map')
        self.user.pop('is_assessment')
        self.user.pop('number')

        self.store.set(self.mac, self.user)

        return redirect('main')
