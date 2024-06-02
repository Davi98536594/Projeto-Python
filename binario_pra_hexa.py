def dec_pra_hexa(numero):
    if numero < 0:
        return "Número inválido"
    elif numero == 0:
        return "0"
    else:
        hexadecimal = ""
        while numero > 0:
            resto = numero % 16
            if resto < 10:
                hexadecimal = str(resto) + hexadecimal
            else:
                hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
            numero //= 16
        return hexadecimal

# Exemplo de uso:
num_dec = int(input("Digite um número decimal: "))
print("O número hexadecimal correspondente é:", dec_pra_hexa(num_dec))
