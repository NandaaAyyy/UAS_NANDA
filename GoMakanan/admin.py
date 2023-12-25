from django.contrib import admin
from .models import Pembeli

# Register your models here.

class MemberPembeli():
  list_display = ("NAMA", "NO_ANTREAN", "PESANAN",)
  
admin.site.register(Pembeli)
