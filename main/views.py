from django.shortcuts import render

def coming_soon(request):
    return render(request, 'main/coming_soon.html')