# import the standard Django Model
# from built-in library
from django.db import models
from cloudinary.models import CloudinaryField


# declare a new model with a name "post" to store data

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    # image field
    image = CloudinaryField('image')


class Post(models.Model):
    # fields of the model
    fname = models.CharField(max_length=30, null=False, blank=False)
    lname = models.CharField(max_length=30, null=False, blank=False)
    mobile = models.CharField(max_length=30, null=False, blank=False)
    message = models.CharField(max_length=30, null=False, blank=False)


class Appointment(models.Model):
    # Appointment model
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]
