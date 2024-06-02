def bin_pra_octal(num_bin):
    num_dec = int(num_bin, 2)  
    octal = oct(num_dec).replace('0o', '') 
    return octal

num_bin = input("Digite um número binário: ")
print("O número octal correspondente é:", bin_pra_octal(num_bin))
