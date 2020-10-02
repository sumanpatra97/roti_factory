from django.contrib import admin

from rotinew.models import rotii, login

class roti(admin.ModelAdmin):
    list_display = ['user','value']

class loginn(admin.ModelAdmin):
    list_display = ['first_name','last_name']

admin.site.register(login,loginn)

admin.site.register(rotii,roti)