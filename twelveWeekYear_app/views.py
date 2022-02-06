from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    # goals = Goals.objects.all()
    context = {"test": "This is test"}
    return render(request, "twelveWeekYear_app/index.html", context)