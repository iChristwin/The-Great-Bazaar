from django.shortcuts import render, redirect, reverse

# Create your views here.
# My imports -----------------------------------------------------------------
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, DetailView
from django.views.generic import UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from interest.models import Offer
from review.models import UserRating

from .models import Item
from .forms import ItemForm, ItemUpdateForm

# ===================================================================


@login_required
def item_home(request):
    request.user.mode = 'item'
    request.user.save()
    return home(request)


class AddItem(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/form.html'
    login_url = 'login'
    context_object_name = 'item'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Add'
        context = super(AddItem, self).get_context_data(**kwargs)
        return context


class ItemDetails(DetailView):
    model = Item
    template_name = 'items/details.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        """
        Add additional info to the profile page, including reviews,
        and user rating
        """
        item = self.get_object()
        if self.request.user == item.owner:
            kwargs['offers'] = Offer.objects.filter(item=item).order_by('-offer')
        elif self.request.user.is_authenticated:
            kwargs['offers'] = Offer.objects.filter(item=item,
                                                    owner=self.request.user,
                                                    ).order_by('-offer')
        context = super(ItemDetails, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        if item.available is False:
            return redirect('item:reserved', self.kwargs['pk'])
        else:
            return super().dispatch(request, *args, **kwargs)


class ItemReserved(DetailView):
    model = Item
    template_name = 'items/reserved.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        """
        Add additional info to the profile page, including reviews,
        and user rating
        """
        item = self.get_object()
        kwargs['offer'] = Offer.objects.get(item=item, accepted=True)
        context = super(ItemReserved, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        if item.available is False:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('item:details', self.kwargs['pk'])


class EditItem(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemUpdateForm
    template_name = 'items/form.html'
    login_url = 'login'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Edit'
        context = super(EditItem, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        if item.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RemoveItem(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'items/delete.html'
    success_url = reverse_lazy('item:inventory')
    login_url = 'login'
    context_object_name = 'item'

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        if item.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ItemInventory(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'items/inventory.html'
    login_url = 'login'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user).order_by('-date_added')


# ===================================================================


def home(request):
    """This view decides what ur home view is, for starters, its intro"""
    return render(request, 'home.html')


class ListItems(ListView):
    model = Item
    template_name = 'items/all.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(available=True).order_by('-date_added')
