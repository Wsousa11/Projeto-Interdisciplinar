print('='*51)
print('Calculadora Conversora de Sistemas de Numeração')
print('='*51)

while True:
    print('Escolha para qual sistema de numeração você quer converter o número decimal: ')
    funcao = input('[1] Binario, [2] Octadecimal, [3] Hexadecimal, [4] Sair : ')
    print()

    if funcao != '1' and funcao != '2' and funcao != '3' and funcao != '4':
        print('Opção invalida ! Escolha uma opção disponível !!!')
        print()
    elif funcao == '4':
        print('Obrigado por utilizar nosso produto!')
        break
    else:
        print('Conversão da base decimal para as bases binário, hexadecimal e octadecimal.')
        num = int(input('Digite um número decimal: '))
        x = num
        
        if num <= 0: print(), print('ERRO - Digite um número inteiro e positivo !!!'), print()    
        
        else:
            if funcao == '1':
                resultado = ''
                base = 'Binario'
                while num != 0:
                    r = num % 2
                    resultado = str(r) + resultado
                    num = num//2

            elif funcao == '2':
                resultado = ''
                base = 'Octadecimal'
                while num != 0:
                    r = num % 8
                    resultado = str(r) + resultado
                    num = num // 8

            elif funcao == '3':
                lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
                resultado = ''
                base = 'hexadecimal'
                while num != 0:
                    r = num % 16
                    resultado = f'{lista[r]}{resultado}'
                    num = num // 16
            print()
            print(f'O decimal {x} equivale a {resultado} na base {base}.')
            print()
