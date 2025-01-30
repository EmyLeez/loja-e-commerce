def verificar_login(email_digitado, senha_digitada):
    """
    Verifica se o email e a senha correspondem a um usuário no arquivo CSV.
    :param email_digitado: Email inserido pelo usuário.
    :param senha_digitada: Senha inserida pelo usuário.
    :return: True se login for bem-sucedido, False caso contrário.
    """
    try:
        with open("C:\\Users\\55979\\Documents\\repositorios\\loja-e-commerce\\app\\csv\\login.csv", mode="r", encoding="utf-8") as file:
            linhas = file.readlines()  # Lê todas as linhas do arquivo

            for i, linha in enumerate(linhas):
                if i == 0:
                    continue  # Pular a primeira linha (cabeçalho)

                dados = linha.strip().split(";")  # Divide a linha pelos ";"
                
                if len(dados) == 3:  # Garantir que temos os 3 campos (nome, email, senha)
                    nome, email, senha = dados
                    if email == email_digitado and senha == senha_digitada:
                        return True  # Credenciais corretas

    except FileNotFoundError:
        print("Arquivo login.csv não encontrado.")
    except Exception as e:
        print(f"Erro ao verificar login: {e}")

    return False  # Caso não encontre usuário correspondente
