class Solution:
    def partitionPalindrome(self, s):
        dp = [list() for _ in range(len(s) + 1)]
        dp[len(s)] = [[]]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if self.checkPalindrome(s[i:j]):
                    dp[i] += list(map(lambda partition: [s[i:j]] + partition, dp[j]))
        return dp[0]
    
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