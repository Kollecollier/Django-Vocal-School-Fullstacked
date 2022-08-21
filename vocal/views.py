"Django project view's"
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class AppointmentTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("femail")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")

        messages.add_message(request, messages.SUCCESS, f"{message}")
        return HttpResponseRedirect(request.path)
