def converter_decimal_pra_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ""
    while decimal >0:
        resto = decimal %2
        binario =str(resto) + binario
        decimal = decimal // 2
    return binario
decimal = int(input("Digite um número "))
binario = converter_decimal_pra_binario(decimal)
print(f'O número decimal {decimal} em binario é: {binario}')
