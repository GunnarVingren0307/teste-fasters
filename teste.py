import os
import platform

lista = ["topico 1", "topico 2", "topico 3", "topico 4", "topico 5"]


def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


while True:
    print("Selecione uma opção")
    print("(1) Cadastrar novo tópico,\n(2) Listar todos,\n(3) Selecionar específico,\n(4) deletar todos,\n(5) deletar especifico,\n(6) Tópicos em intervalor\n(7) sair")

    opcao = input("Digite o número da opcão desejada: ")

    match opcao:
        case "1":
            limpar_tela()
            item = input("Digite o item que deseja cadastrar: ")
            lista.append(item)
            print("Item cadastrado com sucesso!")
            input("Aperte enter para continuar...")
            limpar_tela()
            continue
        case "2":
            limpar_tela()
            if len(lista) == 0:
                print(f"A lista está vazia: {lista}")
                input("Aperte enter para retornar ao menu\n")
                limpar_tela()
                continue
            else:
                print("Aqui estão todos os tópicos: ")
                print(lista)
                input("Aperte enter para retornar ao menu\n")
                limpar_tela()
                continue
        case "3":
            if len(lista) == 0:
                print(f"A lista está vazia: {lista}")
                input("Aperte enter para retornar ao menu\n")
                limpar_tela()
                continue
            while True:
                try:
                    limpar_tela()
                    item = int(
                        input("Digite a posição do item que deseja selecionar: \n"))
                    posicao = lista[item]
                    print(
                        f"O item selecionado na posição {item}: \n {posicao}.")
                    input("Aperte enter para retornar ao menu\n")
                    limpar_tela()
                    break
                except (IndexError, ValueError):
                    print(
                        "Índice inválido. Digite um valor inteiro entre 0 e", len(lista) - 1)
                    input("Aperte enter para tentar novamente...\n")
                    limpar_tela()
        case "4":
            limpar_tela()
            if len(lista) == 0:
                print(f"A lista já está vazia: {lista}")
                input("Aperte enter para retornar ao menu\n")
                limpar_tela()
                continue
            else:
                resposta = input(
                    "Tem certeza que deseja continuar? 'S' para Sim e 'N' para não: ")
                if resposta == "S" or resposta == "s":
                    lista.clear()
                    print("Todos os items foram deletados com sucesso!")
                    input("Aperte enter para retornar ao menu\n")
                    limpar_tela()
                    continue
                elif resposta == "N" or resposta == "n":
                    limpar_tela()
                    input(
                        "Lista não foi deletada\nAperte enter para retornar ao menu")
                    limpar_tela()
                else:
                    print("Insira uma resposta válida!")
                    input("Aperte enter para inserir novamente...")
                    limpar_tela()
        case "5":
            if len(lista) == 0:
                print(f"A lista está vazia: {lista}")
                input("Aperte enter para retornar ao menu\n")
                limpar_tela()
                continue
            while True:
                try:
                    limpar_tela()
                    itemQueVaiSerDeletado = int(
                        input("Digite o índice que deseja deletar: "))

                    confirmacao = input(
                        f"tem certeza que deseja excluir este item? {lista[itemQueVaiSerDeletado]} 'S' para sim e 'N' para não: ")
                    if confirmacao == "S" or confirmacao == "s":
                        del lista[itemQueVaiSerDeletado]
                        input(
                            "item deletado com sucesso. Aperte enter para concluir...")
                        limpar_tela()
                        break
                    elif confirmacao == "N" or confirmacao == "n":
                        input("item NÃO foi deletado. Aperte enter para concluir...")
                        limpar_tela()
                        break
                    else:
                        input(
                            "Insira uma resposta válida. Aperte enter para concluir...")
                        limpar_tela()
                except (IndexError, ValueError):
                    print("Índice inválido. Digite um valor inteiro entre 0 e",
                          len(lista) - 1)
                    input("Aperte enter para tentar novamente...\n")
                    limpar_tela()
        case "6":
            if len(lista) == 0:
                print(f"A lista está vazia: {lista}")
                input("Aperte enter para retornar ao menu\n")
                limpar_tela()
                continue
            while True:
                try:
                    limpar_tela()
                    limiteInferior = int(
                        input("Digite o primeiro valor do intervalo que deseja selecionar: "))
                    limiteSuperior = int(
                        input("Digite o segundo valor do intervalo que deseja selecionar: "))
                    if limiteInferior > limiteSuperior:
                        print(
                            "não é permitido um valor inferior para a primeira opção")
                    else:
                        for i in range(limiteInferior, limiteSuperior + 1):
                            print("Posição {}:  {}.".format(i, lista[i]))
                    input("Aperte enter para retornar ao menu\n")
                    limpar_tela()
                    break
                except (IndexError, ValueError):
                    print("Índice inválido. Digite um valor inteiro entre 0 e",
                          len(lista) - 1)
                    input("Aperte enter para tentar novamente...\n")
                    limpar_tela()
        case "7":
            escolha = input(
                "Aperte 'f' para fechar o programa ou 'C' para continuar: ")
            if escolha == "f" or escolha == "F":
                input("Fechando o programa, aperte enter para concluir...")
                limpar_tela()
                break
            elif escolha == "c" or escolha == "C":
                input("Aperte enter para retornar ao menu")
                limpar_tela()
            else:
                print("Insira um valor válido!")
                limpar_tela()
        case _:
            print("Insira um valor válido")
            input("Aperte enter para retornar")
            limpar_tela()
