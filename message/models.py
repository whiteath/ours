#coding:utf-8
from django.db import models
from django.contrib import admin

class Messa(models.Model):
    msg = models.CharField(max_length=280)
    mtime = models.DateTimeField(auto_now_add = True)

class MessaAdmin(admin.ModelAdmin):
    list_display = ('msg','mtime')

admin.site.register(Messa,MessaAdmin)
