class Carro():
    def __init__(self, marca, modelo, ano, cor, statusFarol = 'desligado'):
        self.marca = marca
        self.modelo = modelo
        self.anoDeFabricacao = ano
        self.cor = cor

        self.statusFarol = statusFarol

        self.velocimetro = 0

        self.__status = False

    def ligarFarol(self):
        if (self.statusFarol == 'desligado'):
            self.statusFarol = 'ligado'
            print('Farol ligado')
        else:
            print('O farol já está ligado')

    def desligarFarol(self):
        if (self.statusFarol == 'ligado'):
            self.statusFarol = 'desligado'
            print('Farol desligado')

    def acelerar(self, acresVelocidade):
        self.velocimetro = self.velocimetro + acresVelocidade

    def frear(self, descresVelocidade = 5):
        if (self.velocimetro > descresVelocidade):
            self.velocimetro = self.velocimetro - descresVelocidade
        else:
            self.velocimetro = 0

    def getSatus(self): # pegar e retornar o valor da varialvel __status
        return self.__status

    def setStatus(self, novo_status, chave):

        chave_certa = self.__verifica_chave(chave)

        if chave_certa:
            self._status = novo_status
            print('Chave correta, carro ligado')
        else:
            print('O stuatus não pode ser alterado')

gol = Carro('wolks', 'gol', 2010, 'laranja')
fusca = Carro('wolks', 'fusca', 1990 , 'azul claro')
uno = Carro('fiat', 'uno', 2000, 'azul escuro', statusFarol = 'ligado')
gol2 = Carro('wolks', 'gol', 2010, 'laranja')
fox = Carro('wolks', 'fox', 2009, 'prata')
