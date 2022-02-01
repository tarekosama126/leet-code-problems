def firstUniqChar(s: str) -> int:
    cache = {}
    if len(s) == 0:
        return -1
    for i in s:
        cache[i] = cache.get(i, 0) + 1
    for i in range(0, len(s)):
        if cache[s[i]] == 1:
            return i
    return -1