class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum = A[0]
        curr_sum = A[0]
        for curr in A[1:]:
            curr_sum = max(curr, curr_sum + curr)
            max_sum = max(max_sum, curr_sum)
        return max_sum


    def maxProduct(self, A):
        max_p = A[0]
        curr_p = A[0]
        curr_min_p = A[0]
        for curr in A[1:]:
            curr_p, curr_min_p = max(curr, curr_p*curr, curr_min_p*curr),\
                                 min(curr, curr_min_p*curr, curr_p*curr)
            max_p = max(max_p, curr_p)
        return max_p

