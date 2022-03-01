def subtractProductAndSum(n: int):
    sum = 0
    product = 1
    digit = 0
    while (n != 0):
        digit = n % 10
        sum = sum + digit
        product = product * digit
        n = n // 10
    return product - sum