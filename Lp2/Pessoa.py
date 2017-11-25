class Pessoa(object):
    
    def __init__(self):
        self._nome = None
        self._email = None
        self._celular = None
        
    def retorna_Nome(self):
        return self._nome
    
    def retorna_Email(self):
        return self._email
    
    def retorna_Celular(self):
        return self._celular
   
    def alterar_Nome(self, nome):
        self._nome = nome
        return True
    
    def alterar_Celular(self, celular):
        self._celular = celular
        return True
    
    def alterar_Email(self, email):
        self._email = email
        return True





    


    
    
    
