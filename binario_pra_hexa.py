def binario_para_hexadecimal(num_bin):
    numero_decimal = int(num_bin, 2)  
    hexadecimal = hex(numero_decimal).upper()[2:]  
    return hexadecimal

num_bin = input("Digite um número binário: ")
print("O número hexadecimal correspondente é:", binario_para_hexadecimal(num_bin))
