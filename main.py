# variaveis
usuarios = []
postagens = []
proximo_id_usuario = 1
proximo_id_postagem = 1

# funções

def criar_usuario(nome):
    global proximo_id_usuario
    if nome == '':
        raise ValueError("Nome não pode ser vazio")
    usuario = {
        'id':proximo_id_usuario,
        'nome':nome,
        'seguidores':[],
        'seguindo':[]
    }  
    usuarios.append(usuario)
    proximo_id_usuario += 1


def criar_postagem(usuario_id, texto):
    global proximo_id_postagem
    if texto == '':
        raise ValueError("Texto não pode ser vazio")
    
    usuario = encontrar_usuario_por_id(usuario_id)
    postagem = {
        'id': proximo_id_postagem,
        'usuario_id': usuario_id,
        'texto': texto,
        'curtidas': [],
        'comentarios': []
    }
    postagens.append(postagem)
    proximo_id_postagem += 1
    
    
def seguir_usuario(usuario_seguidor_id, usuario_a_seguir_id):
    if usuario_seguidor_id == usuario_a_seguir_id:
        return  # Não fazer nada se o usuário tentar seguir a si mesmo.
    
    try:
        usuario_seguidor = encontrar_usuario_por_id(usuario_seguidor_id)
        usuario_a_seguir = encontrar_usuario_por_id(usuario_a_seguir_id)
    except IndexError:
        raise IndexError("Usuário não encontrado")
    
    if usuario_a_seguir_id not in usuario_seguidor['seguindo']:
        usuario_seguidor['seguindo'].append(usuario_a_seguir_id)
        usuario_a_seguir['seguidores'].append(usuario_seguidor_id)

def curtir_postagem(usuario_id, postagem_id):
    try:
        usuario = encontrar_usuario_por_id(usuario_id)
        postagem = encontrar_postagem_por_id(postagem_id)
    except IndexError:
        raise IndexError("Usuário ou postagem não encontrados")
    
    if usuario_id not in postagem['curtidas']:
        postagem['curtidas'].append(usuario_id)


def comentar_postagem(usuario_id, postagem_id, texto):
    if texto == '':
        raise ValueError("Comentário não pode ser vazio")
    
    try:
        usuario = encontrar_usuario_por_id(usuario_id)
        postagem = encontrar_postagem_por_id(postagem_id)
    except IndexError:
        raise IndexError("Usuário ou postagem não encontrados")
    
    comentario = {
        'usuario_id': usuario_id,
        'texto': texto
    }
    postagem['comentarios'].append(comentario)


def encontrar_usuario_por_id(user_id):
    if user_id <= 0 or user_id > len(usuarios):
        raise IndexError("Usuário não encontrado")
    return usuarios[user_id - 1]


def encontrar_postagem_por_id(post_id):
    if post_id <= 0 or post_id > len(postagens):
        raise IndexError("Postagem não encontrada")
    return postagens[post_id - 1]



# MENU
def exibir_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Criar Usuário")
        print("2. Criar Postagem")
        print("3. Seguir Usuário")
        print("4. Curtir Postagem")
        print("5. Comentar em Postagem")
        print("6. Sair")

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
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


#exibir_menu()
#Terminal: python -m pytest ./teste.py