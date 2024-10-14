from django.db import models
from django.utils import timezone

# Create your models here.

class Medikua(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    lanpostua = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} -- {self.izena} -- {self.abizena} -- {self.lanpostua}"
    

class Pazientea(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    historiala = models.CharField(max_length=10000)


    def __str__(self):
        return f"{self.id} -- {self.izena} -- {self.abizena} -- {self.historiala}"

class Zita(models.Model):
    id = models.AutoField(primary_key= True)
    data = models.DateTimeField(default=timezone.now)
    paziente_kodea = models.ForeignKey(Pazientea, on_delete=models.CASCADE)
    mediku_kodea = models.ForeignKey(Medikua, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.paziente_kodea.izena} -- {self.data} -- {self.mediku_kodea.izena}"
