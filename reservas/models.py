from django.db import models

# Modelo Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre

# Modelo Profesional del Servicio
class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Modelo Cita
class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    servicio = models.CharField(max_length=100)  # Corte de cabello, Tinte, etc.

    def __str__(self):
        return f"Cita para {self.cliente.nombre} con {self.profesional.nombre} el {self.fecha}"

# Modelo Historial de Atención
class HistorialAtencion(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    servicio_realizado = models.CharField(max_length=100)
    comentarios = models.TextField()

    def __str__(self):
        return f"Historial de atención para {self.cita.cliente.nombre} - {self.servicio_realizado}"
