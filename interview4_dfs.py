class Solution:
    def partitionPalindrome(self, s):
        result = list()
        self.dfs(s, list(), 0, result)
        return result

    def dfs(self, s, partition_accumulated, s_idx, partitions):
        if s_idx == len(s):
            partitions.append(partition_accumulated)
            return
        for i in range(s_idx + 1, len(s) + 1):
            if self.checkPalindrome(s[s_idx:i]):
                self.dfs(s, partition_accumulated + [s[s_idx: i]], i, partitions)
    
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