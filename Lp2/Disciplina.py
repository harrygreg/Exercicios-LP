class Disciplina(object):
    def __init(self):
        self._nome = None
        self._carga = None
        self._teoria = None
        self._pratica = None
        self._ementa = None
        self._competencias = None
        self._conteudo = None
        self._bibliografia_basica = None
        self._bibliografia_complementar = None

    def getNome(self):
        return self._nome
    
    
        
    def Altera_Nome(self,Nome):
        self._nome=Nome
    def getCarga(self):
        return self._carga
    def Altera_Carga(self,Carga):
        try:
            if Carga <= 0 :
                return False
            else:
                self._carga=Carga
                return True
        except Exception as e:
            return print(e)
    def getTeoria(self):
         return self._teoria
    
    
       

    def Altera_Teoria(self,Teoria):
        try:
            if Teoria <= 0 :
                return False
            else:
                self._teoria=Teoria
                return True
        except Exception as e:
            return print(e)
       

    def getPratica(self):
        return self._pratica
    
    

    def Altera_Pratica(self,Pratica):
        try:
            if Pratica <= 0 :
                return False
            else:
                self._pratica=Pratica
                return True
        except Exception as e:
            return print(e)

    def getEmenta(self):
        return self._ementa
    
    def setEmenta(self,Ementa):
        self._ementa=Ementa

    def Altera_Ementa(self,NovoEmenta):
        self._ementa=NovoEmenta
        
    def getCompetencias(self):
        return self._competencias
    
    def setCompetencias(self,Competencias):
        self._competencias=Competencias

    def Altera_Competencias(self,NovoCompetencias):
        self._competencias=NovoCompetencias
        
    def getHabilidades(self):
        return self._habilidades
    
    def setHabilidades(self,Habilidades):
        self._habilidades=Habilidades

    def Altera_Habilidades(self,NovoHabilidades):
        self._habilidades=NovoHabilidades
        
    def getConteudo(self):
        return self._conteudo
    
    def setConteudo(self,Conteudo):
        self._conteudo=Conteudo

    def Altera_Conteudo(self,NovoConteudo):
        self._conteudo=NovoConteudo

        
    def getBibliografia_basica(self):
        return self._bibliografia_basica
    
    def setBibliografia_basica(self,Bibliografia_basica):
        self._bibliografia_basica=Bibliografia_basica

    def Altera_Bibliografia_basica(self,NovoBibliografia_basica):
        self._bibliografia_basica=NovoBibliografia_basica
        
    def getBibliografia_complementar(self):
        return self._bibliografia_complementar
    
    def setBibliografia_complementar(self,Bibliografia_complementar):
        self._bibliografia_complementar=Bibliografia_complementar

    def Altera_Bibliografia_complementar(self,NovoBibliografia_complementar):
        self._bibliografia_complementar=Bibliografia_complementar
    
        



     
