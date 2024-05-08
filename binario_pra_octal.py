
binario = input("Digite um número binário: ")


if not all(char in '01' for char in binario):
    print("Entrada inválida. Por favor, digite apenas números binários (0 e 1).")
else:
    
    decimal = 0
    potencia = 0
    binario_int = int(binario)  

    while binario_int > 0:
        ultimo_digito = binario_int % 10
        decimal += ultimo_digito * (2 ** potencia)
        potencia += 1
        binario_int //= 10

    
    if decimal == 0:
        octal = '0'
    else:
        octal = ''
        while decimal > 0:
            octal = str(decimal % 8) + octal
            decimal //= 8

    
    print("O número octal correspondente é:", octal)
