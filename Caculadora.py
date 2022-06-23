while True:

    numero_1 = input('Digite um Numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador: ')
    sair = input('Deseja Sair [s]Sim [n]Não: ').lower()

    if not numero_1.isnumeric() or not numero_2.isnumeric():
        print("Voce precisa digitar um numero valido: ou sair ")
        continue

    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    if operador == '*':
        print(f'A multiplicação do numero: {numero_1}: e {numero_2}: Resultado = {numero_1 * numero_2}')
    elif operador == '+':
        soma = numero_1 + numero_2
        print(f'A Soma do numero: {numero_1}: e {numero_2}: Resultado = {numero_1 + numero_2}')
    elif operador == '-':
        print(f'A Subtração do numero: {numero_1}: e {numero_2}: Resultado = {numero_1 - numero_2}')
    elif operador == '/':
        print(f'A Divisão do numero: {numero_1}: e {numero_2}: Resultado = {numero_1 / numero_2}')

    else:
        print("Operação Invalida, Digite um opredaor valido")

    if sair =='s':
        break
