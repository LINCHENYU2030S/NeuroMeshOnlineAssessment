class Solution:
    def readInput(self):
        string = input()
        return string
    
    def calculateLabel(self, string):
        string_len = len(string)
        label = [" "] * string_len
        left_bracket_idx = list()

        for index, char in enumerate(string):
            if char == "(":
                left_bracket_idx.append(index)
            elif char == ")":
                if len(left_bracket_idx) == 0:
                    label[index] = "?"
                else:
                    left_bracket_idx.pop()
        
        for idx in left_bracket_idx:
            label[idx] = "x"
        return "".join(label)
    
    def solve(self):
        string = self.readInput()
        label = self.calculateLabel(string)
        #print(string)  不确定是否需要再打印一次原字符串
        print(label)
        return label

if __name__ == "__main__":
    Solution().solve()