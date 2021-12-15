from django.http import HttpResponse
from django.shortcuts import render
def welcome(request):
    return HttpResponse("hello world")

def hello(request):
    return HttpResponse("""<html>
                        <head><title>home</title></head>
                        <body>
                        <h1>this is home page </h1>
                        </body>
                        </html>""")
    
def sample(request):
    fp = open(r"C:\Users\GODAVARTHIVENUGOPAL\Desktop\django6.30\project3\pro3\sample.html",'rb')
    res=fp.read()
    fp.close()
    return HttpResponse(res)

def home(request):
    return render(request,'home.html')