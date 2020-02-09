# 1- Importation des models dans le fichier admin.py :
from . import models

# 2- Integrer Django admin interface :

from django.contrib import admin

#-------------------------------------- IMPORTATION DES MODELS ---------------------------------------------#
from . import models

#-------------------------------------- IMPORTATION DE MARK_SAFE ---------------------------------------------#
from django.utils.safestring import mark_safe


# Register your models here.

#-------------------------------------- CLASSE PERMETTANT D'AJOUTER LE MODEL COMMENTAIRE EN LIGNE dans la page detail de article ----------------------#

class ArticleInline(admin.TabularInline):
    model = models.Article
    extra = 0

#-------------------------------------- CREATION DU MODEL CATEGORIE DANS L'ADMIN ---------------------------------------------#

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display =('view_image', 'nom','date_add','date_upd')
    list_filter = ('status', 'date_add', 'date_upd')
    search_fields = ('nom',)
    ordering = ('nom',)
    list_per_page = 3

    date_hierarchy = 'date_add'

    fieldsets = [
    ('Titre et visibilité', {'fields': ['nom', 'status', ]}),
    ('Description et image', {'fields': ['image', 'description', ]}),
    ]
    
    actions = ('active', 'deactive')
    

    readonly_fields = ['detail_image']

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La selection a été activée avec succès")

    active.short_desription = "Activez les Categorys selectionnés"

    def deactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La selection a été désactivée avec succès")
        
    deactive.short_desription = "Désactivez les Categorys selectionnés"

    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px"/>'.format(url = obj.image.url))

    def detail_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px"/>'.format(url = obj.image.url))

    # AFFICHAGE DES MODELS EN LIGNE SOUS LE DETAIL DU MODEL DANS L'ADMIN #

    inlines = [ArticleInline]

#-------------------------------------- CREATION DU MODEL ARTICLE DANS L'ADMIN ---------------------------------------------#

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):

    # AFFICHAGE DES CHAMPS DU MODEL DANS L'ADMIN #

    list_display =('nom','view_image','date_add','date_upd')
    
    # FILTRAGE DU MODEL DANS L'ADMIN #

    list_filter = ('status', 'date_add', 'date_upd')
    
    #  CHAMPS DE RECHERCHE DU MODEL DANS L'ADMIN #
    search_fields = ('nom',)

    # ORDONNER DES CHAMPS DU MODEL DANS L'ADMIN #

    ordering = ('nom',)
    list_per_page = 3
    # ORDONNER DES CHAMPS DU MODEL EN FONCTION DE LA DATE DANS L'ADMIN #

    date_hierarchy = ('date_add')


    # AFFICHAGE DES CHAMPS DU MODEL COMME DES LIENS DANS L'ADMIN #
    
    list_display_links = ('view_image', 'nom',)

    #  STRUCTURER LES CHAMPS DU MODEL AVEC DES PANNELS DANS L'ADMIN #

    fieldsets = [
        ('les clés etrangeres', {'fields': ['categorie', 'tag', ]}),
        ('les champs specifiques', {'fields': ['image', 'description', ]}),
        ('les champs standards', {'fields': ['status',]}),
    ]

    # AFFICHAGE DES MODELS SOUS LA MEME FORME QUE LES GROUPES DANS L'ADMIN (utiliser pour les relations ManyToMany) #
    
    filter_horizontal = ('tag',)
    
    # MODIFIER LES SATATUTS DU MODEL DANS L'ADMIN #

    actions = ('active', 'deactive')
    
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La selection a été activée avec succès")

    active.short_desription = "Activez les Categorys selectionnés"

    def deactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La selection a été désactivée avec succès")
    deactive.short_desription = "Désactivez les Categorys selectionnés"
    
    # AFFICHAGE DE L'IMAGE DANS LE DEATAIL DU MODEL DANS L'ADMIN #
    readonly_fields = ['detail_image']

    # FONCTION PERMETTANT D'AFFICHER L'IMAGE DANS LA TABLE ET LE DETAIL DU MODEL #

    def view_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px"/>'.format(url = obj.image.url))

    def detail_image(self, obj):
        return mark_safe('<img src="{url}" width="100px" height="100px"/>'.format(url = obj.image.url))
    

#-------------------------------------- CREATION DU MODEL TAG DANS L'ADMIN ---------------------------------------------#


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_add', 'date_upd', 'status',)
    list_filter = ('date_add', 'date_upd', 'status',)
    search_fields = ('nom',)
    ordering = ('nom',)
    date_hierarchy = ('date_add')
    list_per_page = 2