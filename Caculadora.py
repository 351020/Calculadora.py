while True:
    num_1 = input("Digite Um número: ")
    num_2 = input("Digite outro número: ")
    operador = input('Digite o Operador: ')

    sair = input('Deseja sair? Digite [s]im ou [n]ão:  ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Número Invalido Digite o Número corretamente. ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operação Invalida ')

    if sair == 's':
        break