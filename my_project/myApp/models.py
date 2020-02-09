from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="Categorie/%Y/%m/%d/")
    date_add = models.DateTimeField( auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom
            
    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

class Tag(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
        
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Article(models.Model):
    nom=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='article/')
    tag = models.ManyToManyField(Tag, related_name="tag_article")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='categorie_article')
    date_add=models.DateTimeField(auto_now=True)
    date_upd=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom
                
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"