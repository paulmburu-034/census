from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core import serializers
from registration.models import BirthRegistration, DeathRegistration
# Create your views here.


def alive_population_information(request):
    data = serializers.serialize("json", BirthRegistration.objects.filter(alive=True))

    return HttpResponse(data, content_type="application/json")


def dead_population_information(request):
    death_results = BirthRegistration.objects.filter(alive=False)
    data = serializers.serialize("json", death_results)

    return HttpResponse(data, content_type="application/json")


def death_analysis_information(request):
    death_results = DeathRegistration.objects.all()

    data = serializers.serialize("json", death_results)

    return HttpResponse(data, content_type="application/json")


def analysis_information(request):
    return render(request, 'analysis/analysis.html')