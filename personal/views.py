from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content' : ['If wanna see ma dick, send request at','judajocu14@hotmail.com']})