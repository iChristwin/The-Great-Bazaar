from django import forms

from .models import CollectDeposit, DisburseDeposit


class CollectForm(forms.ModelForm):
    class Meta:
        model = CollectDeposit
        fields = ('acc_name', 'acc_number', 'date', 'trnx_id')
        labels = {'acc_name': 'Account name',
                  'acc_number': 'Account number',
                  'date': 'Date of deposit',
                  'trnx_id': 'Transaction ID',
                  }


# =============================================================================


class DisburseForm(forms.ModelForm):
    class Meta:
        model = DisburseDeposit
        fields = ('bank', 'acc_name', 'acc_number', )
        labels = {'acc_name': 'Account name',
                  'acc_number': 'Account number',
                  }
