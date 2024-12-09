from django.contrib import admin
from .models import Cliente, Profesional, Cita, HistorialAtencion

admin.site.register(Cliente)
admin.site.register(Profesional)
admin.site.register(Cita)
admin.site.register(HistorialAtencion)
