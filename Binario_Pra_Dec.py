def binario_para_decimal(binario):
    n = len(binario)
    decimal = 0
    for i in range(n):
        digito = int(binario[i])
        decimal += digito * (2 ** (n - i - 1))
    return decimal
