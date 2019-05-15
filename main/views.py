from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name='main/home.html')
    # context={"Tutorials":})


def register(request):
    form = UserCreationForm()
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})

