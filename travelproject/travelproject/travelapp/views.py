from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Teams
# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Teams.objects.all()


    return render(request,"index.html",{'result':obj, 'result1':obj1})

#def about(request):
    #return render(request,"result.html")

#def contact(request):
   # return HttpResponse("My Contact is 9894575658")

#def addition(request):
