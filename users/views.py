from django.shortcuts import render
from django.http import HttpResponse
from . forms import UpdateForm
# Create your views here.
def home(request):
    form = UpdateForm()
        
    template = 'index.html'

    return render(request, template, {'form':form})