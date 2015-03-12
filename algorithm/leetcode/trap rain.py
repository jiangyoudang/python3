class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A) < 3:
            return 0
        l = 0
        r = len(A)-1
        volume = 0
        while l<r:
            left = A[l]
            right = A[r]
            if left <= right:
                l += 1
                while left>=A[l] and l<r:
                    volume += left-A[l]
                    l += 1
            else:
                r -= 1
                while right >=A[r] and l<r:
                    volume += right-A[r]
                    r -= 1

        return volume