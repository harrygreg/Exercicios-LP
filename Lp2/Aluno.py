from Matricula import Matricula

class Aluno(object):
    
    def __init__(self):    
        self._sigla_curso = None
        self._matriculas = None
        
    def disciplinas_alunos(self, lista, Disciplina, Aluno):
        lista.append(Disciplina)
        lista.append(Aluno)
        return lista
    
    def getSigla(self, Sigla):
        self._sigla_curso = Sigla
        
    def matricular(self, Matricula, ListMatricula):
        ListMatricula.append(Matricula)
        return True

    def confirmar_matricula(self, matricula, ListaMatricula, Disp, ListaDisp):
        if Disp in ListaMatricula:
            return False
        else:
            ListaDisp.append(Disp)
            if matricula in ListMatricula:
                Matricula.Data_canfirmacao(self)
                return Matricula.Data_canfirmacao(self)
        
    def cancelar_matricula(self, matricula, ListaMatricula):
        if matricula in ListMatricula:
            Matricula.Data_cancelamento(self)
            return Matricula.Data_cancelamento(self)

        





