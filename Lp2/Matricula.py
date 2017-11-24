
import datetime,time

class Matricula(object):
    def __inti__(self):
        self._aluno = None
        self.disciplina = None
        self._data_matricula = None
        self._data_confirmacao=None
        self._data_cancelamento = None

    def Altera_aluno(self,Aluno):
        self._aluno=Aluno
        return True

       
    def Altera_Disciplina(self,Disciplina):
        self._disciplina = Disciplina
        return True
    
   
    def Data_canfirmacao(self):
        self._data_confirmacao = datetime.datetime.now()
        return self._data_confirmacao
    def Data_cancelamento(self):
        self._data_cancelamento=datetime.datetime.now()
        return self._data_cancelamento
    
    





