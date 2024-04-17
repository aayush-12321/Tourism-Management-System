from django import forms

class TravelDateForm(forms.Form):
    traveldate = forms.DateField()

class ContactForm(forms.Form):
    address = forms.CharField()
    phone = forms.CharField()
