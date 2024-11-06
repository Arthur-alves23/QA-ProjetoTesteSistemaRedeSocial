import pytest
from main import *

def setup_function():
    usuarios.clear()
    postagens.clear()
    #proximo_id_usuario = 1
    #proximo_id_postagem = 1

#def testaCriarUsuarioValido():
#    criar_usuario("Gleison")
#    assert len(usuarios) == 1 
#    assert usuarios[0] == {
#       'id':1, 'nome':'Gleison',
#       'seguidores':[], 'seguindo':[]}

def test_criar_usuario_valido():
    criar_usuario("Karen")
    assert len(usuarios) == 1
    assert usuarios[0]['nome'] == "Karen"
    assert usuarios[0]['seguidores'] == []
    assert usuarios[0]['seguindo'] == []

def testaCriarUsuarioSemNome():
    #with pytest.raises(Exception) as error:
    with pytest.raises(ValueError):
        criar_usuario("")
        

def test_criar_usuario_valido():
    criar_usuario("Karen")
    assert usuarios[0]["nome"] == "Karen"
    assert usuarios[0]["id"] == 1
    assert usuarios[0]["seguidores"] == []
    assert usuarios[0]["seguindo"] == []

def test_criar_usuario_nome_em_branco():
    with pytest.raises(ValueError):  # ou IndexError, dependendo da sua implementação
        criar_usuario("")

def test_criar_postagem_valida():
    criar_usuario("Karen")
    criar_postagem(1, "Olá, mundo!")
    assert postagens[0]["usuario_id"] == 1
    assert postagens[0]["texto"] == "Olá, mundo!"
    assert postagens[0]["curtidas"] == []
    assert postagens[0]["comentarios"] == []

def test_criar_postagem_texto_em_branco():
    criar_usuario("Karen")
    with pytest.raises(ValueError):
        criar_postagem(1, "")

def test_criar_postagem_usuario_inexistente():
    with pytest.raises(IndexError):
        criar_postagem(999, "Postagem de usuário inexistente")
        

#Terminal: python -m pytest ./teste.py





