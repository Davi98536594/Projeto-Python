def dec_pra_octal(numero):
    if numero < 0:
        return "Número inválido"
    elif numero == 0:
        return "0"
    else:
        octal = ""
        while numero > 0:
            resto = numero % 8
            octal = str(resto) + octal
            numero //= 8
        return octal
num_decimal = int(input("Digite um número decimal: "))
print("O número octal correspondente é:", dec_pra_octal(num_decimal))
