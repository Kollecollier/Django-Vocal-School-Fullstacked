"View testing"
from django.test import TestCase

class TestViews(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'vocal_school/index.html')

    def test_ManageAppointmentTemplateView(self):
        response = self.client.get('/manage-appointments/')
        self.assertTemplateNotUsed(response, 'vocal_school/manage-appointments.html')

    def test_AppointmentTemplateView(self):
        response = self.client.get('/appointment/')
        self.assertTemplateNotUsed(response, 'vocal_school/appointments.html')