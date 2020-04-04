def moveZeroes(nums):
    i = 0
    j = 1
    size = len(nums)-1
    while i <= size and j <= size:
        if nums[i] != 0:
            i += 1
            j += 1
        elif nums[i] == 0 and nums[j] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
            j += 1
        elif nums[i] != 0 and nums[j] != 0:
            i += 2
            j += 2
        elif nums[i] == 0 and nums[j] == 0:
            j += 1
    return nums
def removeDuplicates(nums):
    ans = 1
    index = 1
    test = nums[0]
    for i in range(1, len(nums)):
        if test != nums[i]:
            nums[index] = nums[i]
            ans += 1
            index += 1
        test = nums[i]
    return ans
def singleNumber(nums) -> int:
        nums.sort()
        i = 0
        while i != len(nums):
            if i + 1 >= len(nums):
                return nums[i]
            if nums[i] == nums[i + 1]:
                i = i + 2
                continue
            else:
                return nums[i]
def maxProfit(prices) -> int:
    maxprofit = 0
    i  = 0
    j  = 1
    size = len(prices)-1
    while j <= size:
        if prices[i] < prices[j]:
            maxprofit += (prices[j] - prices[i])
        i += 1
        j += 1
    return maxprofit
def rotate(nums, k) -> None:
    print(len(nums))
    loop = 0
    lastindex = len(nums)-1
    while loop != k:
        temp = nums[lastindex]
        j = lastindex-1
        for i in range(lastindex, 0, -1):
            nums[i] = nums[j]
            j -= 1
        nums[0] = temp
        loop += 1
def numJewelsInStones(J, S) :
    answer = 0
    lengthJ = len(J)
    lengthS = len(S)
    for i in range(0,lengthJ):
        for j in range(0, lengthS):
    	    if J[i] == S[i] :
    		    answer+=1
    return answer
def defangIPaddr(address):
    address = address.replace(".", "[.]");
    return address;
def decompressRLElist(nums):
    i=0;
    answer = []
    while(i!=len(nums)):
        freq = nums[i];
        i+=1
        val = nums[i];
        i+=1
        for j in range(0, freq):
            answer.append(val)
    return answer
def subtractProductAndSum(n:int):
    sum = 0
    product = 1
    digit=0
    while(n != 0):
        digit = n%10
        sum = sum + digit
        product = product*digit
        n=n//10
    return product - sum
def findNumbers(nums):
    count = 0
    for i in range(0,len(nums)):
        num = str( nums[i] )
        if (len(num) % 2 == 0):
            count+=1
    return count
def sortArrayByParity(A):
    size = len(A)
    arr = [0] * size
    i = 0
    j = size-1
    for x in range(0, size):
        if(i > j):
        	break
        if(A[x]%2==0):
        	arr[i]=A[x]
        	i+=1
        else :
        	arr[j] = A[x]
        	j-=1
    return arr;
def fizzBuzz(n):
    list = []
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            list.append("FizzBuzz")
        elif i%3==0:
            list.append("Fizz")
        elif i%5==0:
            list.append("Buzz")
        else:
            list.append(str(i))
    return list
"""
map in JAVA 
        Map<Integer, Integer> Map1 = new HashMap<Integer, Integer>();
        	for(int x : A){
        		Map1.put(x, Map1.getOrDefault(x,0)+1);
	         }
        	
        	for (int k: Map1.keySet())
                if (Map1.get(k) > 1)
                    return k;
	        return 0;}

        List<Integer> answer = new ArrayList();
        boolean test = true;
        for(int i=left;i<=right;i++){
        	test = true;
        	char[] SepratedNumber = String.valueOf(i).toCharArray();
            for(char c : SepratedNumber) {
            	if(c=='0' ||  i % (c-'0') > 0) {
            		test = false;
            		break;
            	}
            }
            if(test) {
            	answer.add(i);
            }
        }
        for(int x:answer) {
        	System.out.print(x+" ");
        }
        return answer;
        
        
        Set<String> hash_Set = new HashSet<String>(); 
        hash_Set.add(total);
        hash_Set.size();
        set.contains("Geeks")
"""
def isValid(s):
    list = []
    for i in s:
        if i =='(' or i=='[' or i=='{':
            list.append(i)
        elif i == ')':
            if list.pop(len(list)-1) == '(':
                continue
            else:
                return False
        elif i == '}':
            if list.pop(len(list)-1) == '}':
                continue
            else:
                return False
        elif i == ']':
            if list.pop(len(list)-1) == ']':
                continue
            else:
                return False
    return True
#print(moveZeroes([0,1,0,3,12]))
#print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
#print(maxProfit([7,1,5,3,6,4]))
#print(maxProfit([1,2,3,4,5]))
#print(maxProfit([7,6,4,3,1]))
#rotate([1,2,3,4,5,6,7],3)
#numJewelsInStones("aA","aAAbbbb")
#print(decompressRLElist([1,2,3,4]))
