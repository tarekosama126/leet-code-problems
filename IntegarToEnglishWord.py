def numberToWords(num: int) -> str:
    ans=""
    count = 0
    if(num==0):
       print("Zero")
    while num != 0:
        last3Digits = num%1000
        print(last3Digits)
        ans = helper(str(last3Digits),count) + ans
        #print(last3Digits,helper(str(last3Digits),count))
        
        num = num//1000
        if(num!=0):
            ans = " " + ans
        count+=1
    print(ans)
def helper(number,count):
    res = ""
    
    if(len(number)==3):
        hund = number[0]
        rest = number[1:]
        if(hund != "0"):
            res += GetValues(hund) + "Hundred "
        if(rest[0]!="0" and rest[0]!=1):
            res += GetValues(str(int(rest[0])*10)) + GetValues(rest[1])
        elif(rest[0]=="1"):
            res+= GetValues(rest)
    elif(len(number)==2):
        
        if(number[0]=="1"):
            res+=GetValues(number)
        else:
            if(number[1]=="0"):
                res += GetValues(str(int(number[0])*10)) 
            else:
                res += GetValues(str(int(number[0])*10)) + GetValues(number[1])
    else:
        print("HENAAA")
        res+= GetValues(number)
    if(count==1):
        res+="Thousand "
    elif(count==2):
        res+="Million "    
    
    
    return res
def GetValues(number):
    #function that map values to wordss
    reference = {'1': "One ", '2': "Two ", '3': "Three ",
                '4': "Four ", '5': "Five ", '6': "Six ",
                '7': "Seven ", '8': "Eight ", '9': "Nine ",
                '11': "Eleven ", '12': "Twelve ", '13': "Thirteen ",
                '14': "Fourteen ", '15': "Fifteen ", '16': "Sixteen ",
                '17': "Seventeen ", '18': "Eighteen ", '19': "Nineteen ",
                '10': "Ten ", '20': "Twenty ", '30': "Thirty ",
                '40': "Forty ", '50': "Fifty ", '60': "Sixty ",
                '70': "Seventy ", '80': "Eighty ", '90': "Ninety "
                }
    return reference[number]
numberToWords(0)       