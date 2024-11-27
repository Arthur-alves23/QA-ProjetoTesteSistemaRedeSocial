import pytest
from main import *


def testaCriarUsuarioValido():
    resetar()
    criar_usuario("Gleison")
    assert usuarios[0] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

def testaCriarUsuarioSemNome():
    resetar()
    with pytest.raises(Exception) as error:
        criar_usuario("")

def testaCriarPostagemValida():
    resetar()
    criar_usuario("Maria")
    criar_postagem(1, "Olá Mundo")

    assert postagens[0] == {
        'id':1, 'usuario':1, 'mensagem': 'Olá Mundo',
        'curtidores':[]
    }

def testCriarPostagemTextoEmBranco():
    resetar()
    criar_usuario('arthur')
    with pytest.raises(Exception) as error:
        criar_postagem(1,"")

def testaRetornaUsuarioPorId():
    resetar()
    criar_usuario('juan')
    criar_usuario('gleison')
    usuario = encontrar_usuario_por_id(2)
    assert usuario == {
        'id':2,
        'nome':'gleison',
        'seguidores':[],
        'seguindo':[]
    }

def testaUsuariosInseridosNaLista():
    resetar()
    criar_usuario('jose')
    criar_usuario('maria')
    listaEsperada = [{
        'id':1, 'nome':'jose', 'seguidores':[], 'seguindo':[]
    },{
        'id':2, 'nome':'maria', 'seguidores':[], 'seguindo':[]
    }]

    assert usuarios == listaEsperada

def testaCriarPostagemUsuarioInexistente():
    resetar()
    with pytest.raises(IndexError) as error:
        criar_postagem(1,'relou')

def testaSeguirUsuarioExistente():
    resetar()
    criar_usuario('gleison')
    criar_usuario('karen')
    seguir_usuario(1,2)

    assert usuarios[0]['seguindo'] == [2]
    assert usuarios[1]['seguidores'] == [1]

def testaSeguirUsuarioInexistente():
    resetar()
    criar_usuario('gleison')
    with pytest.raises(Exception) as error:
        seguir_usuario(1,4)

def testaSeguirMesmoUsuario():
    resetar()
    criar_usuario('gleison')
    with pytest.raises(Exception) as error:
        seguir_usuario(1,1)

def testaCurtirPostagemValida():
    resetar()
    criar_usuario('gleison')
    criar_usuario('jose')
    criar_postagem(1, 'Acorda povo!')
    curtir_postagem(2, 1)

    assert postagens[0]['curtidores'] == [2]

#def testaCurtirPostagemNovamente():
#    resetar()
#    criar_usuario('gleison')
#    criar_usuario('jose')
#    criar_postagem(1, 'Adoro testar!')
#    curtir_postagem(2, 1)
#    with pytest.raises(Exception) as error:
#        curtir_postagem(2, 1)


#python -m pytest .\testes\teste.py -vv
#python -m pytest .\teste.py -vv

# Caso de Teste 1: test_seguir_usuario_mesmo_usuario
# Verifica se o sistema impede que um usuário siga a si mesmo.
def test_seguir_usuario_mesmo_usuario():
    resetar()  
    criar_usuario("Carlos")  
    with pytest.raises(Exception) as error:  
        seguir_usuario(1, 1) 
    assert str(error.value) == "Não é possível seguir a si mesmo" 



def test_curtir_mesma_postagem_novamente():
    resetar()
    criar_usuario("Carlos")  
    criar_usuario("Ana")  
    criar_postagem(1, "Postagem testando curtidas")  
    curtir_postagem(2, 1)  
    with pytest.raises(Exception) as error:  
        curtir_postagem(2, 1)  
    assert str(error.value) == "Você já curtiu esta postagem" 


def test_curtir_postagem_inexistente():
    resetar()
    criar_usuario("Carlos")
    with pytest.raises(IndexError): 
        curtir_postagem(1, 999)  


def test_comentar_postagem_valida():
    resetar()
    criar_usuario("Carlos")
    criar_postagem(1, "Postagem para comentar")
    comentar_postagem(1, 1, "Ótimo post!")  
    postagem = postagens[0]  
    assert len(postagem['comentarios']) == 1  
    assert postagem['comentarios'][0]['texto'] == "Ótimo post!"  


def test_comentar_texto_em_branco():
    resetar()
    criar_usuario("Carlos")
    criar_postagem(1, "Postagem para comentar")
    with pytest.raises(ValueError) as error:  
        comentar_postagem(1, 1, "")  
    assert str(error.value) == "O comentário não pode ser vazio"  

def test_comentar_postagem_inexistente():
    resetar()
    criar_usuario("Carlos")
    with pytest.raises(IndexError):  
        comentar_postagem(1, 999, "Comentário na postagem inexistente")  
        
def test_excluir_usuario():
    resetar()
    criar_usuario("João")
    criar_usuario("Maria")
    criar_postagem(1, "Postagem de João")
    criar_postagem(2, "Postagem de Maria")
    curtir_postagem(1, 2)
    curtir_postagem(2, 1)
    comentar_postagem(1, 2, "Comentário de João na postagem de Maria")
    comentar_postagem(2, 1, "Comentário de Maria na postagem de João")

    excluir_usuario(1)

    
    assert all(p['usuario'] for p in postagens), f"Erro: Postagens finais: {postagens}"

    
    for postagem in postagens:
        assert 1 not in postagem['curtidores'], f"Erro: Curtidores na postagem {postagem['id']}: {postagem['curtidores']}"
        assert all(c['usuario'] for c in postagem.get('comentarios', [])), f"Erro: Comentários na postagem {postagem['id']}: {postagem.get('comentarios', [])}"

    
        assert all(u['id'] for u in usuarios), f"Erro: Usuários finais: {usuarios}"




        # python -m pytest .\teste.py -vv
