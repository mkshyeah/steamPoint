from django.contrib import admin
from .models import Category,Saunas,SaunasImage
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


class SaunasImageInline(admin.TabularInline):
  model = SaunasImage
  extra = 6

@admin.register(Saunas)
class SaunasAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price_per_hour',
                    'available','created','updated',
                    'discount']
    list_filter = ['available','created','updated']
    list_editable = ['price_per_hour','available','discount']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SaunasImageInline]