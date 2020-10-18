from Cidade import Cidade
from Adjacente import Adjacente

class Rota:
    cacador = Cidade("Caçador", 261)
    florianopolis = Cidade("Florianópolis", 0)
    itajai = Cidade("Itajai ", 77)
    blumenau = Cidade("Blumenau ", 93)
    brusque = Cidade("Brusque ", 66)
    riodosul = Cidade("Rio do Sul", 118)
    palhoca = Cidade("Palhoça ", 14)
    lages = Cidade("Lages ", 176)
    curitibanos = Cidade("Curitibanos ", 204)
    santacecilia = Cidade("Santa Cecília ", 198)
    videira = Cidade("Videira ", 265)

    cacador.addCidadeAdjacente(Adjacente(videira, 40))
    cacador.addCidadeAdjacente(Adjacente(santacecilia, 74))

    videira.addCidadeAdjacente(Adjacente(cacador, 40))
    videira.addCidadeAdjacente(Adjacente(curitibanos, 81))

    curitibanos.addCidadeAdjacente(Adjacente(videira, 81))
    curitibanos.addCidadeAdjacente(Adjacente(lages, 93))

    lages.addCidadeAdjacente(Adjacente(curitibanos, 93))
    lages.addCidadeAdjacente(Adjacente(riodosul, 128))
    lages.addCidadeAdjacente(Adjacente(palhoca, 212))

    palhoca.addCidadeAdjacente(Adjacente(lages, 212))
    palhoca.addCidadeAdjacente(Adjacente(florianopolis, 22))

    florianopolis.addCidadeAdjacente(Adjacente(palhoca, 22))
    florianopolis.addCidadeAdjacente(Adjacente(itajai,99))
    
    itajai.addCidadeAdjacente(Adjacente(florianopolis,99))
    itajai.addCidadeAdjacente(Adjacente(brusque,35))
    itajai.addCidadeAdjacente(Adjacente(blumenau,58))

    blumenau.addCidadeAdjacente(Adjacente(itajai,58))
    blumenau.addCidadeAdjacente(Adjacente(riodosul,96))

    brusque.addCidadeAdjacente(Adjacente(itajai,35))
    brusque.addCidadeAdjacente(Adjacente(riodosul,136))
    
    riodosul.addCidadeAdjacente(Adjacente(blumenau,96))
    riodosul.addCidadeAdjacente(Adjacente(brusque,136))
    riodosul.addCidadeAdjacente(Adjacente(lages,128))
    riodosul.addCidadeAdjacente(Adjacente(santacecilia,136))

    santacecilia.addCidadeAdjacente(Adjacente(riodosul,136))
    santacecilia.addCidadeAdjacente(Adjacente(cacador,74))
