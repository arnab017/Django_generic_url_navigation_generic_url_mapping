from django.shortcuts import render

# Create your views here.

def contacts(request):
    return render(request,'contacts.html')

def abouts(request):
    return render(request,'abouts.html')