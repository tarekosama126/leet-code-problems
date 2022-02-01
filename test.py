import math


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







from typing import List
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

from typing import List
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

from typing import List
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

