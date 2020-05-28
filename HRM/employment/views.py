from django.shortcuts import render
from .models import Employment
from django.http import HttpResponseRedirect, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


def index(request):
    employment = Employment.objects.all()
    return render(request, 'index.html', {'employment': employment})


def new(request):
    return render(request, 'new_applicant.html')


@csrf_exempt
def new_update(request):
    new_applicant = Employment.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        gender=request.POST["gender"],
        national_id=request.POST["national_id"],
        year_of_birth=request.POST["year_of_birth"],
        date_of_completion=timezone.datetime.today())
    new_applicant.save()
    return HttpResponseRedirect("/")


def details(request, person_id):
    person = Employment.objects.get(id=person_id)
    return render(request, 'details.html', {'person': person})


@csrf_exempt
def details_update(request, person_id):
    person = Employment.objects.get(id=person_id)
    person.first_name = request.POST["first_name"]
    person.last_name = request.POST["last_name"]
    if request.POST["gender"]:
        person.gender = request.POST["gender"]
    person.national_id = request.POST["national_id"]
    person.picture = request.POST["picture"]
    person.save()
    return HttpResponseRedirect("/")
