def myAtoi(str: str) -> int:
    if len(str) == 0:
        return 0
    flag = True
    str = str.strip()
    start = 0
    if str[0] == '-':
        flag = False
        start += 1
    answer = 0
    while (len(str) > start and str[start].isnumeric()):
        answer = answer * 10 + int(str[start])
        start += 1

    if flag == False:
        answer *= -1
    if answer < -2147483648:
        return -2147483648
    if answer > 2147483647:
        return 2147483647
    return answer