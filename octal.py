def octal_to_decimal(octal_str):
    if '.' in octal_str:
        integer_part, fractional_part = octal_str.split('.')
    else:
        integer_part, fractional_part = octal_str, '0'

    decimal_integer = int(integer_part, 8)
    decimal_fraction = sum(int(digit) * 8 ** -(index + 1) for index, digit in enumerate(fractional_part))

    return decimal_integer #+ decimal_fraction


def hex_to_decimal(hex_str):
        decimal = 0
        hex_str = hex_str[::-1]  # Reverse the hex string
        for i in range(len(hex_str)):
            digit = hex_str[i]
            if digit.isdigit():
                decimal += int(digit) * (16 ** i)
            else:
                decimal += (ord(digit.upper()) - 55) * (16 ** i)

        return decimal
