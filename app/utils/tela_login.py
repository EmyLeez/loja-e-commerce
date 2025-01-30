from graphics import *

def desenhar_tela_login(janela):
    """
    Desenha a tela de login na janela existente.
    :param janela: Instância de GraphWin.
    :return: Retorna os objetos de entrada (email, senha), o botão de login e o botão voltar.
    """
    # Limpa a janela
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem de fundo da tela de login
    tela_login = Image(Point(400, 300), "assets/tela_login.png")
    tela_login.draw(janela)

    # Desenhar campos de entrada de texto
    email_input = Entry(Point(153.0, 165.0), 20)  # Largura do campo = 20 caracteres
    email_input.draw(janela)

    senha_input = Entry(Point(153.0, 282.0), 20)  # Largura do campo = 20 caracteres
    senha_input.draw(janela)

    # Desenhar o botão de login (transparente)
    botao_login = Rectangle(Point(93.0, 339.0), Point(297.0, 395.0))
    botao_login.setOutline("")  # Botão transparente
    botao_login.draw(janela)

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

    return email_input, senha_input, botao_login, botao_voltar
