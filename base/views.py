from django.shortcuts import render
from .models import *

notes = Note.objects.all()


def home_view(request):
    context = {"notes": notes}
    return render(request, "pages/home.html", context)
