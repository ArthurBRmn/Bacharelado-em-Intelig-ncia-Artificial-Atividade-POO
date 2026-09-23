from codigo.livro import *

def test_abrir_livro():
    livro = Livro()
    assert livro.abrir() == "O livro foi aberto"

def test_fechar_livro():
    livro = Livro()
    assert livro.fechar() == "O livro foi fechado"

def test_marcar_pagina_livro():
    livro = Livro()
    livro.set_numero_paginas(200)
    livro.marcar_pagina(50)
    assert livro.get_pagina_atual() == 50

def test_marcar_pagina_livro_nao_tem():
    livro = Livro()
    livro.set_numero_paginas(50)
    livro.marcar_pagina(60)
    assert livro.get_pagina_atual() == 1

def test_avancar_pagina():
    livro = Livro()
    livro.set_numero_paginas(200)
    livro.avancar_pagina()
    assert livro.get_pagina_atual() == 2
# só pula de 1 em 1 pagina pq sim

def test_retroceder_pagina():
    livro = Livro()
    livro.set_numero_paginas(400)
    livro.set_pagina_atual(40)
    livro.retroceder_pagina()
    assert livro.get_pagina_atual() == 39

def test_pagina_atual():
    livro = Livro()
    livro.set_pagina_atual(50)
    assert livro.get_pagina_atual() == 50