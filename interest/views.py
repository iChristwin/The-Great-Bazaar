from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Offer, Bookmarks, Bargain, Order
from .forms import OfferForm, BargainForm, OrderForm

from items.models import Item
from store.models import Stock

# ===================================================================


def charge(bid):
    """This function calculates fees for trnxs."""
    rate = 3.33
    return bid * rate / 100


@login_required
def add_bookmark(request, pk):
    item = Item.objects.get(pk=pk)
    bookmarks, created = Bookmarks.objects.get_or_create(owner=request.user)
    bookmarks.bookmarked.add(item)
    bookmarks.save()
    return redirect(item.get_absolute_url())


@login_required
def remove_bookmark(request, pk):
    item = Item.objects.get(pk=pk)
    bookmarks, created = Bookmarks.objects.get_or_create(owner=request.user)
    bookmarks.bookmarked.remove(item)
    bookmarks.save()
    return redirect(item.get_absolute_url())


@login_required
def get_bookmarks(request):
    bookmarks, created = Bookmarks.objects.get_or_create(owner=request.user)
    return render(request, 'bookmarks/list.html', {'bookmarks': bookmarks})


class AddOffer(LoginRequiredMixin, CreateView):
    model = Offer
    form_class = OfferForm
    login_url = 'login'
    context_object_name = 'offer'
    template_name = 'interest/form.html'

    def form_valid(self, form):
        form.instance.item = Item.objects.get(pk=self.kwargs['pk'])
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Add'
        kwargs['interest'] = 'Offer'
        context = super(AddOffer, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        item = Item.objects.get(pk=self.kwargs['pk'])
        if item.owner == self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UpdateOffer(LoginRequiredMixin, UpdateView):
    model = Offer
    form_class = OfferForm
    login_url = 'login'
    context_object_name = 'offer'
    template_name = 'interest/form.html'

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Update'
        kwargs['interest'] = 'Offer'
        context = super(UpdateOffer, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        offer = self.get_object()
        if offer.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteOffer(LoginRequiredMixin, DeleteView):
    model = Offer
    login_url = 'login'
    template_name = 'interest/delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'offer'

    def dispatch(self, request, *args, **kwargs):
        offer = self.get_object()
        if offer.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class MyOffers(LoginRequiredMixin, ListView):
    model = Offer
    login_url = 'login'
    template_name = 'interest/list.html'
    context_object_name = 'offers'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(owner=self.request.user)
        return queryset


@login_required
def accept_offer(request, pk):
    offer = Offer.objects.get(pk=pk)
    if request.user == offer.item.owner:
        offer.accepted = True
        offer.item.available = False
        offer.item.booked_for = request.user
        offer.item.save()
        offer.save()
    return redirect(offer.item.get_absolute_url())


@login_required
def cancel_offer(request, pk):
    offer = Offer.objects.get(pk=pk)
    if request.user == offer.item.owner or offer.owner == request.user:
        offer.accepted = False
        offer.item.available = True
        offer.item.save()
        offer.save()
        if offer.bargaindeposit:
            offer.bargaindeposit.delete()
    return redirect(offer.item.get_absolute_url())


class MakeBargain(LoginRequiredMixin, CreateView):
    model = Bargain
    form_class = BargainForm
    login_url = 'login'
    context_object_name = 'bargain'
    template_name = 'interest/form.html'

    def form_valid(self, form):
        form.instance.offer = Offer.objects.get(pk=self.kwargs['pk'])
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Make'
        kwargs['interest'] = 'Bargain'
        context = super(MakeBargain, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        offer = Offer.objects.get(pk=self.kwargs['pk'])
        if offer.item.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UpdateBargain(LoginRequiredMixin, UpdateView):
    model = Bargain
    form_class = BargainForm
    login_url = 'login'
    context_object_name = 'bargain'
    template_name = 'interest/form.html'

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Update'
        kwargs['interest'] = 'Bargain'
        context = super(UpdateBargain, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        bargain = self.get_object()
        if bargain.seller != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteBargain(LoginRequiredMixin, DeleteView):
    model = Bargain
    login_url = 'login'
    template_name = 'interest/delete.html'
    context_object_name = 'bargain'

    def dispatch(self, request, *args, **kwargs):
        bargain = self.get_object()
        if bargain.seller != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@login_required
def accept_bargain(request, pk):
    offer = Offer.objects.get(pk=pk)
    if request.user == offer.owner:
        offer.offer = offer.bargain.bargain
        offer.save()
        offer.bargain.delete()
    return redirect(offer.item.get_absolute_url())


class AddOrder(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    login_url = 'login'
    context_object_name = 'order'
    template_name = 'interest/form.html'

    def form_valid(self, form):
        form.instance.stock = Stock.objects.get(pk=self.kwargs['pk'])
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Make'
        kwargs['interest'] = 'Order'
        context = super(AddOrder, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        stock = Stock.objects.get(pk=self.kwargs['pk'])
        if stock.store.owner == self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class UpdateOrder(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    login_url = 'login'
    context_object_name = 'order'
    template_name = 'interest/form.html'

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Update'
        kwargs['interest'] = 'Order'
        context = super(UpdateOrder, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if order.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteOrder(LoginRequiredMixin, DeleteView):
    model = Order
    login_url = 'login'
    template_name = 'interest/delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'order'

    def dispatch(self, request, *args, **kwargs):
        order = self.get_object()
        if order.owner == self.request.user or order.stock.store.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class MyOrders(LoginRequiredMixin, ListView):
    model = Order
    login_url = 'login'
    template_name = 'interest/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(owner=self.request.user)
        return queryset


@login_required
def accept_order(request, pk):
    order = Order.objects.get(pk=pk)
    if order.quantity < order.stock.quantity and order.accepted is False:
        if request.user == order.stock.store.owner:
            order.stock.quantity -= order.quantity
            order.accepted = True
            order.stock.save()
            order.save()
    return redirect(order.stock.get_absolute_url())



