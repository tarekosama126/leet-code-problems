def reverse(x):
    negative = False
    reversed = 0
    if x < 1:
        negative = True
        x = abs(x)
    while (x != 0):
        lastdigit = x % 10
        reversed = (reversed * 10) + lastdigit
        x = x // 10
    if negative:
        reversed *= -1

    return reversed