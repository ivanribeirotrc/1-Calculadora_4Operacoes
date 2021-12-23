# Autor: Ivan Ribeiro
# Descrição: Primeira calculadora básica para treinos em python via pycharm
# Data: 22/12/2021

import time
import colorama
from colorama import Fore


def div():
    print('Divisão na area!!')
    n7 = float(input('Insira o primeiro valor: '))
    n8 = float(input('Insira o segundo valor: '))
    r4 = float(n7 / n8)
    print('O resultado da soma entre: ' + Fore.CYAN + ' %.2f' % n7 + Fore.RESET + ' e ' + Fore.CYAN + '%.2f' % n8 + Fore.RESET + ' foi de: ' + Fore.CYAN + '%.2f' % r4 + Fore.RESET)
    print(Fore.GREEN + '1' + Fore.RESET + '- Nova Subtração / ' + Fore.GREEN + '2' + Fore.RESET + '- Menu Inicial / ' + Fore.GREEN + '3' + Fore.RESET + '- Sair')
    m = int(input('Insira o opção desejada: '))
    if m == 1:
        div()
    elif m == 2:
        operacoes()
    elif m == 3:
        return


def multi():
    print('Multiplicando!!')
    n5 = float(input('Insira o primeiro valor: '))
    n6 = float(input('Insira o segundo valor: '))
    r3 = float(n5 * n6)
    print('O resultado da soma entre: ' + Fore.CYAN + ' %.2f' % n5 + Fore.RESET + ' e ' + Fore.CYAN + '%.2f' % n6 + Fore.RESET + ' foi de: ' + Fore.CYAN + '%.2f' % r3 + Fore.RESET)
    print(Fore.GREEN + '1' + Fore.RESET + '- Nova Subtração / ' + Fore.GREEN + '2' + Fore.RESET + '- Menu Inicial / ' + Fore.GREEN + '3' + Fore.RESET + '- Sair')
    m = int(input('Insira o opção desejada: '))
    if m == 1:
        multi()
    elif m == 2:
        operacoes()
    elif m == 3:
        return


def sub():
    print('Hora da subtração!!')
    n3 = float(input('Insira o primeiro valor: '))
    n4 = float(input('Insira o segundo valor: '))
    r2 = float(n3 - n4)
    print('O resultado da soma entre: ' + Fore.CYAN + ' %.2f' % n3 + Fore.RESET + ' e ' + Fore.CYAN + '%.2f' % n4 + Fore.RESET + ' foi de: ' + Fore.CYAN + '%.2f' % r2 + Fore.RESET)
    print(Fore.GREEN + '1' + Fore.RESET + '- Nova Subtração / ' + Fore.GREEN + '2' + Fore.RESET + '- Menu Inicial / ' + Fore.GREEN + '3' + Fore.RESET + '- Sair')
    m = int(input('Insira o opção desejada: '))
    if m == 1:
        sub()
    elif m == 2:
        operacoes()
    elif m == 3:
        return


def soma():
    print('Vamos as somas!!')
    n1 = float(input('Insira o primeiro valor: '))
    n2 = float(input('Insira o segundo valor: '))
    r = float(n1 + n2)
    print('O resultado da soma entre: ' + Fore.CYAN + ' %.2f' % n1 + Fore.RESET + ' e ' + Fore.CYAN + '%.2f' % n2 + Fore.RESET + ' foi de: ' + Fore.CYAN + '%.2f' % r + Fore.RESET)
    print(Fore.GREEN + '1' + Fore.RESET + '- Nova Soma / ' + Fore.GREEN + '2' + Fore.RESET + '- Menu Inicial / ' + Fore.GREEN + '3' + Fore.RESET + '- Sair')
    m = int(input('Insira o opção desejada: '))
    if m == 1:
        soma()
    elif m == 2:
        operacoes()
    elif m == 3:
        return


def operacoes():
    print('Operações: ' + Fore.GREEN + '1' + Fore.RESET + '- Adição / ' + Fore.GREEN + '2' + Fore.RESET + '- Subtração / ' + Fore.GREEN + '3' + Fore.RESET + '- Multiplicação / ' + Fore.GREEN + '4' + Fore.RESET + '- Divisão / ')
    op = int(input('Qual operação deseja? '))
    if op == 1:
        soma()
    elif op == 2:
        sub()
    elif op == 3:
        multi()
    elif op == 4:
        div()
    else:
        print('Favor selecione uma operação que seja VALIDA!')
        operacoes()


def main():
    nome = input('Informe seu nome: ')
    print('Seu nome é:' + Fore.RED + ' %s' % nome + Fore.RESET)
    nome_conf = int(input('O nome está correto? Sim = ' + Fore.GREEN + '1' + Fore.RESET + ' / Não = ' + Fore.GREEN + '2 ' + Fore.RESET))
    if nome_conf == 1:
        print('Então vamos aos calculos' + Fore.RED + ' %s' % nome + Fore.RESET)
        operacoes()
    else:
        main()


print('Calculadora Básica by ' + Fore.RED + 'Ivan Ribeiro' + Fore.RESET)
colorama.init()
time.sleep(1)
print(Fore.YELLOW + 'Iniciando')
time.sleep(1)
print(Fore.YELLOW + 'Carregando o programa')
time.sleep(1)
print(Fore.YELLOW + 'Finalizando verificação' + Fore.RESET)
time.sleep(1)
main()
