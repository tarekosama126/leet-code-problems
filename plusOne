def plusOne(digits):
    i = len(digits) - 1
    line = ""
    while (i >= 0):
        if (digits[i] < 9):
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            line = str(digits[i]) + line
            i -= 1
    line = str(1) + line
    return list(line)