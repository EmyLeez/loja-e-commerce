import time
from graphics import *

def desenhar_tela_cadastro_livros(janela):
    """
    Desenha a tela de cadastro de livros e adiciona campos de entrada.
    """
    # Limpa a janela antes de desenhar a nova tela
    for item in janela.items[:]:
        item.undraw()
    janela.update()

    # Carrega a imagem de fundo da tela de cadastro de livros
    tela_cadastro_livros = Image(Point(400, 300), "assets/tela_cadastro_livros.png")
    tela_cadastro_livros.draw(janela)

    # Criar campos de entrada
    input_id = Entry(Point(195.0, 238.0), 15)  
    input_id.draw(janela)

    input_nome = Entry(Point(258.0, 302.0), 15)  
    input_nome.draw(janela)

    input_quantidade = Entry(Point(300.0, 375.0), 10)  
    input_quantidade.draw(janela)

    input_preco = Entry(Point(250.0, 443.0), 15)  
    input_preco.draw(janela)

    # Criar botão "Cadastrar Livro" transparente
    botao_cadastrar = Rectangle(Point(72.0, 496.0), Point(301.0, 553.0))
    botao_cadastrar.setOutline("")  
    botao_cadastrar.draw(janela)

    # Criar botão "Voltar" no canto inferior direito
    botao_voltar = Rectangle(Point(714.0, 560.0), Point(800.0, 600.0))
    botao_voltar.setFill("gray")
    botao_voltar.setOutline("black")
    botao_voltar.draw(janela)

    # Texto centralizado no botão "Voltar"
    texto_voltar = Text(Point(757.5, 580.0), "Voltar")
    texto_voltar.setSize(10)
    texto_voltar.setStyle("bold")
    texto_voltar.draw(janela)

    print("Tela de Cadastro de Livros carregada.")

    return input_id, input_nome, input_quantidade, input_preco, botao_cadastrar, botao_voltar
