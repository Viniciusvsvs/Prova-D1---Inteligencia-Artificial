from VetorAdjacente import VetorAdjacente


class Main:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print("\nCidade Atual: {}" .format(atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            print("Chegamos na capital de destino: {} " .format(self.objetivo.nome))
            self.achou = True
        else:
            self.fronteira = VetorAdjacente(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                Main.buscar(self, self.fronteira.getPrimeiro())



from Rota import Rota
rota = Rota()
aestrela = Main(rota.florianopolis)
aestrela.buscar(Rota.cacador)
