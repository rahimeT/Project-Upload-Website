from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Pdf(models.Model):
    name = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name="İsim")
    subject = models.CharField(max_length=50, verbose_name="Ödevin Konusu")
    content = RichTextField()
    date = models.DateTimeField(auto_now_add = True, verbose_name="Oluşturulma Tarihi")
    pdf_file = models.FileField(  verbose_name="Ödev Dosyası")
    def __str__(self):
        return self.subject

