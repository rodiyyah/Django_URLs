from urllib import request
from django.shortcuts import render

# Create your views here.
def home_view(requesst):
    return render(
        request,
        "home.html"
    )
