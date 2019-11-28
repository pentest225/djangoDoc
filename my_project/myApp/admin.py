from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display =('nom','description','image','date_add','date_upd')
