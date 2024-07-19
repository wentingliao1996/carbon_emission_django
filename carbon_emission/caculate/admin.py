from django.contrib import admin
from .models import TestDB

# Register your models here.
class TestDBAdmin(admin.ModelAdmin):   
    list_display=('id','name','distance','teu','carbon')
    list_filter=('name','distance')
    search_fields=('name',)
    ordering=('id',)
 
admin.site.register(TestDB,TestDBAdmin)