import os

def perguntas():
    pass

def respostas():
    pass
def processar_resposta(resposta, respostas, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}{respostas[0]}{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}{respostas[1]}{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}{respostas[2]}{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}{respostas[3]}{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo a PetShop')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - {perguntas[0]}{os.linesep}[2] - {perguntas[1]}{os.linesep}[3] - {perguntas[2]}{os.linesep}[4] - {perguntas[1]}{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()