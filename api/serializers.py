from rest_framework import serializers
from .models import AlunoS



class AlunoSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoS
        fields = '__all__'
