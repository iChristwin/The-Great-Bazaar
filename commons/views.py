from django.shortcuts import render, redirect
# from interest.models import Interest


def home(request):
    if request.user.is_authenticated:
        return redirect('%s:home' % request.user.view)
    else:
        return redirect('welcome')
