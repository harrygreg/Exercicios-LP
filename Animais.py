arquivo = open("Animais.txt")
texto = arquivo.read()
lista=texto.split()
animais = sorted(lista)
with open('Animais_Ordenados.txt','w') as arquivo2:
    for x in range(0, len(animais)):
        arquivo2.write("{}\n".format(animais[x]))
        
