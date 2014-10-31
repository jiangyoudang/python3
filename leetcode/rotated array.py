class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        L = 0
        R = len(A)-1
        if A[L] == target: return L
        while L<R:
            M = (L+R)//2
            if A[L] == target: return L
            elif A[M] == target: return M
            elif A[R] == target: return R

            if A[L]< A[M]:
                if A[L]<target<A[M]: R = M - 1
                else: L=M + 1
            else:
                if A[M]< target < A[R]: L = M + 1
                else: R = M - 1
        return -1

    #no duplicates
    def findMin(self, num):
        l = 0
        r = len(num)-1
        min_num = num[0]

        while l<r:
            m = l + (r-l)//2
            min_num = min(min_num, num[l], num[r], num[m])
            if num[l] < num[m]:
                l = m+1
            else:
                r = m-1
        return min_num


    # allow duplicates
    def findMin2(self, num):
        l = 0
        r = len(num)-1
        min_num = num[0]

        while l<r:
            m = l + (r-l)//2
            min_num = min(min_num, num[l], num[r], num[m])
            if num[l] < num[m]:
                l = m+1
            elif num[l] > num[m]:
                r = m-1
            else:
                l += 1
        return min_num