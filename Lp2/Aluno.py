from Matricula import Matricula

class Aluno(object):
    
    def __init__(self):    
        self._sigla_curso = None
        self._matriculas = None
        
    def disciplinas_alunos(self, lista, disciplina, aluno):
        lista.append(disciplina)
        lista.append(aluno)
        return lista
    
    def getSigla(self, sigla):
        self._sigla_curso = sigla
        
    def matricular(self, Matricula, ListMatricula):
        ListMatricula.append(Matricula)
        return True

    def confirmar_matricula(self, matricula, listaMatricula, disp, listaDisp):
        if disp in listaMatricula:
            return False
        else:
            listaDisp.append(disp)
            if matricula in listaMatricula:
                Matricula.Data_canfirmacao(self)
                return Matricula.Data_canfirmacao(self)
        
    def cancelar_matricula(self, matricula, listaMatricula):
        if matricula in listaMatricula:
            Matricula.Data_cancelamento(self)
            return Matricula.Data_cancelamento(self)

        





