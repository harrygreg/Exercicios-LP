class Dicionario(dict):

    def __init__(self):
        self = dict()

    def add(self, chave, valor):
        self[chave] = valor
        
arquivo = open("tweets.txt")
tweets = arquivo.read()
lista_tweets = tweets.split()
dic = Dicionario()

        
                
with open('Qtd_tweets.txt','w') as arquivo2:
    for x in range (0,len(lista_tweets)):
        palavra = lista_tweets[x]
        if palavra not in dic:
           arquivo2.write("{};{}\n".format(palavra,lista_tweets.count(palavra)))
           dic.add(palavra,lista_tweets.count(palavra))
    

