from django.shortcuts import render
from django.http import HttpResponse
from .forms import DetailsForm
from django.contrib import messages as message
# Create your views here.
def home(request):
    form = DetailsForm()
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            form = DetailsForm()
    return render(request, 'index.html',{'form':form})