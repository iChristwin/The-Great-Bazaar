from haystack import indexes
from .models import Item


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    locale = indexes.CharField(model_attr='owner__locale')
    last_seen = indexes.DateField(model_attr='owner__last_modified')
    date_added = indexes.DateField(model_attr='date_added')
    available = indexes.CharField(model_attr='available')

    def get_model(self):
        return Item

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(available='True')
