from graphics import *

def desenhar_tela_cadastro(janela):
    """
    Desenha a tela de cadastro na janela existente.
    :param janela: Instância de GraphWin.
    :return: Retorna os inputs (nome, email, senha), o botão de enviar e o botão de voltar.
    """
    # Limpa a janela
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem de fundo da tela de cadastro
    tela_cadastro = Image(Point(400, 300), "assets/tela_cadastro.png")
    tela_cadastro.draw(janela)

    # Desenhar campos de entrada de texto
    nome_input = Entry(Point(185.0, 229.0), 20)  # Campo para nome
    nome_input.draw(janela)

    email_input = Entry(Point(173.0, 353.0), 20)  # Campo para email
    email_input.draw(janela)

    senha_input = Entry(Point(183.0, 470.0), 20)  # Campo para senha
    senha_input.draw(janela)

    # Desenhar o botão de enviar cadastro
    botao_enviar = Rectangle(Point(93.0, 520.0), Point(296.0, 578.0))
    botao_enviar.setOutline("")
    botao_enviar.draw(janela)


    # Desenhar o botão "Voltar"
    botao_voltar = Rectangle(Point(714.0, 560.0), Point(800.0, 600.0))  # Retângulo correto
    botao_voltar.setFill("gray")  # Cor visível para o botão
    botao_voltar.setOutline("black")
    botao_voltar.draw(janela)

    # Texto centralizado no botão "Voltar"
    texto_voltar = Text(Point(757.5, 580.0), "Voltar")  # Centraliza o texto
    texto_voltar.setSize(10)  # Tamanho do texto
    texto_voltar.setStyle("bold")
    texto_voltar.draw(janela)

    return nome_input, email_input, senha_input, botao_enviar, botao_voltar
