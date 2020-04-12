from django import forms
import PyPDF2

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'document')









