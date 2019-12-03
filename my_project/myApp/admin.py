from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display =('nom','description','date_add','date_upd')
    list_filter = ('status', 'date_add', 'date_upd')
    ordering = ('nom',)
    list_per_page = 3

    date_hierarchy = 'date_add'


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
@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    fields = (('nom','image'), 'date_add','date_upd')
    list_display =('nom','description','date_add','date_upd')
    list_filter = ('status', 'date_add', 'date_upd')
    ordering = ('nom',)
    search_fields = ('nom',)
    list_per_page = 3

    date_hierarchy = 'date_add'


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