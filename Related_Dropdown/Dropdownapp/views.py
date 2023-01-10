from django.shortcuts import render
from .forms import Userform
# Create your views here.


def index(request):
    if request.method=='POST':
        user=Userform(request.POST)
        if user.is_valid():
            user.save()
    return render(request,'index.html')