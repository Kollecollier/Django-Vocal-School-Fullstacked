# import the standard Django Model
# from built-in library
from django.contrib.auth.models import User
from django.db import models

# declare a new model with a name "post" to store data


class Post(models.Model):
    # fields of the model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=30, null=False, blank=False)
    lname = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    mobile = models.CharField(max_length=30, null=False, blank=False)
    message = models.CharField(max_length=30, null=False, blank=False)
