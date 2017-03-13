from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<p>In index view</p>")

def item_detail(request, id):
    return HttpResponse("<p>In item detail view with id {0}</p>".format(id))