#conversor de decimal para octal
def decimal_tranformando_octal(numero):
    if numero == 0:
        return 0
    else:
        resultado = ""
        while numero != 0:
            resto = numero % 8
            resultado = str(resto) + resultado
            numero = numero // 8
            return resultado
numero = int(input("Digite um número intero decial para transformar em octal: "))
octal = decimal_tranformando_octal(numero)
print("{} convertido em octal é {}".format(numero, octal))
