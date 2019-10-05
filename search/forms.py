from django import forms
from haystack.forms import SearchForm


class BazaarSearchForm(SearchForm):

    def search(self):
        queryset = super(BazaarSearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()
        return queryset


class StockSearchForm(SearchForm):
    price = forms.FloatField(required=False)

    def search(self):
        queryset = super(StockSearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()
        if self.cleaned_data['price']:
            queryset = queryset.filter(price=self.cleaned_data['price'])
        return queryset

