from django.core.exceptions import ValidationError

from .constants import ENLISTED


def is_mobile(entry):
    if entry[1:].isdigit() and entry.startswith('+') and len(entry) == 14:
        pass
    else:
        msg = u"Invalid entry, Make sure its a valid mobile NUMBER (starting with a country code)"
        raise ValidationError(msg)


def is_sluggy(entry):
    words = entry.split('-')
    for word in words:
        if word.isalpha():
            pass
        else:
            message = u"Just alphabets & hyphens (-) please!"
            raise ValidationError(message)


def is_enlisted(entry):
    if entry.lower() in ENLISTED:
        pass
    else:
        message = u"Seems %s has not been listed for enrollment" % entry
        raise ValidationError(message)
