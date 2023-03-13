from lib.interface import menu, cabecalho, leiaInt
from lib.arquivo import ArquivoExiste, criarArquivo, lerarquivo, cadastrar
from time import sleep

arq = 'pessoas cadastradas.txt'

if not ArquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('QUal o Nome da pessoa: '))
        idade = leiaInt('Qual a idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\033[33mDesligando o Sistema ... Volte Sempre!\033[m')
        break
    else:
        print('\033[31mERRO, Digite uma opção válida\033[m')
    sleep(2)
