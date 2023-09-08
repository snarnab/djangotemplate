from django.shortcuts import HttpResponse, render

def htmltemplate(req):
    return render(req, "index.html")

