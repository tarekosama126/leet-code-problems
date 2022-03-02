def isSubsequence(self, s: str, t: str) -> bool:
    SizeOfs = len(s)
    SizeOft = len(t)
    if(SizeOft < SizeOfs):
        return False
    first = 0
    second = 0
    while(first < SizeOfs and second < SizeOft):
        if(s[first]==t[second]):
            first +=1
            second +=1
        else:
            second +=1
    #print(first,second)
    return first==SizeOfs