from django.contrib import admin
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "pdf"

urlpatterns = [
    path('about/',views.about,name ="about" ),
    path('dashboard/',views.dashboard,name ="dashboard" ),
    path('pdf/<int:id>',views.detail,name ="detail" ),
    path('addPdf/',views.addPdf,name ="addPdf" ),
    path('update/<int:id>',views.updatePdf,name ="update" ),
    path('delete/<int:id>',views.deletePdf,name ="delete" ),
    #path('media/',views.readAlgorithm,name="reader")
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
