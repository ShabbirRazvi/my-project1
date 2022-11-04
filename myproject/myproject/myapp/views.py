from django.shortcuts import render
from .forms import Register_form
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User Registered Successfully")
        else:
            return HttpResponse("User is not Registered!")
    else:
        form = Register_form()
        return render(request, 'register.html', {'form': form})


@login_required(login_url='/login/')
def homepage_view(request):
    return render(request, 'homepage.html')
