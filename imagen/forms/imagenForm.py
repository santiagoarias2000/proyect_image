from django import forms
from imagen.models import Document


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('imagen',)
