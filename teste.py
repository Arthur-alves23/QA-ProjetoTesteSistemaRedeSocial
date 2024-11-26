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

# Caso de Teste 1: test_seguir_usuario_mesmo_usuario
# Verifica se o sistema impede que um usuário siga a si mesmo.
def test_seguir_usuario_mesmo_usuario():
    resetar()  # Reseta o sistema antes do teste
    criar_usuario("Carlos")  # Cria um usuário
    with pytest.raises(Exception) as error:  # Espera que uma exceção seja levantada
        seguir_usuario(1, 1)  # Tenta seguir a si mesmo (usuário 1 tenta seguir usuário 1)
    assert str(error.value) == "Não é possível seguir a si mesmo"  # Verifica se a exceção é a esperada

# Caso de Teste 2: test_seguir_usuario_inexistente
# Verifica se o sistema lança um erro ao tentar seguir um usuário que não existe.
def test_seguir_usuario_inexistente():
    resetar()
    criar_usuario("Carlos")  # Cria o usuário 1
    with pytest.raises(IndexError):  # Espera-se um IndexError
        seguir_usuario(1, 999)  # Tenta seguir um usuário com ID 999 que não existe

# Caso de Teste 3: test_curtir_mesma_postagem_novamente
# Verifica se o sistema impede curtidas duplicadas na mesma postagem por um mesmo usuário.
def test_curtir_mesma_postagem_novamente():
    resetar()
    criar_usuario("Carlos")  # Cria o usuário 1
    criar_usuario("Ana")  # Cria o usuário 2
    criar_postagem(1, "Postagem testando curtidas")  # Cria uma postagem com o usuário 1
    curtir_postagem(2, 1)  # Usuário 2 curte a postagem 1
    with pytest.raises(Exception) as error:  # Espera-se uma exceção se o usuário tentar curtir novamente
        curtir_postagem(2, 1)  # Usuário 2 tenta curtir a mesma postagem novamente
    assert str(error.value) == "Você já curtiu esta postagem"  # Verifica se a mensagem da exceção é a esperada

# Caso de Teste 4: test_curtir_postagem_inexistente
# Verifica se o sistema lança um erro ao tentar curtir uma postagem inexistente.
def test_curtir_postagem_inexistente():
    resetar()
    criar_usuario("Carlos")
    with pytest.raises(IndexError):  # Espera-se um IndexError
        curtir_postagem(1, 999)  # Tenta curtir uma postagem que não existe (ID 999)

# Caso de Teste 5: test_comentar_postagem_valida
# Verifica se um usuário pode comentar em uma postagem válida.
def test_comentar_postagem_valida():
    resetar()
    criar_usuario("Carlos")
    criar_postagem(1, "Postagem para comentar")
    comentar_postagem(1, 1, "Ótimo post!")  # Usuário 1 comenta na postagem 1
    postagem = postagens[0]  # Pega a postagem 1
    assert len(postagem['comentarios']) == 1  # Verifica se existe um comentário na postagem
    assert postagem['comentarios'][0]['texto'] == "Ótimo post!"  # Verifica se o comentário tem o texto esperado

# Caso de Teste 6: test_comentar_texto_em_branco
# Verifica se o sistema lança um erro ao tentar comentar com um texto em branco.
def test_comentar_texto_em_branco():
    resetar()
    criar_usuario("Carlos")
    criar_postagem(1, "Postagem para comentar")
    with pytest.raises(ValueError) as error:  # Espera-se um ValueError
        comentar_postagem(1, 1, "")  # Tenta comentar com texto vazio
    assert str(error.value) == "O comentário não pode ser vazio"  # Verifica a mensagem do erro

# Caso de Teste 7: test_comentar_postagem_inexistente
# Verifica se o sistema lança um erro ao tentar comentar em uma postagem inexistente.
def test_comentar_postagem_inexistente():
    resetar()
    criar_usuario("Carlos")
    with pytest.raises(IndexError):  # Espera-se um IndexError
        comentar_postagem(1, 999, "Comentário na postagem inexistente")  # Tenta comentar em uma postagem que não existe
        
# Caso de Teste 8: test_excluir_usuario
# Verifica se a exclusão de um usuário remove o usuário, suas postagens, e interações (curtidas e comentários)
def test_excluir_usuario():
    resetar()  # Reseta o sistema antes do teste
    criar_usuario("Carlos")  # Cria o usuário 1
    criar_usuario("Ana")  # Cria o usuário 2

    # Criação de postagens e interações (comentários e curtidas)
    criar_postagem(1, "Postagem de Carlos")
    curtir_postagem(2, 1)  # Usuário 2 curte a postagem de Carlos
    comentar_postagem(2, 1, "Comentário de Ana")

    # Verifica se o usuário e as interações foram criados corretamente
    assert len(usuarios) == 2
    assert len(postagens) == 1
    assert postagens[0]['curtidores'] == [2]
    assert len(postagens[0]['comentarios']) == 1

    # Exclui o usuário 1 (Carlos)
    excluir_usuario(1)

    # Verifica se o usuário 1 foi removido
    assert len(usuarios) == 1  # Apenas o usuário 2 (Ana) deve permanecer
    assert postagens == []  # A postagem de Carlos deve ser removida

    # Verifica que a postagem de Carlos foi excluída
    assert not any(postagem['usuario'] == 1 for postagem in postagens)
    assert not any(id_usuario == 1 for postagem in postagens[0]['curtidores'])
    assert not any(comentario['usuario'] == 1 for postagem in postagens[0]['comentarios'])
    
    
    # python -m pytest .\testes\teste.py -vv
