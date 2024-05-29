def decimal_to_hex(n):
    hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    result = []
    while n > 0:
        result.append(hex[n % 16])
        n = n // 16
    result.reverse()
    return ''.join(result)
