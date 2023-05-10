from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'AI/base.html')

def message(request):
    return render(request, 'AI/message.html')