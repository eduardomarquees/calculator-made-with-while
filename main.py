#Calculadora feita com WHILE

while True:
    number1 = input('Digite um valor: ')
    number2 = input('Digite um valor: ')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multipilicar')
    print('4. Dividir')
    print('5. Sair')
    operacao = input('Digite uma operação:  ')

    numbervalid = None
    number1_float = 0
    number2_float = 0

    try:
        number1_float = float(number1)
        number2_float = float(number2)
        numbervalid = True
    except:
        numbervalid = None

#Condições
    if numbervalid is None:
        print('Digite somente um valor...')
        continue

    operacaoValidas = '1,2,3,4,5'

    if operacao not in operacaoValidas:
        print('Operador Inválido, tente colocar somente um operador')
        continue

    if operacao == '5':
        print('Saindo...')
        break

    # if len(operacao) > 1:
    #     print('Digite somente um operador!')
    #     continue

    print('Realizando sua conta, confira abaixo...')

    if operacao == '1':
        print(number1_float + number2_float)
    elif operacao == '2':
        print(number1_float - number2_float)
    elif operacao == '3':
        print(number1_float * number2_float)
    # elif operacao == '4':
    #     print(number1_float / number2_float)
    elif number2_float != 0:
        print(number1_float / number2_float)
    else:
        print('Não pode ser dividido por zero')



