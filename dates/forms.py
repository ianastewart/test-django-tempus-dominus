from django.forms import *
from django.forms import widgets
from .models import DateTest
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

dateOptions ={'minDate': '2018-01-01',
              'maxDate': '2040-01-01',
              'format': 'DD/MM/YYYY'}

class DateForm(ModelForm):
    class Meta:

        model = DateTest
        fields = ('date', 'time', 'datetime', 'comment')

        widgets = {'date':DatePicker(options=dateOptions),
                   'time': TimePicker(),
                   'datetime': DateTimePicker(),
                   }
