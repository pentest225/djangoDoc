# djangoDoc
 Documentations Django partie Admin 
>Bonjour tous dans ce tutoriel, nous allons ensemble génère une partie administrations d'un projet Django
>### NB :
>suivre ce tutoriel signifie que vous avez déjà une bonne notion des notions en créations de projet  Django paramétrage du seing et aussi dans la création des models 

## Model du Projet 
>Pour notre tutoriel nous alons travallez aevc les models suivents 
```python
# dans le fichier model.py
from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField()
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
```
    
>Apres creatios de notre models on peux maintement faire notre migrations
```python 
 python3 manage.py makemigrations
 ```
 ```python 
 python3 manage.py migrate
 ```
 ![ alt text](https://github.com/pentest225/djangoDoc/blob/master/imagesReadme/welcomeDjango.png)
 Ok tout est bon 
 
 ## Creations de notre partie Admin 
 >ok notre environnement Django est fin prés nous pouvons passer au vif du sujet, la création de notre partie admin tent attendue 
 >Commençons par coller ce boute de code dans le fichier admin.py
 ```python 
from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display =('nom','description','date_add','date_upd')
 ```
 
 ![alt text](https://github.com/pentest225/djangoDoc/blob/master/imagesReadme/Capture%20d%E2%80%99%C3%A9cran%202019-11-28%20%C3%A0%2015.16.58.png)
 
 
