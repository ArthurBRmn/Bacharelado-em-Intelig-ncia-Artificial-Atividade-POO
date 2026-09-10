 # 1. Classe veiculo

class Veiculo:

    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.ano = 0
        self.velocidade_atual = 0
        self.ligado = False

    def acelerar (self, quantidade):
        if self.ligado == True:
            self.velocidade_atual += quantidade
            print(f'Velocidade atual: {self.velocidade_atual}\n')

    def frear (self,quantidade_f):
        self.velocidade_atual -= quantidade_f

        if self.velocidade_atual < 0:
            self.velocidade_atual = 0

        print(f'Velocidade atual: {self.velocidade_atual}\n')

# Se ligado == False vai virar True
    def ligar (self):
        if self.ligado == False:
            self.ligado = True
            print('Carro ligou\n')

# Se ligado == True vai virar False e zerar a velocidade
    def desligar (self):
        if self.ligado == True:
            self.ligado = False
            self.velocidade_atual = 0
            print('Carro desligou\n')

print('_' * 50 + '\nAtividade 1. Veiculo\n' + '_' * 50)

veiculo1 = Veiculo()
veiculo1.ligar()
veiculo1.acelerar(50)
veiculo1. frear(25)

# 2. Classe ContaBancaria:

class ContaBancaria:
    def __init__(self):
        self.titular =''
        self.numero_conta = 0
        self.saldo = 0

    def depositar (self, valor):
        self.saldo += valor
        print(f'Depositado com sucesso: {valor} R$, o seu saldo: {self.saldo}\n')

    def sacar (self, valor_r):
        if valor_r <= self.saldo:
            self.saldo -= valor_r
            print(f'saque: {valor_r} R$, o seu saldo: {self.saldo}\n')

print('_' * 50 +'\nAtividade 2. ContaBancaria\n' + '_' * 50)


contabancaria1 = ContaBancaria()
contabancaria1.depositar(1800)
contabancaria1.sacar(500)

print(f'Saldo bancário: {contabancaria1.saldo}\n')

# Classe Livro:

class Livro:

    def __init__(self):

        self.titulo = ''
        self.autor =''
        self.ano_publicacao = 0
        self.numero_paginas = 170
        self.genero = ''

        self.pagina_atual = 5

    def abrir (self):
        print('Livro aberto\n')

    def fechar (self):
        print('Livro fechado\n')

    def marcar_pagina (self,pagina):
        if self.numero_paginas >= pagina:
            self.pagina_atual = pagina
            print(f'Você marcou a página: {self.pagina_atual}\n')

    def avancar_pagina (self):
        if self.pagina_atual < self.numero_paginas:
            self.pagina_atual += 1
            print(f'Você avançou para página: {self.pagina_atual}\n')

    def retroceder_pagina (self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
            print(f'Você retrocedeu para a pagina: {self.pagina_atual}\n')

print('_' * 50 + '\nAtividade 3. Livro\n' + '_' * 50)

livro1 = Livro()
livro1.abrir()
livro1.avancar_pagina()
livro1.avancar_pagina()
livro1.retroceder_pagina()
livro1.marcar_pagina(50)
livro1.fechar()

# 4. Classe Pessoa:

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

pessoa1 = Pessoa()
pessoa1.envelhecer()
pessoa1.crescer(0.02)
pessoa1.ganhar_peso(1.5)
pessoa1.perder_peso(2)

# 5. Classe Produto:

class Produto:

    def __init__(self):
        self.nome = ''
        self.preco = 5.50
        self.quantidade_estoque = 0
        self.categoria = ''

    def adicionar_estoque (self,quantidade):
        self.quantidade_estoque += quantidade
        print(f'Adicionando a o estoque: {quantidade}, total no estoque: {self.quantidade_estoque}\n')

    def remover_estoque (self, quantidade_r):

        if quantidade_r <= self.quantidade_estoque:
            self.quantidade_estoque -= quantidade_r
            print(f'Removendo do estoque: {quantidade_r}, total no estoque: {self.quantidade_estoque}\n')

    def aplicar_desconto (self, valor_d):

        self.preco *= 1 - valor_d / 100
        print(f'Desconto: {valor_d}, preço total: {self.preco}\n')

print('_' * 50 + '\nAtividade 5. Produto\n' + '_' * 50)

produto1 = Produto()
produto1.adicionar_estoque(10)
produto1.remover_estoque(5)
produto1.aplicar_desconto(10)

# 6. Classe Funcionario

class Funcionario:

    def __init__(self):

        self.nome = ''
        self.cargo = ''
        self.salario = 1000
        self.departamento = ''

    def receber_aumento (self, porcentual):

        self.salario *= 1 + porcentual/100
        print(f'\nSalario com aumento : {porcentual} % = {self.salario} R$')
        print()

    def mudar_departamento (self, novo_departamento):
        self.departamento = novo_departamento
        print(f'Funcionário {self.nome} e do {self.departamento} agora.')
        print()

    def exibir_dados(self):
        print(f'Nome: {self.nome} \nCargo: {self.cargo} '
              f'\nSalario: {self.salario} \nDepartamento: {self.departamento}\n')

print('_' * 50 + '\nAtividade 6. Funcionário\n' + '_' * 50)

funcionario1 = Funcionario()
funcionario1.receber_aumento(10)
funcionario1.mudar_departamento('Deparmento 2')
funcionario1.exibir_dados()
