import math
import heapq
from typing import List


def moveZeroes(nums):
    i = 0
    j = 1
    size = len(nums) - 1
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
    i = 0
    j = 1
    size = len(prices) - 1
    while j <= size:
        if prices[i] < prices[j]:
            maxprofit += (prices[j] - prices[i])
        i += 1
        j += 1
    return maxprofit


def rotate(nums, k) -> None:
    print(len(nums))
    loop = 0
    lastindex = len(nums) - 1
    while loop != k:
        temp = nums[lastindex]
        j = lastindex - 1
        for i in range(lastindex, 0, -1):
            nums[i] = nums[j]
            j -= 1
        nums[0] = temp
        loop += 1


def numJewelsInStones(J, S):
    answer = 0
    lengthJ = len(J)
    lengthS = len(S)
    for i in range(0, lengthJ):
        for j in range(0, lengthS):
            if J[i] == S[i]:
                answer += 1
    return answer


def defangIPaddr(address):
    address = address.replace(".", "[.]");
    return address;


def decompressRLElist(nums):
    i = 0;
    answer = []
    while (i != len(nums)):
        freq = nums[i];
        i += 1
        val = nums[i];
        i += 1
        for j in range(0, freq):
            answer.append(val)
    return answer


def subtractProductAndSum(n: int):
    sum = 0
    product = 1
    digit = 0
    while (n != 0):
        digit = n % 10
        sum = sum + digit
        product = product * digit
        n = n // 10
    return product - sum


def findNumbers(nums):
    count = 0
    for i in range(0, len(nums)):
        num = str(nums[i])
        if (len(num) % 2 == 0):
            count += 1
    return count


def sortArrayByParity(A):
    size = len(A)
    arr = [0] * size
    i = 0
    j = size - 1
    for x in range(0, size):
        if (i > j):
            break
        if (A[x] % 2 == 0):
            arr[i] = A[x]
            i += 1
        else:
            arr[j] = A[x]
            j -= 1
    return arr;


def fizzBuzz(n):
    list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
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


def twoSum(nums, target):
    arr = []
    x = False
    size = len(nums)
    for i in range(0, size):
        for j in range(i + 1, size):
            if (nums[i] + nums[j] == target):
                arr[0] = i
                arr[1] = j
                x = True
                break

        if (x):
            break
    return arr


def plusOne(digits):
    i = len(digits) - 1
    line = ""
    while (i >= 0):
        if (digits[i] < 9):
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            line = str(digits[i]) + line
            i -= 1
    line = str(1) + line
    return list(line)


def reverse(x):
    negative = False
    reversed = 0
    if x < 1:
        negative = True
        x = abs(x)
    while (x != 0):
        lastdigit = x % 10
        reversed = (reversed * 10) + lastdigit
        x = x // 10
    if negative:
        reversed *= -1

    return reversed


def groupAnagrams(strs):
    cache = {}
    for i in strs:
        orginal = i
        org_ordered = str(sorted(i))
        print(org_ordered)
        if org_ordered in cache.keys():
            cache[org_ordered] = cache[org_ordered] + [orginal]
        else:
            cache[org_ordered] = [orginal]
    print(cache)
    output = []
    for key in cache:
        output.append(cache[key])
    return output


def countElements(arr):
    arr.sort()
    if len(arr) <= 1:
        return 0
    count = 0
    stack = [arr[0]]
    i = 1
    while i < len(arr):
        lastindex = len(stack) - 1
        if arr[i] > stack[lastindex] and arr[i] - stack[lastindex] == 1:
            count += 1
            x = stack.pop(lastindex)
            if x in stack:
                continue
            else:
                stack.append(arr[i])
                i += 1
        else:
            stack.append(arr[i])
            i += 1

    return count


def fun(S, T):
    index1 = 0
    for i in range(0, len(S)):
        if S[i] != '#':
            S[index1] = S[i]
            index1 += 1
        else:
            index1 -= 1
        if index1 < 0:
            index1 = 0
    index2 = 0
    for i in range(0, len(T)):
        if T[i] != '#':
            T[index2] = T[i]
            index2 += 1
        else:
            index2 = -1
        if index2 < 0:
            index2 = 0
    if index1 != index2:
        return False
    for i in range(0, index1 + 1):
        if S[i] != T[i]:
            return False

    return True


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return []
        else:
            self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        if len(self.stack) == 0:
            return []
        else:
            return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return []
        else:
            return min(self.stack)


def lastStoneWeight(stones) -> int:
    myneglist = [-x for x in stones]
    heapq.heapify(myneglist)
    while len(myneglist) >= 2:
        x = heapq.heappop(myneglist) * -1
        y = heapq.heappop(myneglist) * -1
        heapq.heappush(myneglist, (x - y) * -1)
    return myneglist(0) * -1


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


