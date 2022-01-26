import abc
from django.core.files.storage import FileSystemStorage
from django.forms.widgets import Media
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, HttpResponse ,redirect , get_object_or_404

from .forms import PdfForm
from .models import Pdf
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import aspose.words as aw
import docx2txt
from pdfReader import pdfOkuma
# Url gelince görüntülenecek siteleri burada belirle
def index(request):

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


@login_required(login_url = "user:login")
def dashboard(request):
    pdfs = Pdf.objects.filter(name = request.user)
    context ={
        "pdfs":pdfs
    }
    return render(request,"dashboard.html",context)


@login_required(login_url = "user:login")
def addPdf(request):
    form = PdfForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        pdf = form.save(commit=False)
        pdf.author = request.user
        pdf.save()
        messages.success(request,"Ödev başarıyla yüklendi...")
        return redirect("pdf:dashboard")
    return render(request,"addPdf.html",{"form":form})




def detail(request,id):
    pdf = get_object_or_404(Pdf, id = id)

    pdfOkuma.readAlgorithm(pdf.pdf_file)      #PDF AYRIŞTIRMA

    return render(request, "detail.html",{"pdf": pdf})
    




@login_required(login_url = "user:login")
def updatePdf(request,id):
    pdf = get_object_or_404(Pdf , id =id)
    form = PdfForm(request.POST or None, request.FILES or None, instance= pdf)
    if form.is_valid():
        pdf = form.save(commit=False)
        pdf.author = request.user
        pdf.save()
       
        messages.success(request, "Ödev başarıyla güncellendi")
        return redirect("pdf:dashboard")
    
    return render(request , "update.html",{"form": form})



# silmek için gerekli olan geri bildirim kısmı
@login_required(login_url = "user:login")
def deletePdf(request,id):
    pdf = get_object_or_404(Pdf , id = id)
    pdf.delete()
    messages.success(request, "Ödev Başarıyla Silindi")

    return redirect("pdf:dashboard")


