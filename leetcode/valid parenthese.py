class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        pair = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in '}])':
                if stack and pair[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False