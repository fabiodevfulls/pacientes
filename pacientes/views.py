from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse,Http404
from. models  import Pacientes,Tarefas,Consultas,Visualizacoes
from django.contrib import messages
from django.contrib.messages import constants




def pacientes(request):
    if request.method == "GET":
        pacientes=Pacientes.objects.all()
        print(pacientes)
        return render(request,'pacientes.html',{'queixas':Pacientes.queixa_choices,'pacientes':pacientes})
    elif request.method == "POST":
        nome= request.POST.get('nome')
        mail= request.POST.get('mail')
        telefone= request.POST.get('telefone')
        queixa= request.POST.get('queixa')
        foto= request.FILES.get('foto')

        if len(nome.strip())==0 or not foto:
            messages.add_message(request, constants.ERROR,'Preencha todos os campos')
            return redirect('pacientes')

        paciente=Pacientes(
         nome= nome,
         mail= mail,
         telefone= telefone,
         queixa= queixa,
         foto= foto
        )

        paciente.save()
        messages.add_message(request, constants.SUCCESS,'Cadastro realizado com sucesso')

        return redirect('pacientes')
        
        
def paciente_view(request,id):
    paciente = Pacientes.objects.get(id=id)
    if request.method == "GET":
        tarefas = Tarefas.objects.all()
        consultas = Consultas.objects.filter(paciente=paciente)
        consultas_list = [str(i.data) for i in consultas]  # Coletando datas das consultas
        humor_list = [i.humor for i in consultas]  # Coletando humor das consultas

        tuple_grafico= (consultas_list,humor_list)
        return render(request, 'paciente.html', {'paciente': paciente,'tarefas':tarefas, 'consultas':consultas,'tuple_grafico': tuple_grafico})
    elif request.method == "POST":
        humor=request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.FILES.get('video')
        tarefas = request.POST.getlist('tarefas')
        consultas = Consultas(
            humor=int(humor),
            registro_geral= registro_geral,
            video= video,
            paciente= paciente
        )
        consultas.save()
        for i  in tarefas:
            tarefa = Tarefas.objects.get(id=id)
            consultas.tarefas.add(tarefa)
            consultas.save()
            messages.add_message(request,constants.SUCCESS,'registro de consultas com sucesso')
            return redirect(f'/pacientes/{id}')

def atualizar_paciente(request,id):
    paciente = Pacientes.objects.get(id=id)
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    status = True if pagamento_em_dia == 'ativo' else False
    paciente.pagamento_em_dia = status
    paciente.save()
    return redirect(f'/pacientes/{id}')

def excluir_consulta(request, id):
    consulta = get_object_or_404(Consultas, id=id)
    consulta.delete()
    return redirect(f'/pacientes/{consulta.paciente.id}')

def consulta_publica(request, id):
    consulta = get_object_or_404(Consultas, id=id)

    print(consulta.link_publico)  # Apenas para debug

    # Se o paciente não tem pagamento em dia, retorna erro 404
    if not consulta.paciente.pagamento_em_dia:
        raise Http404()

    # Captura o IP do usuário e salva a visualização no banco de dados
    ip = request.META.get('REMOTE_ADDR', '0.0.0.0')  # Usa um IP padrão se não encontrar
    Visualizacoes.objects.create(consulta=consulta, ip=ip)  # Salva no BD

    return render(request, 'consulta_publica.html', {'consulta': consulta})