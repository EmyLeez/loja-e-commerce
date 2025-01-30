from graphics import *

def desenhar_tela_consulta_produto(janela):
    """
    Desenha a tela de consulta de produto e adiciona um campo de entrada e botão de pesquisa.
    :param janela: Instância de GraphWin.
    :return: Retorna o campo de entrada, botão de consulta e botão de voltar.
    """
    # Limpa a tela antes de desenhar a nova
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem da tela de consulta
    tela_consulta = Image(Point(400, 300), "assets/tela_consulta.png")
    tela_consulta.draw(janela)

    # Criar campo de entrada para o ID do produto
    input_id = Entry(Point(222.0, 244.0), 15)  # Campo centralizado na posição desejada
    input_id.draw(janela)

    # Criar botão "Consultar" (retângulo transparente)
    botao_consultar = Rectangle(Point(96.0, 300.0), Point(324.0, 356.0))
    botao_consultar.setOutline("")  # Botão invisível
    botao_consultar.draw(janela)

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

    return input_id, botao_consultar, botao_voltar
