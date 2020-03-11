from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from registration.models import BirthRegistration, DeathRegistration, RegistrationCentre
# Create your views here.
from .forms import SearchForm
from django.http import HttpResponse
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.text import slugify

# from .print_certificates import *
birth_Title = "National Government of Kenya"
birth_page_info = "Birth Certificate"


def view_birth_applicant(request, id):
    applicant = get_object_or_404(BirthRegistration, id=id)
    return render(request, 'cert_management/birth_applicant_detail.html', {'applicant': applicant})


def view_death_applicant(request, id):
    applicant = get_object_or_404(DeathRegistration, person=id)
    return render(request, 'cert_management/death_applicant_detail.html', {'applicant': applicant})


def filter_apllicant(request):
    death_applicant = DeathRegistration.objects.all()


@login_required
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
    return render(request, 'cert_management/birth_search.html',
                  {'form': form, 'query': query, 'results': results})


@login_required()
def death_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            death_query = DeathRegistration.objects.all()
            # death_query = BirthRegistration.objects.filter(alive=False)
            # if death_query.person in birth_query.id:
            # results = DeathRegistration.objects.annotate(
            #     search=SearchVector('death_cert_no'),
            # ).filter(search=query)
            results = death_query.annotate(
                search=SearchVector('death_cert_no'),
            ).filter(search=query)
    return render(request, 'cert_management/death_search.html',
                  {'form': form, 'query': query, 'results': results})


@login_required()
def print_birth_certificate(request, id):
    applicant = get_object_or_404(BirthRegistration, id=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "inline; filename={first_name}-{surname}-{birth_cert_no}-certificate.pdf".format(
        first_name=applicant.first_name,
        surname=applicant.surname,
        birth_cert_no=applicant.birth_cert_no,
    )
    if request.user.is_staff:
        current_user = request.user
        birth_date = applicant.date_of_birth.strftime("%d/%m/%Y")
        add_date = applicant.birth_reg_date.strftime("%d/%m/%Y")
        update_date = applicant.birth_reg_updated.strftime("%d/%m/%Y")
        html = render_to_string("cert_management/birth_certificate.html", {
            'applicant': applicant, 'current_user': current_user, 'birth_date': birth_date,
            'add_date': add_date, 'update_date': update_date})
        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response
    else:
        e = 'You are not authorized to access this page'
        h = render(request, "cert_management/birth_error.html", {
            'applicant': applicant, 'e': e})
        return h


@login_required()
def print_death_certificate(request, id):
    applicant = get_object_or_404(DeathRegistration, person=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "inline; filename={first_name}-{surname}-{birth_cert_no}-certificate.pdf".format(
        first_name=applicant.person.first_name,
        surname=applicant.person.surname,
        birth_cert_no=applicant.death_cert_no,
    )
    if request.user.is_staff:
        current_user = request.user
        age = int((applicant.date_of_death - applicant.person.date_of_birth).days / 365.25)
        death_date = applicant.date_of_death.strftime("%d/%m/%Y")
        add_date = applicant.death_reg_date.strftime("%d/%m/%Y")
        update_date = applicant.death_reg_updated.strftime("%d/%m/%Y")
        html = render_to_string("cert_management/death_certificate.html", {
            'applicant': applicant, 'current_user': current_user, 'age': age, 'death_date': death_date,
            'add_date': add_date, 'update_date': update_date})
        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response
    else:
        e = 'You are not authorized to access this page'
        h = render(request, "cert_management/birth_error.html", {
            'applicant': applicant, 'e': e})
        return h
