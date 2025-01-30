import time
from graphics import *

def desenhar_tela_menu(janela):
    """
    Desenha a tela do menu na janela existente e adiciona botões transparentes.
    :param janela: Instância de GraphWin.
    :return: Retorna os botões desenhados.
    """
    # Limpa a janela completamente antes de desenhar a nova tela
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem de fundo da tela de menu
    tela_menu = Image(Point(400, 300), "assets/tela_menu.png")
    tela_menu.draw(janela)

    # Criando botões transparentes com base nas coordenadas fornecidas
    botao_cadastrar_livro = Rectangle(Point(76.0, 148.0), Point(303.0, 204.0))
    botao_cadastrar_livro.setOutline("")  # Remove borda para tornar invisível
    botao_cadastrar_livro.draw(janela)

    botao_verificar_estoque = Rectangle(Point(76.0, 225.0), Point(304.0, 281.0))
    botao_verificar_estoque.setOutline("")
    botao_verificar_estoque.draw(janela)

    botao_gerar_lista = Rectangle(Point(76.0, 302.0), Point(304.0, 358.0))
    botao_gerar_lista.setOutline("")
    botao_gerar_lista.draw(janela)

    botao_comprar_livros = Rectangle(Point(76.0, 378.0), Point(304.0, 435.0))
    botao_comprar_livros.setOutline("")
    botao_comprar_livros.draw(janela)

    print("Tela do Menu carregada. Clique nos botões para testar.")

    return botao_cadastrar_livro, botao_verificar_estoque, botao_gerar_lista, botao_comprar_livros
