class Disciplina(object):
    
    def __init__(self):
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
    
    def altera_Nome(self, nome):
        self._nome = nome
        
    def getCarga(self):
        return self._carga
    
    def altera_Carga(self, Carga):
        try:
            if Carga <= 0 :
                return False
            else:
                self._carga = Carga
                return True
        except Exception as e:
            print(e)
            return False
        
    def getTeoria(self):
         return self._teoria
 
    def altera_Teoria(self, teoria):
        try:
            if teoria <= 0 :
                return False
            else:
                self._teoria = teoria
                return True
        except Exception as e:
            print(e)
            return False
       
    def getPratica(self):
        return self._pratica

    def altera_Pratica(self, pratica):
        try:
            if Pratica <= 0 :
                return False
            else:
                self._pratica = pratica
                return True
        except Exception as e:
            print(e)
            return False

    def getEmenta(self):
        return self._ementa
    
    def setEmenta(self, ementa):
        self._ementa = ementa

    def altera_Ementa(self, novoEmenta):
        self._ementa = novoEmenta
        
    def getCompetencias(self):
        return self._competencias
    
    def setCompetencias(self, competencias):
        self._competencias = competencias

    def altera_Competencias(self, novoCompetencias):
        self._competencias = novoCompetencias
        
    def getHabilidades(self):
        return self._habilidades
    
    def setHabilidades(self, habilidades):
        self._habilidades = habilidades

    def altera_Habilidades(self, novoHabilidades):
        self._habilidades = novoHabilidades
        
    def getConteudo(self):
        return self._conteudo
    
    def setConteudo(self, conteudo):
        self._conteudo = conteudo

    def altera_Conteudo(self, novoConteudo):
        self._conteudo = novoConteudo

    def getBibliografia_basica(self):
        return self._bibliografia_basica
    
    def setBibliografia_basica(self, bibliografia_basica):
        self._bibliografia_basica = bibliografia_basica

    def altera_Bibliografia_basica(self, novoBibliografia_basica):
        self._bibliografia_basica = novoBibliografia_basica
        
    def getBibliografia_complementar(self):
        return self._bibliografia_complementar
    
    def setBibliografia_complementar(self, bibliografia_complementar):
        self._bibliografia_complementar = bibliografia_complementar

    def altera_Bibliografia_complementar(self, novoBibliografia_complementar):
        self._bibliografia_complementar = novoBibliografia_complementar
    
        



     
