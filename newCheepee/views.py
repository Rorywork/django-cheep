from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Cheepees

# Create your views here.

def get_newCheepee(request):
    
    #return render(request, "newCheepee.html",{'surveys': results})
    results = Cheepees.objects.all()
    #results = Cheepees.objects.filter(Owner = request.user.username)
    return render(request,"newCheepee.html",{'Cheepeess': results})
