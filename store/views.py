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

from .forms import CloudinaryPhotoForm
from .models import CloudinaryPhotos

from interest.models import Order
from review.models import UserRating

from .models import Store, Stock
from .forms import StoreForm
from .forms import StockForm, StockUpdateForm

# ===================================================================


@login_required
def store_home(request):
    request.user.mode = 'store'
    request.user.save()
    return home(request)


class SetupStore(LoginRequiredMixin, CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'store/form.html'
    login_url = 'login'
    context_object_name = 'store'

    def get_success_url(self):
        return reverse_lazy('store:details', kwarg={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Setup'
        context = super(SetupStore, self).get_context_data(**kwargs)
        return context


class StoreDetails(DetailView):
    model = Store
    template_name = 'store/details.html'
    context_object_name = 'store'

    def get_context_data(self, **kwargs):
        """
        Add additional info to the profile page, including reviews,
        and user rating
        """
        store = self.get_object()
        kwargs['stocks'] = store.stock_set.all().order_by('-date_added')
        context = super(StoreDetails, self).get_context_data(**kwargs)
        return context


class UpdateStore(LoginRequiredMixin, UpdateView):
    model = Store
    form_class = StoreForm
    template_name = 'store/form.html'
    login_url = 'login'
    context_object_name = 'store'

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Update'
        context = super(UpdateStore, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        store = self.get_object()
        if store.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeleteStore(LoginRequiredMixin, DeleteView):
    model = Store
    template_name = 'store/delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    context_object_name = 'store'

    def dispatch(self, request, *args, **kwargs):
        store = self.get_object()
        if store.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# ===================================================================


class AddStock(LoginRequiredMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock/form.html'
    login_url = 'login'
    context_object_name = 'store'

    def post(self, request, *args, **kwargs):
        response = super(AddStock, self).post(request, *args, **kwargs)
        return response

    def form_valid(self, form):
        form.instance.store = self.request.user.store
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Add'
        context = super(AddStock, self).get_context_data(**kwargs)
        return context


class StockDetails(DetailView):
    model = Stock
    template_name = 'stock/details.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        """
        Add additional info to the profile page, including reviews,
        and user rating
        """
        stock = self.get_object()
        kwargs['photos'] = CloudinaryPhotos.objects.filter(stock=stock)
        if self.request.user == stock.store.owner:
            kwargs['orders'] = Order.objects.filter(stock=stock).order_by('-order_time')
        elif self.request.user.is_authenticated:
            kwargs['orders'] = Order.objects.filter(stock=stock,
                                                    owner=self.request.user,
                                                    ).order_by('-order_time')
        context = super(StockDetails, self).get_context_data(**kwargs)
        return context


class UpdateStock(LoginRequiredMixin, UpdateView):
    model = Stock
    form_class = StockUpdateForm
    template_name = 'stock/form.html'
    login_url = 'login'
    context_object_name = 'store'

    def get_context_data(self, **kwargs):
        kwargs['action'] = 'Update'
        context = super(UpdateStock, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        stock = self.get_object()
        if stock.store.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RemoveStock(LoginRequiredMixin, DeleteView):
    model = Stock
    template_name = 'stock/delete.html'
    success_url = reverse_lazy('store:store')
    login_url = 'login'
    context_object_name = 'store'

    def dispatch(self, request, *args, **kwargs):
        stock = self.get_object()
        if stock.store.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


# ===================================================================


def home(request):
    """This view decides what ur home view is, for starters, its intro"""
    return render(request, 'home.html')


def add_photo(request, pk):
    if request.method == "POST":
        form = CloudinaryPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.stock = Stock.objects.get(pk=pk)
            photo.save()
            return redirect('stock:details', pk)
    else:
        form = CloudinaryPhotoForm()
    return render(request, 'store/form.html', {'form': form})
