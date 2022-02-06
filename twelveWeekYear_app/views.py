from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"test": "This is test"}
    return render(request, "twelveWeekYear_app/index.html", context)