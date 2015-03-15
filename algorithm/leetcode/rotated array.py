def rotate(nums, k):
    '''
    rotate nums k steps in place
    :param nums: a list of int
    :param k: num of steps
    :return:
    '''
    if not nums:
        return

    n = len(nums)

    def _rotate(nums, l, r):
        mid = (r-l+1) // 2
        for i in range(mid):
            temp = nums[l+i]
            nums[l+i] = nums[r-i]
            nums[r-i] = temp

    k = k % n
    if k==0:
        return

    _rotate(nums, 0, n-k-1)
    _rotate(nums, n-k, n-1)
    _rotate(nums, 0, n-1)









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