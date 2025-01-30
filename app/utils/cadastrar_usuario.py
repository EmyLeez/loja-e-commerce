def cadastrar_usuario(nome, email, senha):
    """
    Cadastra um novo usuário no arquivo CSV, verificando se o email já existe.
    :param nome: Nome do usuário.
    :param email: Email do usuário.
    :param senha: Senha do usuário.
    :return: Mensagem de sucesso ou erro.
    """
    caminho_csv = "C:\\Users\\55979\\Documents\\repositorios\\loja-e-commerce\\app\\csv\\login.csv"

    try:
        # Verificar se já existe um usuário com o mesmo email
        with open(caminho_csv, mode="r", encoding="utf-8") as file:
            linhas = file.readlines()

            for i, linha in enumerate(linhas):
                if i == 0:
                    continue  # Ignorar o cabeçalho
                
                dados = linha.strip().split(";") #Lista de valores
                
                if len(dados) == 3:  # Garantir que a linha tem os 3 campos
                    _, email_existente, _ = dados
                    if email_existente == email:
                        return "Esse email já está cadastrado."

        # Verificar se os campos estão vazios
        if not nome or not email or not senha:
            return "Você precisa preencher todos os dados."

        # Se passou na validação, cadastrar o usuário corretamente em uma nova linha
        with open(caminho_csv, mode="a", encoding="utf-8") as file:
            file.write(f"\n{nome};{email};{senha}")

        return "Usuário cadastrado, você será redirecionado."

    except FileNotFoundError:
        return "Arquivo login.csv não encontrado."
    except Exception as e:
        return f"Erro ao cadastrar usuário: {e}"
