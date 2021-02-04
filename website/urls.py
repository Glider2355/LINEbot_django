from django.urls import path

from .views import IndexView, PistoView


urlpatterns = [
    path('', IndexView.as_view()),
    path('pisto/', PistoView.as_view()),
]
