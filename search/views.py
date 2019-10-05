from haystack.generic_views import SearchView
from haystack.forms import SearchForm


from items.models import Item


class BazaarSearch(SearchView):
    template_name = 'welcome.html'
    form_class = SearchForm

    def get_queryset(self):
        queryset = super(BazaarSearch, self).get_queryset()
        queryset = queryset.models(Item, )
        return queryset.order_by("-last_seen")


class ItemSearch(SearchView):
    form_class = SearchForm
    classification = 'item'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.models(Item)
        if self.request.user.is_authenticated:
            queryset = queryset.filter(locale=self.request.user.locale)
        return queryset.order_by("-last_seen")
