"Django project view's"
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render
from .models import Appointment


def index(request):
    return render(request, 'index.html')


class HomeTemplateView(TemplateView):
    template_name = "index.html"


class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            mobile=mobile,
            request=message,
        )

        appointment.save()
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    login_reqired = True
    model = Appointment
    context_object_name = "appointments"
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({"title": "Manage Appointments"})
        return context
