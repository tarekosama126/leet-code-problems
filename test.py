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

