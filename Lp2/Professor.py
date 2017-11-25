from Disciplina import Disciplina
from Pessoa import Pessoa

class Professor(object):
    
    def __init__(self):
        self._apelido = None
        self._disciplina = None

    def getApelido(self):
        return self._apelido
    
    def setApelido(self, apelido):
        self._apelido = apelido
       
    def adiciona_disciplina(self, lista, lista2, nome, carga,):
        if nome in lista:
            return False 
        else:
            lista.append(nome)
            lista2.append(carga)
            return True
        
    def deleta_disciplina(self, lista, lista2, nome):
        
        if nome in lista:
            x = lista.index(nome)
            lista.pop(x)
            lista.pop(x+1)
            return True
        else:
            return False
        
    def total_carga_horaria(self, lista2):
        soma = sum(lista2)
        return soma






 


