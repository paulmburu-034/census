from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


# Create your models here.


class RegistrationCentre(models.Model):
    COUNTIES_CHOICES = (
        ('nairobi', 'Nairobi'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('mombasa', 'Mombasa'),
        ('nyeri', 'Nyeri'),
        ('uasin gishu', 'Uasin Gishu'),
        ('baringo', 'Baringo'),
        ('narok', 'Narok'),
    )
    REGISTRATION_CENTRE_TYPE_CHOICES = (
        ('police post', 'POLICE POST'),
        ('hospital', 'HOSPITAL'),
        ('health centre', 'HEALTH CENTRE'),
        ('dispensary', 'DISPENSARY'),
        ('registrar office', 'REGISTRAR OFFICE')
    )
    reg_centre_name = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Registration centre name must be in Character format',
            code='invalid_reg_centre_name'
        ),
    ])
    reg_centre_type = models.CharField(max_length=50, choices=REGISTRATION_CENTRE_TYPE_CHOICES, default='hospital')
    reg_centre_county = models.CharField(max_length=50, choices=COUNTIES_CHOICES, default='nairobi')
    reg_centre_email = models.EmailField(max_length=50, validators=[
        RegexValidator(
            regex=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            message='Enter correct email format',
            code='invalid_email'
        ),
    ])
    reg_centre_location = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^[a-zA-Z]*$',
            message='Registration Centre location must be in Character format',
            code='invalid_reg_centre_location'
        ),
    ])
    reg_author = models.ForeignKey(User, related_name='admins', on_delete=models.PROTECT)
    reg_date = models.DateTimeField(auto_now_add=True)
    reg_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reg_centre_name


class BirthRegistration(models.Model):
    GENDER_CHOICES = (
        ('male', 'M'),
        ('female', 'F'),
    )
    COUNTIES_CHOICES = (
        ('nairobi', 'Nairobi'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('mombasa', 'Mombasa'),
        ('nyeri', 'Nyeri'),
        ('uasin gishu', 'Uasin Gishu'),
        ('baringo', 'Baringo'),
        ('narok', 'Narok'),
    )
    first_name = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^[A-Za-z]*$',
            message='First Name must be in Character format',
            code='invalid_first_name'
        ),
    ])
    middle_name = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^[A-Za-z]*$',
            message='Middle Name must be in Character format',
            code='invalid_middle_name'
        ),
    ])
    surname = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^[A-Za-z]*$',
            message='Surname must be in Character format',
            code='invalid_surname'
        ),
    ])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    date_of_birth = models.DateTimeField(blank=False)
    mothers_name = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^[A-Za-z ]*$',
            message='Mothers name must be in Character format',
            code='invalid_mothers_name'
        ),
    ])
    fathers_name = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^[A-Za-z ]*$',
            message='Fathers name must be in Character format',
            code='invalid_fathers_name'
        ),
    ])
    county = models.CharField(max_length=50, choices=COUNTIES_CHOICES, default='nairobi')
    constituency = models.CharField(max_length=300, validators=[
        RegexValidator(
            regex='^[A-Za-z ]*$',
            message='Constituency must be in Character format',
            code='invalid_constituency'
        ),
    ])
    reference_number = models.CharField(max_length=50, blank=True)
    id_no = models.CharField(max_length=50, blank=True, validators=[
        RegexValidator(
            regex='^[0-9]*$',
            message='Id Number must be in Numbers only',
            code='invalid_constituency'
        ), MaxLengthValidator(8)
        , MinLengthValidator(7)])
    birth_reg_centre = models.ForeignKey(RegistrationCentre, related_name='birth_registration_centres',
                                         on_delete=models.CASCADE)
    birth_cert_no = models.CharField(max_length=250, unique=True)
    birth_author = models.ForeignKey(User, related_name='employers', on_delete=models.PROTECT)
    birth_reg_date = models.DateTimeField(auto_now_add=True)
    birth_reg_updated = models.DateTimeField(auto_now=True)
    alive = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('certmanagement:birth_applicant_detail', args=[self.id, ])


class DeathRegistration(models.Model):
    STATUS_CHOICES = (
        ('single', 'SINGLE'),
        ('married', 'MARRIED'),
        ('child', 'CHILD'),
    )
    CHILDREN_STATUS_CHOICES = (
        ('yes', 'YES'),
        ('no', 'NO'),
    )
    COUNTIES_CHOICES = (
        ('nairobi', 'Nairobi'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('mombasa', 'Mombasa'),
        ('nyeri', 'Nyeri'),
        ('uasin gishu', 'Uasin Gishu'),
        ('baringo', 'Baringo'),
        ('narok', 'Narok'),
    )
    person = models.OneToOneField(BirthRegistration, related_name='persons', on_delete=models.CASCADE, unique=True)
    date_of_death = models.DateTimeField(blank=False)
    current_county = models.CharField(max_length=50, choices=COUNTIES_CHOICES, default='nairobi')
    death_reg_centre = models.ForeignKey(RegistrationCentre, related_name='death_registration_centres',
                                         on_delete=models.CASCADE)
    current_constituency = models.CharField(max_length=300, validators=[
        RegexValidator(
            regex='^[A-Za-z ]*$',
            message='Current Constituency must be in Character format',
            code='invalid_current_constituency'
        ),
    ])
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='single')
    children = models.CharField(max_length=50, choices=CHILDREN_STATUS_CHOICES, default='no')
    children_no = models.PositiveIntegerField(blank=True, null=True)
    cause_of_death = models.CharField(max_length=300, blank=False, validators=[
        RegexValidator(
            regex='^[A-Za-z ]*$',
            message='Cause of death must be in Character format',
            code='invalid_cause_of_death'
        ),
    ])
    occupation = models.CharField(max_length=300, blank=False, validators=[
        RegexValidator(
            regex='^[A-Za-z ]*$',
            message='Occupation must be in Character format',
            code='invalid_occupation'
        ),
    ])
    death_cert_no = models.CharField(max_length=250, unique=True)
    death_author = models.ForeignKey(User, related_name='users', on_delete=models.PROTECT)
    death_reg_date = models.DateTimeField(auto_now_add=True)
    death_reg_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person

    def get_absolute_url(self):
        return reverse('certmanagement:death_applicant_detail', args=[self.id, ])
