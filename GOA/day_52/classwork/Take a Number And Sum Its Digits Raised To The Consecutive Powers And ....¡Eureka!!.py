def sum_dig_pow(a, b):
    result = []
    for num in range(a, b + 1):
        digits = str(num)
        sum = 0
        for idx, digit in enumerate(digits):
            sum += int(digit) ** (idx + 1)
        if sum == num:
            result.append(num)
    return result