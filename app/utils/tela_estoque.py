from graphics import *

def desenhar_tela_estoque(janela):
    """
    Desenha a tela de estoque e exibe os itens do CSV como uma tabela estilizada com bordas.
    :param janela: Instância de GraphWin.
    :return: Retorna o botão de voltar.
    """
    # Limpa a tela antes de desenhar a nova
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem da tela de estoque
    tela_estoque = Image(Point(400, 300), "assets/tela_estoque.png")
    tela_estoque.draw(janela)

    # Criar botão "Voltar" no canto inferior direito
    botao_voltar = Rectangle(Point(714.0, 560.0), Point(800.0, 600.0))
    botao_voltar.setFill("gray")
    botao_voltar.setOutline("black")
    botao_voltar.draw(janela)

    # Texto no botão "Voltar"
    texto_voltar = Text(Point(757.5, 580.0), "Voltar")
    texto_voltar.setSize(10)
    texto_voltar.setStyle("bold")
    texto_voltar.draw(janela)

    # Ler os itens do CSV e exibir na tabela com bordas
    try:
        caminho_csv = "csv/estoque.csv"

        with open(caminho_csv, mode="r", encoding="utf-8") as file:
            linhas = file.readlines()

            y_pos = 200  # Posição inicial para exibir os itens

            for i, linha in enumerate(linhas):
                if i == 0:
                    continue  # Ignorar o cabeçalho

                dados = linha.strip().split(";")
                if len(dados) == 4:
                    id_livro, nome, quantidade, preco = dados

                    # Adiciona "R$" antes do preço
                    preco_formatado = f"R${preco}"

                    # Criar e exibir os itens nas posições corretas
                    texto_id = Text(Point(41.0, y_pos), id_livro)
                    texto_nome = Text(Point(214.0, y_pos), nome)
                    texto_qtd = Text(Point(513.0, y_pos), quantidade)
                    texto_preco = Text(Point(675.0, y_pos), preco_formatado)  # Preço formatado

                    # Estilizar as células da tabela
                    for texto in [texto_id, texto_nome, texto_qtd, texto_preco]:
                        texto.setSize(10)
                        texto.draw(janela)

                    # Criar bordas para cada linha da tabela
                    linha_tabela = Rectangle(Point(20, y_pos - 10), Point(780, y_pos + 10))
                    linha_tabela.setOutline("black")
                    linha_tabela.draw(janela)

                    y_pos += 30  # Ajusta a linha para o próximo item

    except FileNotFoundError:
        erro_msg = Text(Point(400, 100), "Erro: Arquivo estoque.csv não encontrado.")
        erro_msg.setSize(10)
        erro_msg.setTextColor("red")
        erro_msg.draw(janela)

    return botao_voltar
