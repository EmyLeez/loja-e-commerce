import os

def gerar_html_produto(id_livro, nome_livro, quantidade_livro, preco_livro):
    """
    Gera um arquivo HTML contendo os detalhes do produto consultado.
    :param id_livro: ID do produto.
    :param nome_livro: Nome do produto.
    :param quantidade_livro: Quantidade disponível.
    :param preco_livro: Preço do produto.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Detalhes do Produto</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f4f4f4;
                text-align: center;
            }}
            h2 {{
                color: #333;
            }}
            table {{
                width: 50%;
                margin: auto;
                border-collapse: collapse;
                background: white;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }}
            th, td {{
                padding: 10px;
                border: 1px solid #ccc;
                text-align: left;
            }}
            th {{
                background: #ddd;
            }}
        </style>
    </head>
    <body>
        <h2>Detalhes do Produto</h2>
        <table>
            <tr>
                <th>ID</th>
                <td>{id_livro}</td>
            </tr>
            <tr>
                <th>Nome</th>
                <td>{nome_livro}</td>
            </tr>
            <tr>
                <th>Quantidade</th>
                <td>{quantidade_livro}</td>
            </tr>
            <tr>
                <th>Preço</th>
                <td>{preco_livro}</td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Define o caminho do arquivo HTML
    caminho_html = "produto_consultado.html"

    # Escreve o HTML no arquivo
    with open(caminho_html, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Arquivo HTML gerado: {caminho_html}")
