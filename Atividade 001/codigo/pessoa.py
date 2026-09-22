class Pessoa:

    def __init__(self):

        self.nome = 'Marcos'
        self.idade = 0
        self.altura = 0.0
        self.peso = 0.0

    def envelhecer (self):
        self.idade += 1
        print(f'{self.nome} tem {self.idade} anos.\n')

    def crescer (self, centimetro):
        if self.idade < 21:
            self.altura += centimetro
            print(f'{self.nome} cresceu {centimetro} cm.\n')

    def ganhar_peso (self , quilos):
        self.peso += quilos
        print (f'{self.nome} ganhou: {quilos} kg\n')

    def perder_peso (self, quilos_p):
        self.peso -= quilos_p
        print(f'{self.nome} perdeu: {quilos_p} kg\n')

print('_' * 50 + '\nAtividade 4. Pessoa\n' + '_' * 50)