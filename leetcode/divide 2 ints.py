class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1
        if (dividend>0) ^ (divisor>0):
            sign = -1

        dd = abs(dividend)
        dr = abs(divisor)

        res = 0
        while dd>=dr:
            dr_shift = dr
            i = 0
            while dr_shift <= dd:
                 dr_shift <<= 1
                 i += 1

            res += 1 << i-1
            dd -= dr << i-1


        if sign == 1:
            return res
        else:
            return -res

test = Solution()
print(test.divide(1,-5))