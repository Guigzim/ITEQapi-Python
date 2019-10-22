from django.db import models
from firebirdsql import connect


def dbAcces(sql):
    con = connect(database='C:\\Users\\guilh\\Desktop\\DKSOFT.FDB', user='SYSDBA', password='masterkey', host='localhost')
    cursor = con.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

class AlunoS(models.Model):
    nome = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    cidade = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
    def __init__(self, args):
        self.id = args[0]
        self.nome = args[1]
        self.cidade = args[2]
        
    
    @staticmethod
    def getAlunos():
        result = dbAcces("SELECT ID_ALUNO,NOME,B.DESCRICAO AS CIDADE FROM ALUNOS AS A LEFT JOIN CIDADES AS B ON A.ID_CIDADE=B.ID_CIDADE WHERE A.TIPO = 'AL'")
        alunos = []
        for aluno in result:
            a = AlunoS(aluno)
            alunos.append(a)

        return alunos
