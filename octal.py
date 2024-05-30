def octal_to_decimal(octal_str):
    if '.' in octal_str:
        integer_part, fractional_part = octal_str.split('.')
    else:
        integer_part, fractional_part = octal_str, '0'

    decimal_integer = int(integer_part, 8)
    decimal_fraction = sum(int(digit) * 8 ** -(index + 1) for index, digit in enumerate(fractional_part))

    return decimal_integer + decimal_fraction
