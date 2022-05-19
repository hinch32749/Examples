import datetime
import ipywidgets as widgets
from django import forms

# MONTHS = [(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'),
#           (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]

DAYS = [(i, str(i)) for i in range(1, 32)]
TIME = [(i, datetime.datetime(2022, 1, 11, i+7, 0).strftime("%H:00")) for i in range(1, 10) if i+7 != 12]
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
            'October', 'November', 'December']


class GetDateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone_number = forms.CharField(label='Phone number',
                                   widget=forms.TextInput(attrs={'type': 'tel',
                                                                 'placeholder': '+375 (__) _ _ _-_ _-_ _',
                                                                 'value': '+375'}))
    month_choice = forms.TypedChoiceField(label='Month', choices=MONTHS, empty_value='Choice month')
    day_choice = forms.TypedChoiceField(label='Day', choices=DAYS, empty_value='Choice day')
    time_choice = forms.TypedChoiceField(label='Time', choices=TIME, empty_value='Choice time')
