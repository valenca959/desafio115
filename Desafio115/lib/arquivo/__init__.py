from Desafio115.lib.interface import cabecalho


def ArquivoExiste(nome):
    """
    > Função na qual verificará se tem o arquivo txt criado
    :param nome: nome do arquivo
    :return: retorna se existe o arquivo ou não
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    > irá criar o arquivo.txt caso não tenha
    :param nome: nome do arquivo
    :return:
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    """
    > irá abrir o arquivo e fazer sua leitura e retornar o arquivo
    :param nome: nome do arquivo
    :return: o arquivo txt
    """
    global a
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    """
    > cadastrar novas pessoas no arquivo txt
    :param arq: arquivo que será adicionado
    :param nome: nome da pessoa a cadastrar
    :param idade: idade da pessoa
    :return:
    """
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escerver os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
