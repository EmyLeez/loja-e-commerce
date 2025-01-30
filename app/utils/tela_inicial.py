from graphics import *

def desenhar_tela_inicial(janela):
    """
    Desenha a tela inicial na janela existente.
    :param janela: Instância de GraphWin.
    :return: Retorna os retângulos dos botões (Login e Cadastro).
    """
    # Limpa a janela caso já tenha algo desenhado
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem da tela inicial (800x600, centro 400, 300)
    tela_inicial = Image(Point(400, 300), "assets/inicial.png")
    tela_inicial.draw(janela)

    # Desenhar o botão Login (área clicável)
    # Aqui eu desenho o primeiro botão (botao_login) com as posições escolhidas,  ele é o primeiro botão que o úsuario ver na tela incial do projeto, que se chama Login.
    botao_login = Rectangle(Point(92.0, 241.0), Point(296.0, 299.0))
    botao_login.setOutline("")  # Transparente
    botao_login.draw(janela)

    # Desenhar o botão Cadastro (área clicável)
    botao_cadastro = Rectangle(Point(92.0, 338.0), Point(296.0, 395.0))
    botao_cadastro.setOutline("")  # Transparente
    botao_cadastro.draw(janela)

    return botao_login, botao_cadastro
