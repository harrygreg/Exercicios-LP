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
D.Altera_Nome("LP")
D.Altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP1,ListaCargaP1,D.getNome(),D.getCarga())


D.Altera_Nome("SQL")
D.Altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP1,ListaCargaP1,D.getNome(),D.getCarga())


Prof.setApelido("Yuri")
Prof.getApelido()
D.Altera_Nome("DevOPs")
D.Altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP2,ListaCargaP2,D.getNome(),D.getCarga())

D.Altera_Nome("TecWeb")
D.Altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP2,ListaCargaP2,D.getNome(),D.getCarga())

D.Altera_Nome("Engenharia")
D.Altera_Carga(80)
listadisp.append(D.getNome())
listadisp.append(D.getCarga())
Prof.adiciona_disciplina(ListaDispP2,ListaCargaP2,D.getNome(),D.getCarga())
print(listadisp)
print(ListaDispP1,ListaCargaP1)
print(ListaDispP2,ListaCargaP2)

print(Prof.total_carga_horaria(ListaCargaP1))
print(Prof.total_carga_horaria(ListaCargaP2))



