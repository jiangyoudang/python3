class Solution:
    # @return a boolean
    def isDeformation(self, s1, s2):
        d = {}
        if not len(s1)==len(s2): return False
        for c in s1:
            d[c] = d.get(c, 0) + 1
        for c2 in s2:
            d[c2] = d.get(c2, 0) - 1
            if d[c2]<0: return False
        return True


    def isScramble(self, s1, s2):
        if s1==s2: return True
        if self.isDeformation(s1, s2):
            s1_len = len(s1)
            for i in range(1, s1_len):
                s11 = s1[:i]
                s12 = s1[i:]
                s21 = s2[:i]
                s22 = s2[i:]
                s23 = s2[:s1_len-i]
                s24 = s2[s1_len-i:]
                if self.isScramble(s11,s21) and self.isScramble(s12, s22): return True
                if self.isScramble(s11,s24) and self.isScramble(s12, s23): return True
        return False


test = Solution()
res = test.isScramble('ab', 'ba')
print(res)