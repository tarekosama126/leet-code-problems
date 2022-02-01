from typing import List
def stringShift(s: str, shift: List[List[int]]):
    absolute = 0
    for i in shift:
        if i[0] == 0:
            absolute -= i[1]
        else:
            absolute += i[1]
    print(absolute)
    if absolute == 0:
        return s
    elif absolute < 0:
        absolute = abs(absolute) % len(s)
        if absolute == 0:
            return s
        first = s[:absolute]
        second = s[absolute:]
        return second + first
    else:
        absolute = absolute % len(s)
        if absolute == 0:
            return s
        first = s[:len(s) - absolute]
        second = s[len(s) - absolute:]
        return second + first