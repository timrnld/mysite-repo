from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# defines a function called index that accepts a request and returns at HttpResponse.
def index(request):
    return render(request, 'cv/index.html')
