def binario_para_octal(binario):
    decimal = int(binario, 2)
    octal = oct(decimal)
    return octal[2:]  #

binario = input("Digite um número binário para converter em octal: ")
resultado_octal = binario_para_octal(binario)
print(f'Binário: {binario} -> Octal: {resultado_octal}')
