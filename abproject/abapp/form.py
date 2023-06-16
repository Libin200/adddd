from django import forms
from abapp.models import aaa
class aaaform(forms.ModelForm):
    class Meta:
        model=aaa
        fields="__all__"