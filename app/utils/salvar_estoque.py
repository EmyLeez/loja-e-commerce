import os

def salvar_estoque(id_livro, nome_livro, quantidade_livro, preco_livro):
    """
    Salva ou atualiza o estoque no arquivo CSV.
    Se o ID do livro já existir, a quantidade será atualizada.
    Caso contrário, um novo livro será adicionado.
    """
    caminho_csv = "C:\\Users\\55979\\Documents\\repositorios\\loja-e-commerce\\app\\csv\\estoque.csv"

    try:
        # Verificar se o arquivo existe, se não, criar com cabeçalho
        if not os.path.exists(caminho_csv):
            with open(caminho_csv, mode="w", encoding="utf-8") as file:
                file.write("id;nome;quantidade;preco\n")

        # Ler todas as linhas do arquivo
        with open(caminho_csv, mode="r", encoding="utf-8") as file:
            linhas = file.readlines()

        estoque_atualizado = []
        livro_existente = False

        for i, linha in enumerate(linhas):
            if i == 0:
                estoque_atualizado.append(linha.strip())  # Mantém o cabeçalho
                continue
            
            dados = linha.strip().split(";")

            if len(dados) == 4:
                id_existente, nome_existente, quantidade_existente, preco_existente = dados

                # Se o ID já existe, atualiza a quantidade
                if id_existente == id_livro:
                    nova_quantidade = int(quantidade_existente) + int(quantidade_livro)
                    estoque_atualizado.append(f"{id_livro};{nome_livro};{nova_quantidade};{preco_livro}")
                    livro_existente = True
                else:
                    estoque_atualizado.append(linha.strip())

        # Se o livro não existia, adicionar ao final
        if not livro_existente:
            estoque_atualizado.append(f"{id_livro};{nome_livro};{quantidade_livro};{preco_livro}")

        # Escrever de volta no CSV
        with open(caminho_csv, mode="w", encoding="utf-8") as file:
            for linha in estoque_atualizado:
                file.write(linha + "\n")

        return "Livro cadastrado/atualizado com sucesso!"

    except FileNotFoundError:
        return "Arquivo estoque.csv não encontrado."
    except Exception as e:
        return f"Erro ao salvar o estoque: {e}"
