from django.contrib import admin
from .models import Pdf

# Register your models here.
#Admin Kısmında pdf kısmını tanımlamak için kullandık
@admin.register(Pdf)
class PdfAdmin(admin.ModelAdmin):

    list_display= ["subject","name","subject","date"]
    list_display_links=["subject","date"]
    search_fields=["subject"]
    list_filter = ["date"]
    class Meta:
        model=Pdf



