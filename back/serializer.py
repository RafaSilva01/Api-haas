from rest_framework import serializers


from .models import ItemConfiguracao

class ItemConfiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemConfiguracao
        fields = '__all__'
        