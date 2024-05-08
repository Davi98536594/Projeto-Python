binario = input("Digite um número binário: ")

decimal = 0
potencia = 0


is_valid = True


index = 0
while index < len(binario):
    char = binario[index]
    if char == '0' or char == '1':
        decimal = decimal * 2 + int(char)
    else:
        is_valid = False
        break
    index += 1


if is_valid:
   
    if decimal == 0:
        hexadecimal = '0'
    else:
        hexadecimal = ''
        while decimal > 0:
            remainder = decimal % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                
                hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
            decimal //= 16
            
    print("O número hexadecimal correspondente é:", hexadecimal)
else:
    print("Entrada inválida. Por favor, digite apenas números binários (0 e 1).")
