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