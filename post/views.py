from django.shortcuts import render

# Create your views here.

def list(request, category):
    context = {}
    return render(request, 'post/list.html', context)