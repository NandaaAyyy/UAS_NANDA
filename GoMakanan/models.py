from django.db import models

class Pembeli(models.Model):
  Nama = models.CharField(max_length=255)
  NO_ANTREAN = models.IntegerField(null=True)
  PESANAN = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.Nama}"
  
  