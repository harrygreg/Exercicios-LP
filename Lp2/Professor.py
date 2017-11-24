from Disciplina import Disciplina
from Pessoa import Pessoa
class Professor(object):
    def __init(self):
        
        self._apelido = None
        self._disciplina=None

    def getApelido(self):
        return self._apelido
    def setApelido(self,Apelido):
        self._apelido=Apelido
       
        
    def adiciona_disciplina(self,lista,lista2,Nome,Carga,):
        if Nome in lista:
            return False 
        else:
            lista.append(Nome)
            lista2.append(Carga)
            return True
    def deleta_disciplina(self,lista,lista2,Nome):
        
        if Nome in lista:
            x=lista.index(Nome)
            lista.pop(x)
            lista.pop(x+1)
            return True
        else:
            return False
    def total_carga_horaria(self,lista2):
        soma = sum(lista2)
        return soma






 


