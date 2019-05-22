from django.urls import path, include

urlpatterns = [
    path('', include('guess_number.urls')),
]
