from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def hello_world(request):
    return render(request, 'AI/base.html')

def message(request):
    return render(request, 'AI/message.html')

def signup_view(request):
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)