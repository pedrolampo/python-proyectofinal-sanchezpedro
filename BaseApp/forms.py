from django import forms

class GuitarForm(forms.Form):
  name = forms.CharField(max_length=50)
  price = forms.IntegerField()

class BassForm(forms.Form):
  name = forms.CharField(max_length=50)
  price = forms.IntegerField()

class ClientForm(forms.Form):
  name = forms.CharField(max_length=50)
  surname = forms.CharField(max_length=50)
  email = forms.EmailField()