from django.shortcuts import render, redirect

from libs.views import *


__all__ = [
    'MainView',
    'AssessmentPsychicsView',
    'EffectivityView',
]


class MainView(BaseView):
    def get(self, request, *args, **kwargs):
        # if not context.get('redirect') and context.get('error'):
        #     context.pop('error')
        # elif self.user.get('redirect') and self.user.get('error'):
        #     self.user.pop('redirect')
        #     self.user.pop('error')
        return render(request, 'guess_number/main.html', self.user.data)


class AssessmentPsychicsView(BaseView):
    def get(self, request, *args, **kwargs):
        number = request.GET.get('number_user')

        # self.user['redirect'] = True
        # if len(str(number)) != 2:
        #     self.user['error'] = 'Неверное число. Принимаются только двухзначные числа'
        #     return redirect('main')

        assessment_psychics = self.assessmented_psychics(self.user.data['psychics'], number)

        self.user.data['numbers'].append(number)
        self.user.data['psychics'] = self.user.psychic.update_assumptions(assessment_psychics)
        self.user.data['is_assessment'] = True
        self.user.data['assessments_map'] = assessment_psychics
        self.user.data['assessments'] = [assessment for assessment in assessment_psychics.values()]
        self.user.data['number'] = number
        self.store.set(self.mac, self.user.data)

        return redirect('main')


class EffectivityView(BaseView):
    def get(self, request, *args, **kwargs):
        self.user.update_index_effectivity()

        self.user.data.pop('assessments')
        self.user.data.pop('assessments_map')
        self.user.data.pop('is_assessment')
        self.user.data.pop('number')

        self.store.set(self.mac, self.user.data)

        return redirect('main')
