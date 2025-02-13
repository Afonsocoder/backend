from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    telefone = models.CharField(max_length=9, blank=True, null=True)
    bairro = models.CharField(max_length=255) # Exemplo: "Hoji Ya Henda", "Tala Hady"
    data_diagnostico = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome