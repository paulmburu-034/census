from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core import serializers
from registration.models import BirthRegistration, DeathRegistration
# Create your views here.


def alive_population_information(request):
    try:
        alive = BirthRegistration.objects.all()
        dead = DeathRegistration.objects.all()
    except IndexError:
        alive = None
        dead = None
    total_alive = None
    total_dead = None
    if alive and dead is not None:
        for the_alive in alive.id:
            if the_alive in dead.person:
                total_dead = False
            else:
                data = serializers.serialize("xml", BirthRegistration.objects.all())
                total_alive = True
    else:
        data = serializers.serialize("xml", 'no available data')
    return HttpResponse(data, content_type="application/xml")


def dead_population_information(request):
    try:
        alive = BirthRegistration.objects.all()
        dead = DeathRegistration.objects.all()
    except IndexError:
        alive = None
        dead = None
    total_alive = None
    total_dead = None
    if alive and dead is not None:
        if alive.id in dead.person:
            data = serializers.serialize("xml", BirthRegistration.objects.all())
            total_dead = True
        else:
            total_alive = False
    else:
        data = serializers.serialize("xml", 'no death data is available')
    return HttpResponse(data, content_type="application/xml")

def dead_population_information(request):
    results = {}
    try:
        death_results = DeathRegistration.objects.all()
        birth_results = BirthRegistration.objects.all()
    except IndexError:
        death_results = None

    if death_results is None:
        data = serializers.serialize("xml", 'No data available')
    else:
        for data in death_results:
            results['first_name'] = data.person.first_name


        data = serializers.serialize("xml", death_results + death_results.persons)

    return HttpResponse(data, content_type="application/xml")

