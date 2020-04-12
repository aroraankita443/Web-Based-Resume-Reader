from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UserForm
from .models import User

# Create your views here.
def hi(request):
    form = UserForm()
    return render(request, 'form.html',{'form' : form})


def result(request):
    with open('DEMOAPP/file.csv','r') as file:
        f = file.read()
    return render(request, 'result.html', { 'file' : f})