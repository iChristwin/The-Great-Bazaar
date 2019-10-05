from django.shortcuts import render, redirect

# Create your views here.

from django.conf import settings
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserForm, ProfileForm

from review.models import UserRating, UserReview

REGISTRATION_OPEN = getattr(settings, 'REGISTRATION_OPEN', True)


class RegistrationClosed(TemplateView):
    template_name = 'registration/registration_closed.html'


class JoinCommunity(TemplateView):
    template_name = 'user/community.html'


class SignUpView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'registration/registration_form.html'

    def form_valid(self, form):
        return super(SignUpView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if REGISTRATION_OPEN:
            response = super(SignUpView, self).get(request, *args, **kwargs)
            return response
        else:
            return redirect('closed')

    def post(self, request, *args, **kwargs):
        response = super(SignUpView, self).post(request, *args, **kwargs)
        form = self.get_form()
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            rating = UserRating(subject=user)
            rating.save()
            user.locale = kwargs['locale']
            user.save()
            login(self.request, user)
            return redirect('user:update', pk=user.pk)
        else:
            return response


class ProfileDetails(DetailView):
    model = User
    template_name = 'user/details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        """
        Add additional info to the profile page, including reviews,
        and user rating
        """
        user = self.get_object()
        kwargs['reviews'] = UserReview.objects.filter(subject=user)
        context = super(ProfileDetails, self).get_context_data(**kwargs)
        return context


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'user/form.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    context_object_name = 'profile'

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteAccount(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    login_url = 'login'
    context_object_name = 'profile'

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
