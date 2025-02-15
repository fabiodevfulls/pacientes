from django.db import models
from django.urls import reverse

class Pacientes(models.Model):
    queixa_choices = (
        ('TDAH', 'TDAH'),
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
        ('TAG', 'Transtorno de Ansiedade Generalizada')
    )

    nome = models.CharField(max_length=255)
    mail = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos')
    pagamento_em_dia = models.BooleanField(default=True)
    queixa = models.CharField(max_length=4, choices=queixa_choices, default='TDAH')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pacientes"


class Tarefas(models.Model):
    frequencia_choices = (
        ('D', 'Diário'),
        ('1S', '1 vez por semana'),
        ('2S', '2 vezes por semana'),
        ('3S', '3 vezes por semana'),
        ('N', 'Ao necessitar')
    )

    tarefa = models.CharField(max_length=255)
    instrucoes = models.TextField()
    frequencia = models.CharField(max_length=2, choices=frequencia_choices, default='D')

    def __str__(self):
        return self.tarefa

    class Meta:
        verbose_name_plural = "Tarefas"


class Consultas(models.Model):
    humor = models.PositiveIntegerField()
    registro_geral = models.TextField()
    video = models.FileField(upload_to="video")
    tarefas = models.ManyToManyField(Tarefas)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data.strftime('%d/%m/%Y %H:%M')}"

    @property
    def link_publico(self):
        return f"http://127.0.0.1:8000{reverse('consulta_publica', kwargs={'id': self.id})}"

    @property
    def views(self):
        views = Visualizacoes.objects.filter(consulta=self)
        totais = views.count()
        unicas = views.values('ip').distinct().count()
        return f'{totais} - {unicas}'

    class Meta:
        verbose_name_plural = "Consultas"


class Visualizacoes(models.Model):
    consulta = models.ForeignKey(Consultas, on_delete=models.CASCADE, related_name="visualizacoes")
    ip = models.GenericIPAddressField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visualização em {self.data_hora.strftime('%d/%m/%Y %H:%M')} do IP {self.ip}"

    class Meta:
        verbose_name_plural = "Visualizações"
