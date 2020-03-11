from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User, Group
import datetime
from registration.models import RegistrationCentre
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    registration_centre = models.ForeignKey(RegistrationCentre, related_name='employees_reg_centres',
                                            on_delete=models.CASCADE, default=3)
    photo = models.ImageField(upload_to='employees/%Y/%m/%d', blank=True)
    # slug = models.SlugField(max_length=250)

    def __str__(self):
        return 'Registration Centre for user {}'.format(self.user.username)
