class Solution:
    def readInput(self):
        source = input()
        target = input()
        return source, target
    
    def countMinSubsequence(self, source, target):
        count = 0
        target_pointer = 0
        target_len = len(target)
        while target_pointer < target_len:
            count += 1
            target_pointer_prev = target_pointer
            for char in source:
                target_pointer += (char == target[target_pointer])
                if target_pointer == target_len:
                    break
            if target_pointer == target_pointer_prev:
                return -1
        return count

    def solve(self):
        source, target = self.readInput()
        count = self.countMinSubsequence(source, target)
        print(count)
        return count

if __name__ == "__main__":
    Solution().solve()