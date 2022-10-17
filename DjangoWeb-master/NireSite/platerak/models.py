from django.db import models

# Create your models here.
class Platera(models.Model):
    izena=models.CharField(max_length=50)
    ingredienteak=models.TextField()
    alergenoak=models.TextField()
    prezioa=models.FloatField()

    def __str__(self):
        return u'%s' % self.izena

    def getPrezioa(self):
        return self.prezioa

class Erosketa(models.Model):
    erabiltzailea=models.CharField(max_length=50)
    plateraIzena=models.ForeignKey(Platera, on_delete=models.CASCADE)
    komentarioak=models.TextField()
    kantitatea=models.IntegerField()

    def __str__(self):
        return u'%s' % self.erabiltzailea + "-en erosketa "

    def totala(self):
        return self.plateraIzena.prezioa * self.kantitatea