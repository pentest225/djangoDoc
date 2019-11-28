from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="Categorie/%Y/%m/%d/")
    date_add = models.DateTimeField( auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)
    status = models.BooleanField(default=False)
    
class Produit(models.Model):
    nom=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='Produit/')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='categorie_produit')
    date_add=models.DateTimeField(auto_now=True)
    date_upd=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)