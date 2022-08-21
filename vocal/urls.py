"Django backend urls and patterns"

from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("appointment", AppointmentTemplateView.as_view(), name="appointment"),
]
