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