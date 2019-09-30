from django.core.exceptions import ValidationError
from datetime import datetime, date

#classe para calcular idades a partir de datas
def calculate_age(born):
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


#valida os models
def valida0entre4(value):
    if value < 0 or value > 4:
        raise ValidationError(_('Invalid value: %s') % value)

