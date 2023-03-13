def linha(tam=42):
    return '-' * tam


def cabecalho(text):
    print(linha())
    print(text.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[35m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO, por favor, digite um número INTEIRO válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
