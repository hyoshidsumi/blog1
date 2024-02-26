from django.shortcuts import render

# Create your views here.
def v2(req):
    return render(req, 'v2.html', {'a':'a2'})