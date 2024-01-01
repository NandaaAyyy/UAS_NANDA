from django.db import models

class PembeliGo_Makanan(models.Model):
  NO_ANTREAN = models.IntegerField(null=True)
  Nama = models.CharField(max_length=255)
  PESANAN = models.TextField(max_length=255)
  Jumlah_Makanan=models.IntegerField(null=True)
  Jumlah_Minuman=models.IntegerField(null=True)

  def __str__(self):
    return f"{self.Nama}"

  
  