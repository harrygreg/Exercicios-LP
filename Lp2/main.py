from Disciplina import Disciplina
from Professor import Professor

D = Disciplina()
listadisp = []
ListaDispP1 = []
ListaCargaP1=[]
ListaDispP2 = []
ListaCargaP2=[]
Prof = Professor()
Prof.setApelido("GUGU")
Prof.getApelido()
D.altera_Nome("LP")
D.altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP1,ListaCargaP1,D.getNome(),D.getCarga())


D.altera_Nome("SQL")
D.altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP1,ListaCargaP1,D.getNome(),D.getCarga())


Prof.setApelido("Yuri")
Prof.getApelido()
D.altera_Nome("DevOPs")
D.altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP2,ListaCargaP2,D.getNome(),D.getCarga())

D.altera_Nome("TecWeb")
D.altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP2,ListaCargaP2,D.getNome(),D.getCarga())

D.altera_Nome("Engenharia")
D.altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP2,ListaCargaP2,D.getNome(),D.getCarga())

print(listadisp)
print(ListaDispP1,ListaCargaP1)
print(ListaDispP2,ListaCargaP2)

print(Prof.total_carga_horaria(ListaCargaP1))
print(Prof.total_carga_horaria(ListaCargaP2))



