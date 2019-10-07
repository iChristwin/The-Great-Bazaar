from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DeleteView
from django.views.generic import DetailView, UpdateView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from interest.models import Offer

from .models import Accounts
from .models import CollectDeposit, DisburseDeposit
from .forms import CollectForm, DisburseForm
from .utils import get_account


def choose_bank(request, pk, bank):
    return ''


class ConfirmDeposit(LoginRequiredMixin, UpdateView):
    model = CollectDeposit
    form_class = CollectForm
    template_name = 'payments/form.html'

    def get_queryset(self):
        contract = Offer.objects.get(pk=self.kwargs['pk'])
        queryset = super().get_queryset()
        return queryset.get(contract=contract)


@login_required
def confirm_deposit(request, pk):
    contract = Offer.objects.get(pk=pk)
    trnx = CollectDeposit.objects.get(contract=contract)
    form_class = CollectForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=trnx)
        if form.is_valid():
            trnx = form.save()
            return redirect(trnx.get_absolute_url())
    else:
        form = form_class(instance=trnx)
        return render(request, 'payments/form.html',
                      {'form': form, }
                      )


@login_required
def proceed_deposit(request, bank, pk):
    if bank == 'bank':
        return render(request, template_name='payments/banks.html', context={'pk': pk})
    contract = Offer.objects.get(pk=pk)
    trnx, status = CollectDeposit.objects.get_or_create(contract=contract,
                                                        owner=request.user,)
    trnx.bank = str(bank)
    trnx.amount = contract.offer
    trnx.save()
    acc = Accounts.objects.get(bank=str(bank))
    return render(request, 'payments/proceed.html',
                  {'acc': acc, }
                  )


@login_required
def cashout_proceed(request, pk):
    offer = Offer.objects.get(pk=pk)
    form_class = DisburseForm
    if request.method == 'POST' and offer.item.owner == request.user:
        cashout, created = DisburseDeposit.objects.get_or_create(owner=request.user,
                                                                 contract=offer)
        if cashout.editable is False:
            return redirect(offer.item.get_absolute_url())
        form = form_class(data=request.POST, instance=cashout)
        if form.is_valid():
            cashout = form.save()
            return redirect(offer.item.get_absolute_url())
    else:
        form = form_class()
        return render(request, 'payments/form.html',
                      {'form': form, }
                      )
