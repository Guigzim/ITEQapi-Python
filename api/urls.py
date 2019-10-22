from django.urls import path
from .views import *

urlpatterns = [
    path('list_alunos/', AlunosList.as_view(), name='list_alunos'),
]