from django import forms
from .models import AddTransaction


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = AddTransaction
        fields = ['Title', 'Amount', 'Type', 'Category', 'Date']
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date'}),
            'Amount': forms.NumberInput(attrs={'min': 0}),
        }
