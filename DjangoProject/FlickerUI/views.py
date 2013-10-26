# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render
import csv
import os

def index(request):

    fname = os.path.join(os.path.dirname(__file__), 'flickpics.csv')
    with open(fname, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows=[row for row in spamreader]
  #  return HttpResponse("Hello, world. You're at the poll index.")
    return  render(request, 'index.html', {"rows": rows})


def search(request):
    return render(request,'SearchImage.html')