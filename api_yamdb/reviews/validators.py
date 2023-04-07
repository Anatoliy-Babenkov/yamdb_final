import datetime as dt

from django.core.exceptions import ValidationError


def year_validator(year):
    if year > dt.datetime.now().year:
        raise ValidationError('Год ещё не наступил!')
