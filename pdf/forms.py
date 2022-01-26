from django import forms
from .models import Pdf

class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ["name","subject", "content","pdf_file"]   # bu alanlar gerekli demek istedik
     
  
