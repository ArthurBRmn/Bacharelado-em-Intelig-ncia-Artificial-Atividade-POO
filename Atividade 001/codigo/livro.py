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