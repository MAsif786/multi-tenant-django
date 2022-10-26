from django.shortcuts import render

# Create your views here.

def home(request):
    tenant = request.META['HTTP_HOST'].split('.')[0]
    return render(request, 'home.html', {'tenant': tenant})
