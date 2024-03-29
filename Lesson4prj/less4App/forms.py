from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets={

                'dob' : forms.DateInput(attrs={'class': 'datepicker1 form-control'}),
                'name' :forms.TextInput(attrs={'class': 'form-control'}),
                'email':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email Address'}),
                'slary':forms.TextInput(attrs={'class': 'form-control'}),

        }


class ContactForm(forms.Form):
        to =forms.EmailField(required=True, widget = forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Email Address'}))
        subject =forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control col-sm-4', 'placeholder':'subject'}))
        message =forms.CharField(required=True, widget = forms.Textarea(attrs={'class':'form-control col-sm-4','placeholder':'Message'}),label=(''))
