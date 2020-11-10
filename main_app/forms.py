from django import forms
from django.forms.widgets import DateInput, TimeInput, TextInput
from .models import AutoBrand, AutoModels, TechnicalService, TestDriveModel, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import pendulum

class CarFilterForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=AutoBrand.objects.all(), label="Марка", required=False)
    model = forms.ModelChoiceField(queryset=AutoModels.objects.all(), label="Модель", required=False)
    min_price = forms.IntegerField(label="от", min_value=0, required=False)
    max_price = forms.IntegerField(label="до",  min_value=0,required=False)
    min_mileage = forms.IntegerField(label="от", min_value=0, required=False)
    max_mileage = forms.IntegerField(label="до", min_value=0, required=False)

class TechnicalServiceForm(forms.ModelForm):
    class Meta:
        model = TechnicalService
        fields = ('name', 'surname', 'patronymic', 'brand', 'model', 'data', 'time', 'phone_number', 'extra_info')
        widgets = {'data': DateInput(attrs={'type': 'date', 'min': pendulum.now().to_date_string(), 'max': pendulum.now().add(days=2).to_date_string()}),
                   'time': TimeInput(format='H:m', attrs={'type': 'time', 'min': '09:00', 'max': '20:00'}),
                   'phone_number': TextInput(attrs={'placeholder': '+7(___)-___-__-__'})
                   }

class TestDriveForm(forms.ModelForm):
    class Meta:
        model = TestDriveModel
        fields = ('name', 'surname', 'patronymic', 'brand', 'model', 'data', 'time', 'phone_number', 'extra_info')
        widgets = {'data': DateInput(attrs={'type': 'date', 'min': pendulum.now().to_date_string(), 'max': pendulum.now().add(days=2).to_date_string()}),
                 'time': TimeInput(format='H:m', attrs={'type': 'time', 'min': '09:00', 'max': '20:00'}),
                 'phone_number': TextInput(attrs={'placeholder': '+7(___)-___-__-__'})
                 }

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'full_name', 'phone', 'password1', 'password2')

