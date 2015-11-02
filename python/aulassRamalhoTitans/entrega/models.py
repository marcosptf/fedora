# coding: utf-8
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    fone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64, blank=True)
    logradouro = models.CharField(max_length=128, blank=True)
    numero = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.nome, self.fone)
    
# XXX: mover para o admin.py

from django.contrib import admin
admin.site.register(Cliente)
