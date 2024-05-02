from django.shortcuts import render


# Create your views here.
def home2(request):
    return render(request, 'app/home.html')
