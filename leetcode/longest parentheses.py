class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        l_max = 0

        for i in range(len(s)):
            if s[i]==')' and stack and stack[-1][0]=='(':
                stack.pop()
                if stack:
                    l_max = max(i-stack[-1][1], l_max)
                else:
                    l_max = max(i+1, l_max)
            else:
                stack.append((s[i],i))
        return l_max

test = Solution()
test_case = '(()()(())(('
res = test.longestValidParentheses(test_case)

print(res)