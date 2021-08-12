from django.shortcuts import get_object_or_404, render
from .models import Curso, Faculdade

def index (request):
    return render(request, 'index.html')

#passo 2 criar função
def course_list(request):
    faculdades= Faculdade.objects.all

    dados = {
        'faculdades' :faculdades
    }

    return render(request, 'course_list.html',dados)

def details(request,faculdade_id):
    cursos = Curso.objects.all
    faculdades = Faculdade.objects.all
    detalhes = get_object_or_404(Faculdade, pk = faculdade_id)

    faculdade_a_exibir ={
        'faculdade' : detalhes,
        'cursos' :cursos,
        'faculdades': faculdades
    }



    return render(request, 'details.html',faculdade_a_exibir)

def support(request):
    return render(request, 'support.html')
