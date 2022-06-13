from todo.apps import TodoConfig
from todo.models import DatabaseTeste
from todo.models import soma_valores, vendidos_mes
from rest_framework import serializers

# serializer todos dados
class DataBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseTeste
        fields = ['id_loja','tipo_compra','contagem_clientes_mes','total_vendas','mes_referencia']
# soma de  vendas
class SomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = soma_valores
        fields = ['total_clientes','vendas_totais','ticket']
# para dados por mes, e dados por modelo
class MesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendidos_mes
        fields = ['meses','valores','categoria']

