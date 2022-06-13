from django.db import models
from django.http import response
from rest_framework import serializers
from rest_framework.decorators import api_view
from todo.models import DatabaseTeste
from todo.serializers import DataBaseSerializer
from todo.serializers import SomaSerializer, MesSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def database_list(request):
    base = DatabaseTeste.objects.all()
    serializer = DataBaseSerializer(base, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def database_view(request, pk):
    try:
        base = DatabaseTeste.objects.get(pk=pk)
    except DatabaseTeste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DataBaseSerializer(base)
    return Response(serializer.data)

@api_view(['GET'])
def database_total(request):
    base = DatabaseTeste.objects.all()
    clientes = 0
    vendas = 0
    ticket = 0
    for b in base:
        clientes += int(b.contagem_clientes_mes)
        vendas += int(b.total_vendas)
    ticket = int(vendas/clientes)
    ba = {
        'total_clientes': clientes,
        'vendas_totais': vendas,
        'ticket': ticket,
    }
    serializer = SomaSerializer(ba)
    return Response(serializer.data)

@api_view(['GET'])
def database_mes(request):
    base = DatabaseTeste.objects.all()
    meses =[]
    valores = [0,0,0,0,0,0,0,0,0,0,0,0]
    vendas = 0
    ticket = 0
    for b in base:
        meses.append(b.mes_referencia)
        if(b.mes_referencia == '01/12/2021'):
            break
    for b in base:
        valores[int(b.mes_referencia[3:5])-1] += int(b.total_vendas)
    for v in valores:
        v = str(v)
    ba = {
        'meses': meses,
        'valores':valores
    }
    serializer = MesSerializer(ba,)
    return Response(serializer.data)

def database_tipo(request):
    base = DatabaseTeste.objects.all()
    meses =[]
    presencial = [0,0,0,0,0,0,0,0,0,0,0,0]
    online = [0,0,0,0,0,0,0,0,0,0,0,0]
    vendas = 0
    ticket = 0
    for b in base:
        meses.append(b.mes_referencia)
        if(b.mes_referencia == '01/12/2021'):
            break
    for b in base:
        if(b.mes_referencia == 'Online'):
            
        valores[int(b.mes_referencia[3:5])-1] += int(b.total_vendas)
    for v in valores:
        v = str(v)
    ba = {
        'meses': meses,
        'valores':valores
    }
    serializer = MesSerializer(ba,)
    return Response(serializer.data)

