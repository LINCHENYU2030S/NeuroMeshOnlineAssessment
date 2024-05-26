'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''

class Solution:
    def __init__(self):
        self.memo = list()

    def partitionPalindrome(self, s):
        if len(s) == 0:
            return [[]]
        self.memo = [None] * len(s)
        return self.helper(s, 0)

    def helper(self, s, s_idx):
        if s_idx == len(s):
            return [[]]
        
        if self.memo[s_idx] is not None:
            return self.memo[s_idx]

        result = list()
        for i in range(s_idx + 1, len(s) + 1):
            for partition in self.helper(s, i):
                if self.checkPalindrome(s[s_idx:i]):
                    result.append([s[s_idx:i]] + partition)

        self.memo[s_idx] = result
        return self.memo[s_idx]
    
    def checkPalindrome(self, s):
        for i in range(len(s) // 2):
            if (s[i] != s[len(s) - 1 - i]):
                return False
        return True
    
# test case 1
s = "aab"
#print(Solution().partitionPalindrome(s))

# test case 2
s1 = "aabbaa"
print(Solution().partitionPalindrome(s1))
#print(len(Solution().partitionPalindrome(s1)))