from ast import List


def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1,n+1):
            backword = res[i//2]
            if(i%2==0):
                res.append(backword)
            else:
                res.append(backword+1)
           
        print(res)
        return res