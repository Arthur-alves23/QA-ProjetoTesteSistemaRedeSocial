# variaveis
usuarios = []
postagens = []
proximo_id_usuario = 1
proximo_id_postagem = 1

# funções
def resetar():
    global usuarios, postagens, proximo_id_usuario, proximo_id_postagem
    usuarios.clear()
    postagens.clear()
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def criar_usuario(nome):
    global proximo_id_usuario
    if nome == '':
        raise Exception
    usuario = {
        'id':proximo_id_usuario,
        'nome':nome,
        'seguidores':[],
        'seguindo':[]
        
    }  
    usuarios.append(usuario)
    proximo_id_usuario += 1


def criar_postagem(usuario, texto):
    global proximo_id_postagem

    if texto == "":
        raise Exception

    try:
        encontrar_usuario_por_id(usuario)
        postagem = {
            'id': proximo_id_postagem,
            'usuario': usuario,
            'mensagem': texto,
            'curtidores':[]
        }
        postagens.append(postagem)
        proximo_id_postagem += 1
    except IndexError as error:
        raise IndexError
  
# Função para seguir um usuário
def seguir_usuario(usuario_seguidor, usuario_a_seguir):
    if usuario_seguidor == usuario_a_seguir:  # Verifica se o usuário tenta seguir a si mesmo
        raise Exception("Não é possível seguir a si mesmo")
    usuario_seguidor_obj = encontrar_usuario_por_id(usuario_seguidor)  # Encontra o usuário seguidor
    usuario_a_seguir_obj = encontrar_usuario_por_id(usuario_a_seguir)  # Encontra o usuário a ser seguido
    
    # Impede que o usuário siga mais de uma vez o mesmo usuário
    if usuario_a_seguir in usuario_seguidor_obj['seguindo']:
        raise Exception("Já segue este usuário")
    
    # Adiciona o usuário à lista de seguidores e de seguindo
    usuario_seguidor_obj['seguindo'].append(usuario_a_seguir)
    usuario_a_seguir_obj['seguidores'].append(usuario_seguidor)

# Função para curtir uma postagem
def curtir_postagem(usuario, postagem):
    postagem_obj = encontrar_postagem_por_id(postagem)  # Encontra a postagem
    # Impede que o usuário curta a mesma postagem mais de uma vez
    if usuario in postagem_obj['curtidores']:
        raise Exception("Você já curtiu esta postagem")
    postagem_obj['curtidores'].append(usuario)  # Adiciona o usuário à lista de curtidores

# Função para comentar em uma postagem
def comentar_postagem(usuario, postagem, texto):
    if texto == "":  # Se o comentário for vazio, gera uma exceção
        raise ValueError("O comentário não pode ser vazio")
    try:
        postagem_obj = encontrar_postagem_por_id(postagem)  # Encontra a postagem
        postagem_obj['comentarios'] = postagem_obj.get('comentarios', [])  # Cria a lista de comentários, se não existir
        postagem_obj['comentarios'].append({'usuario': usuario, 'texto': texto})  # Adiciona o comentário à postagem
    except IndexError:
        raise IndexError("Postagem não encontrada")  # Caso a postagem não exista

def encontrar_usuario_por_id(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return usuario
    raise IndexError

def encontrar_postagem_por_id(post_id):
    return postagens[post_id - 1]

def excluir_usuario(user_id):
    global usuarios, postagens

    # Verifica se o usuário existe
    usuario = encontrar_usuario_por_id(user_id)

    # Remove o usuário da lista
    usuarios = [u for u in usuarios if u['id'] != user_id]

    # Remove as postagens do usuário
    postagens = [p for p in postagens if p['usuario'] != user_id]

    # Remove as curtidas feitas pelo usuário em outras postagens
    for postagem in postagens:
        if user_id in postagem['curtidores']:
            postagem['curtidores'].remove(user_id)

    # Remove os comentários feitos pelo usuário em outras postagens
    for postagem in postagens:
        if 'comentarios' in postagem:
            postagem['comentarios'] = [
                c for c in postagem['comentarios'] if c['usuario'] != user_id
            ]
            
# menu
def exibir_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Criar Usuário")
        print("2. Criar Postagem")
        print("3. Seguir Usuário")
        print("4. Curtir Postagem")
        print("5. Comentar em Postagem")
        print("6. Excluir Usuário")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            criar_usuario(nome)
            print("Usuário criado com sucesso!")
        
        elif opcao == "2":
            user_id = int(input("Digite o ID do autor da postagem: "))
            # usuario = encontrar_usuario_por_id(user_id)
            texto = input("Digite o texto da postagem: ")
            # criar_postagem(usuario, texto)
            print("Postagem criada com sucesso!")
        
        elif opcao == "3":
            user_id = int(input("Digite o seu ID: "))
            target_id = int(input("Digite o ID do usuário que deseja seguir: "))
            # seguir_usuario(user_id, target_id)
            print("Usuário seguido com sucesso!")
        
        elif opcao == "4":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja curtir: "))
            # curtir_postagem(user_id, post_id)
            print("Postagem curtida com sucesso!")
        
        elif opcao == "5":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja comentar: "))
            texto = input("Digite o texto do comentário: ")
            # comentar_postagem(user_id, post_id, texto)
            print("Comentário adicionado com sucesso!")
            
        elif opcao == "6":
            user_id = int(input("Digite o seu ID: "))
            print("Usuário excluido!")
        
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


#exibir_menu()
