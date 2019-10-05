from django.shortcuts import render, redirect

# Create your views here.
# My imports -----------------------------------------------------------------
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import UserReviewForm
from .models import UserRating
from .utils import create_review

from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def review_user(request, pk):
    form_class = UserReviewForm
    subject = get_user_model().objects.get(pk=pk)
    rating = UserRating.objects.get_or_create(subject=subject)
    create_review(request, form_class, subject, rating)


class ReviewDetails(DetailView):
    model = Review
    template_name = 'user_review/detail.html'
    context_object_name = 'review'


class EditReview(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = 'user_review/edit.html'
    fields = ('rating', 'comment', )
    context_object_name = 'Review'
    success_url = reverse_lazy('home')


class DeleteReview(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'user_review/delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'Review'


def user_details(request, pk):
    subject = get_user_model().objects.get(pk=pk)
    rating = UserRating.objects.get_or_create(subject=subject)
    return render(request, 'user/details.html', {'subject': subject,
                                                 })