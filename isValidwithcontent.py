def isValidwithcontent(s: str) -> bool:
    list = []
    for i in s:
        if i != '(' or i != '[' or i != '{' or i != ')' or i != ']' or i != '}':
            continue
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