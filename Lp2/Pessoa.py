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
   
    def alterar_Nome(self, Nome):
        self._nome = Nome
        return True
    
    def alterar_Celular(self, Celular):
        self._celular = Celular
        return True
    
    def alterar_Email(self, Email):
        self._email = Email
        return True





    


    
    
    
