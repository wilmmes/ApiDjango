from django.db import models
from django.core.exceptions import ValidationError


# Validación personalizada para la especialidad
def validar_especialidad(especialidad):
    especialidades_validas = ['Peinadora', 'Peluquero', 'Barbero', 'Maquilladora']
    if especialidad not in especialidades_validas:
        raise ValidationError(f'{especialidad} no es una especialidad válida.')


def validar_telefono(valor):
    if not valor.isdigit() or len(valor) != 8:
        raise ValidationError("El número de Telefono debe tener exactamente 8 dígitos.")


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=8, validators=[validar_telefono])
 
    def __str__(self):
        return self.nombre


class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50, validators=[validar_especialidad])

    def __str__(self):
        return f'{self.nombre} - {self.especialidad}'

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='citas')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f'Cita de {self.cliente} con {self.profesional} el {self.fecha_hora}'


class HistorialAtencion(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE, related_name='historial')
    detalles = models.TextField()

    def __str__(self):
        return f'Historial de la cita {self.cita}'
