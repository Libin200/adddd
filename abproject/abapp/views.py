from django.shortcuts import render
from django.http import HttpResponse
from abapp.models import aaa
from abapp.form import aaaform
# Create your views here.
def hello(request):
    aa=aaaform()
    return render(request,"aa.html",{'aa':aa})
def home(request):
    if request.method=="POST":
        form=aaaform(request.POST)
        
        try:
            if form.is_valid():
                form.save()
                return render(request,"bb.html")
            else:
                a="please enter all details"
                return render(request,"aa.html",{'a':a})
        except:
            return render(request,"aa.html")
    return render(request,"aa.html")
def view(request):
        return render(request,"cc.html")

def next(request,id):
   
    try:

        aa=aaa.objects.all()
        return render(request,"bb.html",{'aa':aa})
    except:
        return HttpResponse("object doesn't available")
def cookies_count(request):
    count=request.COOKIES.get('count',0)
    totalCount = int(count) + 1
    response=render(request , 'cookiescount.html',{'count':totalCount})
    response.set_cookie('count', totalCount)
    return response
