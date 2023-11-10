from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',  { 'title': 'Home' })

def cusomter_page(request):
    return render(request, 'home.html', { 'title': 'Customer' })

def courier_page(request):
    return render(request, 'home.html', { 'title': 'Courier' })