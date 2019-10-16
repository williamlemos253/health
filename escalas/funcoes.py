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
        raise forms.ValidationError(_('Valor inválido: %s') % value)




#permite o login por email
class EmailAuthentication(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return None


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(' Já existe um usuário com esse email')    
        return email

