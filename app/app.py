from graphics import *
import time
from utils.tela_inicial import desenhar_tela_inicial
from utils.tela_login import desenhar_tela_login
from utils.tela_cadastro import desenhar_tela_cadastro
from utils.verificar_login import verificar_login
from utils.cadastrar_usuario import cadastrar_usuario 
from utils.tela_menu import desenhar_tela_menu
from utils.tela_cadastro_livros import desenhar_tela_cadastro_livros
from utils.salvar_estoque import salvar_estoque
from utils.tela_estoque import desenhar_tela_estoque
from utils.gerar_html_estoque import gerar_html_estoque
from utils.tela_consulta_produto import desenhar_tela_consulta_produto
from utils.consultar_produto import consultar_produto
from utils.tela_atualizar_estoque import desenhar_tela_atualizar_estoque
from utils.atualizar_estoque import atualizar_estoque


def main():
    # Cria a janela principal (800x600)
    janela = GraphWin("Aplicativo", 800, 600)

    # Variável para controlar a tela atual
    tela_atual = "inicial"

    # Exibe a tela inicial e pega os botões desenhados
    botao_login, botao_cadastro = desenhar_tela_inicial(janela)

    # Inicializa variáveis dos campos e botões das telas
    email_input = senha_input = botao_login_tela = botao_voltar = None
    nome_input = email_cadastro_input = senha_cadastro_input = botao_enviar_cadastro = botao_voltar_cadastro = None
    botao_cadastrar_livro = botao_verificar_estoque = botao_gerar_lista = botao_comprar_livros = None
    input_id = input_nome = input_quantidade = input_preco = botao_cadastrar_livro = botao_voltar_cadastro_livros = mensagem = None

    while True:
        try:
            # Captura o clique do usuário
            clique = janela.getMouse()
            x, y = clique.getX(), clique.getY()

            if tela_atual == "inicial":
                # Verificar se clicou no botão Login
                if 92.0 <= x <= 296.0 and 241.0 <= y <= 299.0:
                    print("Clicou em Login")
                    email_input, senha_input, botao_login_tela, botao_voltar = desenhar_tela_login(janela)
                    tela_atual = "login"  # Atualiza a tela atual
                    continue

                # Verificar se clicou no botão Cadastro
                elif 92.0 <= x <= 296.0 and 338.0 <= y <= 395.0:
                    print("Clicou em Cadastro")
                    nome_input, email_cadastro_input, senha_cadastro_input, botao_enviar_cadastro, botao_voltar_cadastro = desenhar_tela_cadastro(janela)
                    tela_atual = "cadastro"  # Atualiza a tela atual
                    continue

            elif tela_atual == "login":
                # Verificar se clicou no botão de login na tela de login
                if 93.0 <= x <= 297.0 and 339.0 <= y <= 395.0:
                    print("Login clicado para login")
                    email = email_input.getText().strip()  # Obtém o texto inserido no campo de email
                    senha = senha_input.getText().strip()  # Obtém o texto inserido no campo de senha
                    print(f"Email: {email}")
                    print(f"Senha: {senha}")

                    # Remover mensagem anterior antes de desenhar a nova
                    for item in janela.items[:]:
                        if isinstance(item, Text):
                            item.undraw()

                    # Criar mensagem na posição correta (189.0, 420.0)
                    mensagem = Text(Point(189.0, 420.0), "")
                    mensagem.setSize(8)  # Tamanho do texto
                    mensagem.setTextColor("black")  # Texto preto
                    mensagem.setStyle("bold")
                                
                    if verificar_login(email, senha):
                        print("Login bem-sucedido!")  # Aqui futuramente podemos redirecionar para outra tela
                        mensagem.setText("Login sucedido, você será redirecionado para o menu")
                        mensagem.draw(janela)

                        time.sleep(2)  # Aguarda 2 segundos
                        desenhar_tela_menu(janela)  # Redireciona para o menu
                        tela_atual = "menu"  # Atualiza o estado da tela
                    else:
                        print("Email ou senha incorretos.")
                        mensagem.setText("Credenciais incorretas")
                        mensagem.draw(janela)
                    continue

                # Verificar se clicou no botão Voltar
                if 714.0 <= x <= 800.0 and 560.0 <= y <= 600.0:
                    print("Clicou em Voltar")
                    botao_login, botao_cadastro = desenhar_tela_inicial(janela)
                    tela_atual = "inicial"  # Volta para a tela inicial
                    continue

            elif tela_atual == "cadastro":
                # Verificar se clicou no botão Enviar
                if 93.0 <= x <= 296.0 and 520.0 <= y <= 578.0:
                    print("Enviar")
                    nome = nome_input.getText()  # Obtém o texto do campo Nome
                    email = email_cadastro_input.getText()  # Obtém o texto do campo Email
                    senha = senha_cadastro_input.getText()  # Obtém o texto do campo Senha
                    print(f"Nome: {nome}")
                    print(f"Email: {email}")
                    print(f"Senha: {senha}")
                    
                    # Remover mensagem anterior antes de desenhar a nova
                    for item in janela.items[:]:
                        if isinstance(item, Text):
                            item.undraw()

                    # Criar mensagem na posição correta (193.0, 504.0)
                    mensagem = Text(Point(193.0, 504.0), "")
                    mensagem.setSize(8)
                    mensagem.setTextColor("black")
                    mensagem.setStyle("bold")

                    resultado = cadastrar_usuario(nome, email, senha)

                    if resultado == "Usuário cadastrado, você será redirecionado.":

                        mensagem.setText(resultado)
                        mensagem.draw(janela)

                        time.sleep(2)  # Aguarda 2 segundos
                        desenhar_tela_menu(janela)  # Redireciona para o menu
                        tela_atual = "menu"  # Atualiza o estado da tela

                    else:
                        mensagem.setText(resultado)
                        mensagem.draw(janela)

                    continue

                # Verificar se clicou no botão Voltar
                if 714.0 <= x <= 800.0 and 560.0 <= y <= 600.0:
                    print("Clicou em Voltar")
                    botao_login, botao_cadastro = desenhar_tela_inicial(janela)
                    tela_atual = "inicial"  # Volta para a tela inicial
                    continue

            elif tela_atual == "menu":
                # Verificar qual botão foi clicado
                if 76.0 <= x <= 303.0 and 148.0 <= y <= 204.0:
                    print("Clicou em: Cadastrar Livro")
                    input_id, input_nome, input_quantidade, input_preco, botao_cadastrar_livro, botao_voltar_cadastro_livros = desenhar_tela_cadastro_livros(janela)
                    
                    # Criar mensagem na posição correta (178, 570) SOMENTE QUANDO ENTRAR NA TELA
                    mensagem = Text(Point(178.0, 570.0), "")
                    mensagem.setSize(8)
                    mensagem.setTextColor("black")
                    mensagem.setStyle("bold")
                    mensagem.draw(janela)
                    
                    tela_atual = "cadastro_livros"
                    continue

                if 76.0 <= x <= 304.0 and 225.0 <= y <= 281.0:
                    print("Clicou em: Atualizar Estoque")
                    botao_voltar, botao_atualizar, campos = desenhar_tela_atualizar_estoque(janela)
                    tela_atual = "atualizar_estoque"
                    continue

                if 76.0 <= x <= 304.0 and 302.0 <= y <= 358.0:
                    print("Clicou em: Gerar Lista")
                    botao_voltar_estoque = desenhar_tela_estoque(janela)
                    tela_atual = "estoque"
                    gerar_html_estoque()
                    continue

                if 76.0 <= x <= 304.0 and 378.0 <= y <= 435.0:
                    print("Clicou em: Consultar Produto")
                    input_id, botao_consultar, botao_voltar = desenhar_tela_consulta_produto(janela)
                    tela_atual = "consulta_produto"
                    continue
            
            elif tela_atual == "cadastro_livros":
                # Verificar se clicou no botão "Cadastrar Livro"
                if 72.0 <= x <= 301.0 and 496.0 <= y <= 553.0:
                    print("Cadastrar Livro")

                    if None in (input_id, input_nome, input_quantidade, input_preco, mensagem):
                        print("Erro: Campos de entrada não foram inicializados corretamente.")
                        continue

                    # Obter os valores dos inputs
                    id_livro = input_id.getText().strip()
                    nome_livro = input_nome.getText().strip()
                    quantidade_livro = input_quantidade.getText().strip()
                    preco_livro = input_preco.getText().strip()
                    
                    print(id_livro)
                    print(nome_livro)
                    print(quantidade_livro)
                    print(preco_livro)
                    
                    # Criar mensagem na posição correta (193.0, 504.0)
                    mensagem = Text(Point(178.0, 570.0), "")
                    mensagem.setSize(8)
                    mensagem.setTextColor("black")
                    mensagem.setStyle("bold")
                    
                    for item in janela.items[:]:
                        if isinstance(item, Text):
                            item.undraw()

                    if not id_livro or not nome_livro or not quantidade_livro or not preco_livro:
                        # Remover mensagem anterior antes de desenhar a nova
                        print("Campos ausentes detectados")
                        mensagem.setText("Campos ausentes detectados.")
                        mensagem.draw(janela)
                        continue
                    else:
                        # Remover mensagem anterior antes de desenhar a nova
                        print("É possível cadastrar!")
                        resultado = salvar_estoque(id_livro, nome_livro, quantidade_livro, preco_livro)
                        print(resultado)
                        mensagem.setText(resultado)
                        mensagem.draw(janela)
                        continue


                # Verificar se clicou no botão "Voltar"
                if 714.0 <= x <= 800.0 and 560.0 <= y <= 600.0:
                    print("Clicou em Voltar")
                    botao_cadastrar_livro, botao_verificar_estoque, botao_gerar_lista, botao_comprar_livros = desenhar_tela_menu(janela)
                    tela_atual = "menu"
                    continue

            elif tela_atual == "estoque":
                # Verificar se clicou no botão "Voltar"
                if 714.0 <= x <= 800.0 and 560.0 <= y <= 600.0:
                    print("Clicou em Voltar")
                    botao_cadastrar_livro, botao_verificar_estoque, botao_gerar_lista, botao_comprar_livros = desenhar_tela_menu(janela)
                    tela_atual = "menu"
                    continue
            
            elif tela_atual == "consulta_produto":
                # Verificar se clicou no botão "Consultar"
                if 96.0 <= x <= 324.0 and 300.0 <= y <= 356.0:
                    print("Clicou em Consultar")

                    # Captura o ID inserido no campo de entrada
                    id_produto = input_id.getText().strip()

                    # Limpa mensagens anteriores
                    for item in janela.items[:]:
                        if isinstance(item, Text):
                            item.undraw()

                    if id_produto:
                        # Chama a função para consultar o produto
                        consultar_produto(janela, id_produto)
                    else:
                        # Se o campo estiver vazio, exibe um erro
                        mensagem_erro = Text(Point(590.0, 276.0), "Digite um ID válido")
                        mensagem_erro.setSize(10)
                        mensagem_erro.setTextColor("red")
                        mensagem_erro.draw(janela)

                    continue

                # Verificar se clicou no botão "Voltar"
                if 714.0 <= x <= 800.0 and 560.0 <= y <= 600.0:
                    print("Clicou em Voltar")
                    botao_cadastrar_livro, botao_verificar_estoque, botao_gerar_lista, botao_comprar_livros = desenhar_tela_menu(janela)
                    tela_atual = "menu"
                    continue
                    
            elif tela_atual == "atualizar_estoque":
                # Verificar se clicou no botão "Atualizar Estoque"
                if 300.0 <= x <= 500.0 and 500.0 <= y <= 550.0:
                    print("Clicou em Atualizar Estoque")

                    resultado = atualizar_estoque(campos)
                    print(resultado)

                    # Exibir mensagem de sucesso na tela
                    mensagem_sucesso = Text(Point(400.0, 470.0), resultado)
                    mensagem_sucesso.setSize(10)
                    mensagem_sucesso.setTextColor("green")
                    mensagem_sucesso.draw(janela)
                    continue

                # Verificar se clicou no botão "Voltar"
                if 714.0 <= x <= 800.0 and 560.0 <= y <= 600.0:
                    print("Clicou em Voltar")
                    botao_cadastrar_livro, botao_verificar_estoque, botao_gerar_lista, botao_comprar_livros = desenhar_tela_menu(janela)
                    tela_atual = "menu"
                    continue

            print(f"Clique detectado em: ({x}, {y})")

        except GraphicsError:
            print("Janela fechada.")
            break
        
        except Exception as e:
            print(f"Erro inesperado: {e}")
            continue

    janela.close()

if __name__ == "__main__":
    main()
