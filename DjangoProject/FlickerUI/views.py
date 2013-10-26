# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
import csv
import os

def index(request):
    print "CLLED ME"
    if request.method == 'POST':
        fname = os.path.join(os.path.dirname(__file__), 'flickpics.csv')
        with open(fname, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            rows=[row for row in spamreader]
      #  return HttpResponse("Hello, world. You're at the poll index.")
        return  render_to_response(request, 'index.html', {"rows": rows})


def search(request):
    return render(request,'SearchImage.html')

def search_form(request):
    if 'searchAttribute' in request.GET:
        message = 'You searched for: %r' % request.GET['searchAttribute']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)