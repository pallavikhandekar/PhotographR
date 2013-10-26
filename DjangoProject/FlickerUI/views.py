# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
import csv
import os

def index(request):
    if request.method == 'POST':
        if 'searchAttribute' in request.POST:
            print request.POST['searchAttribute']
        fname = os.path.join(os.path.dirname(__file__), 'flickpics.csv')
        with open(fname, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            rows=[row for row in spamreader]
      #  return HttpResponse("Hello, world. You're at the poll index.")
        return render(request, 'index.html', {"rows": rows})


def search(request):
    return render(request,'SearchImage.html')

