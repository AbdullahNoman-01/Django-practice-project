from django import forms

class contactForm(forms.Form):
   name = forms.CharField(label="User_Name")
   email =forms.EmailField(label="User_Email")
   age = forms.IntegerField(label="Age")
   weight = forms.FloatField()
   Balance= forms.DecimalField()
   Check = forms.BooleanField()
   Birthday = forms.DateField()