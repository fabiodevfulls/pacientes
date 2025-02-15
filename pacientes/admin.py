from django.contrib import admin
from .models import Pacientes, Tarefas, Consultas, Visualizacoes

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mail', 'telefone', 'pagamento_em_dia', 'queixa')  # Colunas visíveis na lista
    list_filter = ('pagamento_em_dia', 'queixa')  # Filtros laterais
    search_fields = ('nome', 'mail', 'telefone')  # Campo de pesquisa
    list_editable = ('pagamento_em_dia',)  # Permite edição direta na lista
    ordering = ('nome',)  # Ordenação alfabética

# Se preferir, pode usar admin.site.register(Pacientes, PacientesAdmin) em vez do decorator @admin.register
admin.site.register(Tarefas)
admin.site.register(Consultas)
admin.site.register(Visualizacoes)
