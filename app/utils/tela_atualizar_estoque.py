from graphics import *

def desenhar_tela_atualizar_estoque(janela):
    """
    Desenha a tela de atualização do estoque e cria campos de entrada preenchidos com os dados do CSV.
    :param janela: Instância de GraphWin.
    :return: Retorna o botão de voltar, botão de atualizar e os campos de entrada.
    """
    # Limpa a tela antes de desenhar a nova
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem da tela de atualização de estoque
    tela_atualizar = Image(Point(400, 300), "assets/tela_estoque.png")
    tela_atualizar.draw(janela)

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

    # Criar botão "Atualizar Estoque"
    botao_atualizar = Rectangle(Point(300.0, 500.0), Point(500.0, 550.0))
    botao_atualizar.setFill("green")
    botao_atualizar.setOutline("black")
    botao_atualizar.draw(janela)

    # Texto no botão "Atualizar"
    texto_atualizar = Text(Point(400.0, 525.0), "Atualizar Estoque")
    texto_atualizar.setSize(10)
    texto_atualizar.setStyle("bold")
    texto_atualizar.setTextColor("white")
    texto_atualizar.draw(janela)

    # Ler os itens do CSV e criar campos de entrada preenchidos
    caminho_csv = "csv/estoque.csv"
    campos = []  # Lista para armazenar os inputs

    try:
        with open(caminho_csv, mode="r", encoding="utf-8") as file:
            linhas = file.readlines()

            y_pos = 200  # Posição inicial para exibir os itens

            for i, linha in enumerate(linhas):
                if i == 0:
                    continue  # Ignorar o cabeçalho

                dados = linha.strip().split(";")
                if len(dados) == 4:
                    id_livro, nome, quantidade, preco = dados

                    # Criar campos de entrada preenchidos com os dados
                    input_id = Entry(Point(41.0, y_pos), 5)  # ID
                    input_id.setText(id_livro)
                    input_id.draw(janela)

                    input_nome = Entry(Point(214.0, y_pos), 20)  # Nome
                    input_nome.setText(nome)
                    input_nome.draw(janela)

                    input_qtd = Entry(Point(513.0, y_pos), 5)  # Quantidade
                    input_qtd.setText(quantidade)
                    input_qtd.draw(janela)

                    input_preco = Entry(Point(675.0, y_pos), 7)  # Preço
                    input_preco.setText(preco)
                    input_preco.draw(janela)

                    campos.append((input_id, input_nome, input_qtd, input_preco))

                    y_pos += 30  # Ajusta a linha para o próximo item

    except FileNotFoundError:
        erro_msg = Text(Point(400, 100), "Erro: Arquivo estoque.csv não encontrado.")
        erro_msg.setSize(10)
        erro_msg.setTextColor("red")
        erro_msg.draw(janela)

    return botao_voltar, botao_atualizar, campos
