from django.shortcuts import render

# Create your views here.

def index(request):
    text_dict = {'text': 'Hasibur Rahman', 'age':'22'}
    return render(request, 'basicApp/index.html', text_dict)

def other(request):
    return render(request, 'basicApp/other.html')

def relative(request):
    return render(request, 'basicApp/relative_urlt.html')