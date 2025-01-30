from graphics import *
from utils.gerar_html_produto import gerar_html_produto

def consultar_produto(janela, id_produto):
    """
    Busca o produto no estoque.csv pelo ID e exibe suas informações na tela com uma tabela bem estruturada.
    Se encontrar, também gera um arquivo HTML com os detalhes.
    :param janela: Instância de GraphWin.
    :param id_produto: ID do produto inserido pelo usuário.
    """
    caminho_csv = "csv/estoque.csv"

    try:
        with open(caminho_csv, mode="r", encoding="utf-8") as file:
            linhas = file.readlines()

            for i, linha in enumerate(linhas):
                if i == 0:
                    continue  # Ignorar o cabeçalho

                dados = linha.strip().split(";")
                if len(dados) == 4:
                    id_livro, nome, quantidade, preco = dados

                    if id_livro == id_produto:
                        preco_formatado = f"R${preco}"

                        # 📍 Ajustando o tamanho e espaçamento da tabela
                        x_tabela = 500   # Posição inicial da tabela
                        y_tabela = 250   # Altura inicial da tabela
                        largura_coluna1 = 100  # Largura para os rótulos
                        largura_coluna2 = 180  # Largura para os valores
                        altura_linha = 45  # Aumentando a altura das células

                        # Criar borda externa da tabela
                        borda_externa = Rectangle(
                            Point(x_tabela, y_tabela),
                            Point(x_tabela + largura_coluna1 + largura_coluna2, y_tabela + altura_linha * 4)
                        )
                        borda_externa.setOutline("black")
                        borda_externa.draw(janela)

                        # Criar linhas horizontais da tabela
                        for i in range(1, 4):  # 3 linhas internas
                            y_pos = y_tabela + (i * altura_linha)
                            linha = Line(
                                Point(x_tabela, y_pos),
                                Point(x_tabela + largura_coluna1 + largura_coluna2, y_pos)
                            )
                            linha.draw(janela)

                        # Criar divisória vertical entre colunas
                        coluna_divisoria = Line(
                            Point(x_tabela + largura_coluna1, y_tabela),
                            Point(x_tabela + largura_coluna1, y_tabela + altura_linha * 4)
                        )
                        coluna_divisoria.draw(janela)

                        # Criar os rótulos (ID, Nome, Qtd, Preço)
                        labels = ["ID:", "Nome:", "Qtd:", "Preço:"]
                        valores = [id_livro, nome, quantidade, preco_formatado]

                        for i in range(4):
                            y_texto = y_tabela + (i * altura_linha) + altura_linha // 2

                            # Criar e estilizar rótulo (coluna 1)
                            label = Text(Point(x_tabela + largura_coluna1 // 2, y_texto), labels[i])
                            label.setSize(12)
                            label.setStyle("bold")
                            label.draw(janela)

                            # Criar e estilizar valor do produto (coluna 2)
                            valor = Text(Point(x_tabela + largura_coluna1 + largura_coluna2 // 2, y_texto), valores[i])
                            valor.setSize(12)
                            valor.draw(janela)

                        # **📌 GERAÇÃO DO HTML**
                        gerar_html_produto(id_livro, nome, quantidade, preco_formatado)
                        print("HTML do produto gerado com sucesso!")

                        return  # Sai da função após encontrar o produto

            # Se não encontrar o produto, exibe mensagem de erro
            mensagem_erro = Text(Point(590.0, 276.0), "Produto não Existe")
            mensagem_erro.setSize(12)
            mensagem_erro.setTextColor("red")
            mensagem_erro.draw(janela)

    except FileNotFoundError:
        erro_msg = Text(Point(400, 100), "Erro: Arquivo estoque.csv não encontrado.")
        erro_msg.setSize(12)
        erro_msg.setTextColor("red")
        erro_msg.draw(janela)
