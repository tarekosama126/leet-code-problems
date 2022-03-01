def isValidwithoutcontent(self, s: str) -> bool:
    list = []
    if len(s) % 2 == 1:
        return False
    for i in s:
        if i == '(' or i == '[' or i == '{':
            list.append(i)
        elif i == ')' and len(list) != 0:
            if list.pop(len(list) - 1) == '(':
                continue
            else:
                return False
        elif i == '}' and len(list) != 0:
            if list.pop(len(list) - 1) == '{':
                continue
            else:
                return False
        elif i == ']' and len(list) != 0:
            if list.pop(len(list) - 1) == '[':
                continue
            else:
                return False
    if len(list) == 0:
        return True
    else:
        return False