def binario_para_hexadecimal(binario):
    decimal = int(binario, 2)
    hexadecimal = hex(decimal)
    return hexadecimal[2:]  

binario = input("Digite um número binário para converter em hexadecimal: ")
resultado_hexadecimal = binario_para_hexadecimal(binario)
print(f'Binário: {binario} -> Hexadecimal: {resultado_hexadecimal}')
