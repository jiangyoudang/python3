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
