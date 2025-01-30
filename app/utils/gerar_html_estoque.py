def gerar_html_estoque():
    """
    Lê os dados do CSV e gera um arquivo HTML estilizado com a tabela do estoque.
    """
    caminho_csv = "csv/estoque.csv"  # Arquivo CSV de estoque
    caminho_html = "estoque.html"  # Arquivo HTML gerado

    try:
        # Lê os dados do CSV
        with open(caminho_csv, mode="r", encoding="utf-8") as file:
            linhas = file.readlines()

        # Ignorar cabeçalho e preparar os dados
        dados = []
        for i, linha in enumerate(linhas):
            if i == 0:
                continue  # Ignorar cabeçalho
            dados.append(linha.strip().split(";"))  # Separar colunas por ";"

        # HTML base com CSS para estilização da tabela
        html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estoque de Livros</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
        }}
        h2 {{
            color: #333;
        }}
        table {{
            width: 80%;
            margin: auto;
            border-collapse: collapse;
            background: #fff;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }}
        th, td {{
            padding: 12px;
            border: 1px solid #ddd;
            text-align: center;
        }}
        th {{
            background: #007bff;
            color: white;
        }}
        tr:nth-child(even) {{
            background: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h2>Lista de Estoque</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Quantidade</th>
            <th>Preço</th>
        </tr>"""

        # Adiciona os dados na tabela
        for id_livro, nome, quantidade, preco in dados:
            preco_formatado = f"R${preco}"  # Formatar preço
            html_content += f"""
        <tr>
            <td>{id_livro}</td>
            <td>{nome}</td>
            <td>{quantidade}</td>
            <td>{preco_formatado}</td>
        </tr>"""

        # Fecha a estrutura do HTML
        html_content += """
    </table>
</body>
</html>"""

        # Salvar o HTML no arquivo
        with open(caminho_html, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"Arquivo HTML gerado com sucesso: {caminho_html}")

    except FileNotFoundError:
        print("Erro: Arquivo CSV não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
