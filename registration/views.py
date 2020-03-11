from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from .forms import BirthRegistrationForm, DeathRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import BirthRegistration, DeathRegistration
from .auto_generate_birth_death_number import birth_cert_number, death_cert_number, increment_cert_number
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from datetime import datetime


# Create your views here.


def home_page(request):
    return render(request, 'registration/index.html')


@login_required
def birth_registration(request):
    cert_number = None
    try:
        birth_results = BirthRegistration.objects.last()
    except IndexError:
        birth_results = None

    if birth_results is None:
        cert_number = birth_cert_number(1)
    else:
        birth_certificate_number = birth_results.birth_cert_no
        new_cert_number = increment_cert_number(birth_certificate_number)
        cert_number = birth_cert_number(new_cert_number)

    if request.method == 'POST':
        birth_form = BirthRegistrationForm(data=request.POST)
        if birth_form.is_valid():
            # Create a new birth object but avoid saving it yet
            new_birth = birth_form.save(commit=False)
            # Set the chosen password
            new_birth.birth_author = request.user
            new_birth.birth_cert_no = cert_number
            try:
                id_number = BirthRegistration.objects.filter(id_no=new_birth.id_no)
                birth_notification = BirthRegistration.objects.filter(reference_number=new_birth.reference_number)
                if birth_notification == new_birth.reference_number and id_number == new_birth.id_no:
                    e = 'this data already exists in the database'
                    return render(request, 'registration/register_birth_error.html', {'form': birth_form, 'e': e})
                elif new_birth.date_of_birth <= datetime.now():
                    new_birth.save()
                    e = 'this record has been added successfully'
                    return render(request, 'registration/birth_register_done.html', {'new_birth': cert_number, 'e': e})
                else:
                    e = 'Enter a valid date'
                    return render(request, 'registration/register_birth_error.html', {'form': birth_form, 'e': e})
            except IntegrityError as e:
                e = 'this data already exists in the database'
                return render(request, "registration/register_birth_error.html", context={'form': birth_form, 'e': e})
    else:
        birth_form = BirthRegistrationForm()
    return render(request, 'registration/birth_registration.html', {'birth_form': birth_form})


@login_required
def death_registration(request, person_id):
    applicant = get_object_or_404(BirthRegistration, id=person_id)
    cert_number = None
    try:
        death_results = DeathRegistration.objects.last()
    except IndexError:
        death_results = None

    if death_results is None:
        cert_number = death_cert_number(1)
    else:
        death_certificate_number = death_results.death_cert_no
        new_cert_number = increment_cert_number(death_certificate_number)
        cert_number = death_cert_number(new_cert_number)
    if request.method == 'POST':
        death_form = DeathRegistrationForm(data=request.POST)
        if death_form.is_valid():
            # Create a new death object but avoid saving it yet
            new_death = death_form.save(commit=False)
            # Set the chosen password
            new_death.death_author = request.user
            new_death.person = applicant
            new_death.death_cert_no = cert_number
            try:
                if new_death.date_of_death <= datetime.now():
                    new_death.save()
                    applicant.alive = False
                    applicant.save()
                    e = 'Data added successfully'
                    return render(request, 'registration/death_register_done.html', context={'form': death_form,
                                                                                             'new_death': cert_number,
                                                                                             'e': e})
            except IntegrityError as e:
                e = 'this data already exists in the database'
                return render(request, "registration/death_register_done.html", context={'form': death_form, 'e': e})
    else:
        death_form = DeathRegistrationForm()
    return render(request, 'registration/death_registration.html', {'death_form': death_form, 'applicant': applicant})


def certificate_management(request):
    return render(request, 'registration/certificate_management.html')


@login_required()
def birth_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            birth_query = BirthRegistration.objects.filter(alive=True)
            results = birth_query.annotate(
                search=SearchVector('first_name', 'middle_name', 'surname'),
            ).filter(search=query)
    return render(request, 'registration/birth_search.html',
                  {'form': form, 'query': query, 'results': results})
