from django.contrib import admin
from .models import PembeliGo_Makanan

# Register your models here.

class MemberPembeli():
  list_display = ("NO_ANTREAN","NAMA","PESANAN", "Jumlah_Makanan", "Jumlah_Minuman")
  
admin.site.register(PembeliGo_Makanan)

