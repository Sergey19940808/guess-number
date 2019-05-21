from django.urls import path

from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('assessment', AssessmentPsychicsView.as_view(), name='assessment'),
    path('effectivity', EffectivityView.as_view(), name='effectivity'),

]
