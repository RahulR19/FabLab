from django import forms
from django.forms import ModelForm
from personal.models import Reserve
from personal.models import Cancel
from personal.models import Item
from django.core.validators import MinValueValidator, MaxValueValidator

class ReserveForm(ModelForm):
    class Meta:
        model = Reserve
        exclude = ['Instrument']

        def clean(self):
            super().clean()
            Rollno      = self.cleaned_data.get['Rollno']
            First       = self.cleaned_data.get['First']
            Last        = self.cleaned_data.get['Last']
            Email       = self.cleaned_data.get['Email']
            Phone       = self.cleaned_data.get['Phone']
            Date        = self.cleaned_data.get['Date']
            Fromtime    = self.cleaned_data.get['Fromtime']
            Totime      = self.cleaned_data.get['Totime']
            Pin         = self.cleaned_data.get['Pin']

class CancelForm(ModelForm):
    class Meta:
        model = Cancel
        fields = '__all__'

        def clean(self):
            super().clean()
            Rollno = self.cleaned_data.get['Rollno']
            Pin   = self.cleaned_data.get['Pin']

form = ReserveForm()
form2 = CancelForm()

"""class ReserveForm(forms.Form):
    Rollno   = forms.CharField()
    First    = forms.CharField()
    Last     = forms.CharField()
    Email    = forms.EmailField()
    Phone    = forms.CharField()
    Date     = forms.DateField(widget=forms.DateInput(format='%D:%M:%Y'))
    Fromtime = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    Totime   = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    Pin      = forms.IntegerField(validators=[MinValueValidator(1000),
                                       MaxValueValidator(9999)])

class Meta:
    model = Reserve()
    exclude = ('status',)

    def save(self):
        Reserve.Rollno = self.cleaned_data['Rollno']
        Reserve.First  = self.cleaned_data['First']
        Reserve.Last   = self.cleaned_data['Last']
        Reserve.Email  = self.cleaned_data['Email']
        Reserve.Phone  = self.cleaned_data['Phone']
        Reserve.Date   = self.cleaned_data['Date']
        Reserve.Fromtime   = self.cleaned_data['Fromtime']
        Reserve.Totime   = self.cleaned_data['Totime']
        Reserve.Pin   = self.cleaned_data['Pin']

        if commit:
            self.save()"""
