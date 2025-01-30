def atualizar_estoque(campos):
    """
    Atualiza o arquivo estoque.csv com os valores dos campos editados.
    :param campos: Lista de tuplas contendo os inputs de ID, Nome, Quantidade e Preço.
    """
    caminho_csv = "csv/estoque.csv"

    try:
        with open(caminho_csv, mode="w", encoding="utf-8") as file:
            # Escrevendo o cabeçalho do CSV
            file.write("id;nome;quantidade;preco\n")

            for input_id, input_nome, input_qtd, input_preco in campos:
                id_livro = input_id.getText().strip()
                nome_livro = input_nome.getText().strip()
                quantidade_livro = input_qtd.getText().strip()
                preco_livro = input_preco.getText().strip()

                if id_livro and nome_livro and quantidade_livro and preco_livro:
                    file.write(f"{id_livro};{nome_livro};{quantidade_livro};{preco_livro}\n")

        return "Estoque atualizado com sucesso!"

    except Exception as e:
        return f"Erro ao atualizar estoque: {e}"