def minPathSum(grid: List[List[int]]):
    row, col = len(grid), len(grid[0])
    Matrix = [[0 for x in range(col)] for y in range(row)]
    Matrix[0][0] = grid[0][0]
    for j in range(1, col):
        Matrix[0][j] = Matrix[0][j - 1] + grid[0][j]
    for j in range(1, row):
        Matrix[j][0] = Matrix[j - 1][0] + grid[j][0]
    for i in range(1, row):
        for j in range(1, col):
            Matrix[i][j] = min(Matrix[i - 1][j], Matrix[i][j - 1]) + grid[i][j]
    return Matrix[row - 1][col - 1]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bstFromPreorder(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    index = 1
    while index < len(preorder):
        print(preorder[index])
        insert(root, preorder[index])
        index += 1
    return root


def PreorderTraversal(root):
    res = []
    if root:
        res.append(root.val)
        if root.left != None and root.right == None:
            res = res + PreorderTraversal(root.left)
            res.append(None)
        elif root.right != None and root.left == None:
            res.append(None)
            res = res + PreorderTraversal(root.right)
        else:
            res = res + PreorderTraversal(root.left)
            res = res + PreorderTraversal(root.right)

    return res


def insert(root, val):
    if val < root.val and root.left == None:
        root.left = TreeNode(val)

        return
    elif val < root.val and root.left != None:

        insert(root.left, val)

    elif val > root.val and root.right == None:
        root.right = TreeNode(val)

        return
    elif val > root.val and root.right != None:

        insert(root.right, val)


def findMaxLength(nums: List[int]) -> int:
    dict = {0: -1}
    count = 0
    max_length = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1

        if count in dict.keys():
            max_length = max(max_length, i - dict[count])
        else:
            dict[count] = i
    return max_length


def productExceptSelf(nums: List[int]) -> List[int]:
    right_multiply = [0] * len(nums)
    right_multiply[-1] = nums[-1]
    for i in range(1, len(nums)):
        right_multiply[len(nums) - i - 1] = right_multiply[len(nums) -
                                                           i] * nums[len(nums) - i - 1]
    output = [0] * len(nums)
    prefix = 1
    current_index = 0
    while current_index < len(output) - 1:
        output[current_index] = prefix * right_multiply[current_index + 1]
        prefix *= nums[current_index]
        current_index += 1
    output[-1] = prefix
    return output


def rotate_array(nums: List[int], k: int) -> None:
    output = [0] * len(nums)
    for i in range(0, len(nums)):
        output[(i + k) % len(nums)] = nums[i]
    print(output)


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    cache = {}
    for i in nums1:
        if i in cache:
            cache[i] += 1
        else:
            cache[i] = 1
    answer = []
    for i in nums2:
        if i in cache and cache[i] != 0:
            cache[i] -= 1
            answer.append(i)
    return answer


def rotate_matrix(matrix: List[List[int]]) -> None:
    size = len(matrix)
    for i in range(0, size // 2):
        for j in range(0, math.ceil(size / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[size - 1 - j][i]
            matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
            matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
            matrix[j][size - 1 - i] = temp


def isValidSudoku(board: List[List[str]]) -> bool:
    # first validate the rows
    # i is rows and j is coloum
    for i in range(0, 9):
        char = []
        for j in range(0, 9):
            if board[i][j] in char:
                return False
            if board[i][j] != ".":
                char.append(board[i][j])
    # print ("ROW IS VALIDATED")
    # validate the coloums
    for i in range(0, 9):
        char = []
        for j in range(0, 9):
            if board[j][i] in char:
                return False
            if board[j][i] != ".":
                char.append(board[j][i])
    # print ("Coloum is validated IS VALIDATED")
    # validate the boxes
    for start in range(0, 9, 3):
        for end in range(0, 9, 3):
            char = []
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[start + i][end + j] in char:
                        return False
                    if board[start + i][end + j] != ".":
                        char.append(board[start + i][end + j])
    # print("Box is validated")
    return True


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

# print(isPalindrome(".,"))
# firstUniqChar("leetcode")
# print(isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
# print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))
# print(intersect([4,9,5], [9,4,9,8,4]))
# rotate_array([-1,-100,3,99],2)
# howManyGames(20,3,6,85)
# print(findMaxLength([0, 1,0]))
# bstFromPreorder([8,5,1,7,10,12])
# print(productExceptSelf([9,0,-2]))
# print(minPathSum([[1,2,5],[3,2,1]]))
# print(isValidwithcontent("(*))"))
# productExceptSelf([1,3,5,7,9])
# stringShift("abcdefg",[[1,1],[1,1],[0,2],[1,3]])
# lastStoneWeight([2,7,4,1,8,1])
# fun("ab#c","ad#c")
# print(countElements([1,1,2]))
# print(reverse(-123))
# print(moveZeroes([0,1,0,3,12]))
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([1,2,3,4,5]))
# print(maxProfit([7,6,4,3,1]))
# rotate([1,2,3,4,5,6,7],3)
# numJewelsInStones("aA","aAAbbbb")
# print(decompressRLElist([1,2,3,4]))
# print(plusOne([9,9]))
# print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

