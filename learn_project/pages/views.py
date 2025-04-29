from django.shortcuts import render

def data_page(request):
    return render(request, 'pages/data.html')

def test_page(request):
    return render(request, 'pages/test.html')

def home(request):
    return render(request, 'pages/home.html')
