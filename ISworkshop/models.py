from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField()
    student_number = models.CharField(max_length=12, default='', blank=True, null=True,)
    last_name = models.CharField(max_length=200, default='', blank=True, null=True,)
    first_name = models.CharField(max_length=200, default='', blank=True, null=True,)
    graduation_year = models.CharField(max_length=200, default='', blank=True, null=True,)
    date_joined = models.DateField(max_length=200, default='', blank=True, null=True,)
    last_login = models.DateTimeField(max_length=200, default='', blank=True, null=True,)
    degree = models.CharField(max_length=200, default='', blank=True, null=True,)
    program = models.CharField(max_length=200, default='', blank=True, null=True,)
    image = models.ImageField(default='default.jpg', upload_to='static')
    city = models.CharField(max_length=200, default='', blank=True, null=True,)
    CAPES_miles_points = models.CharField(max_length=200, default='', blank=True, null=True,)