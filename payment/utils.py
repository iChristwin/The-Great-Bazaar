from .models import Accounts


def get_account(bank):
    acc = Accounts.objects.get(bank=str(bank))
    return acc.number
