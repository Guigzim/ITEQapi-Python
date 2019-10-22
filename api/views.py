from rest_framework import generics
from .models import AlunoS
from .serializers import AlunoSSerializer


# Create your views here.
class AlunosList(generics.ListCreateAPIView):
    queryset = AlunoS.getAlunos()
    serializer_class = AlunoSSerializer