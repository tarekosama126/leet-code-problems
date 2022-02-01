def isPalindrome(s: str) -> bool:
    s = s.lower()
    left = 0
    right = len(s) - 1
    while (left < right):
        while (left < right and ((s[left].isalpha() or s[left].isnumeric()) == False)):
            left += 1
        while (left < right and ((s[right].isalpha() or s[right].isnumeric()) == False)):
            right -= 1
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True