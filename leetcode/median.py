class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        n = len(A)
        m = len(B)
        if m<n:
            return self.findMedianSortedArrays(B, A)

    # find kth

        k = (m+n-1)//2
        l = 0
        r = min(n,k)
        while l<r:
            midA = (l+r)//2
            midB = k - midA
            if A[midA] < B[midB]:
                l = midA + 1
            else:
                r = midA

        if k>=l:
            if l>0:
                a = max(A[l-1],B[k-l])
            else:
                a = B[k-l]
        else:
            a = B[k-l]

        if (m+n)%2==1:
            return a
        else:
            if l<n:
                if k-l+1<m:
                    return (a+min(A[l],B[k-l+1]))/2
                else:
                    return (a + A[l])/2
            else:
                return (a + B[k-l+1])/2


# solution 2: make use of getkth, get median when ks are the middle of the total length.
        #complexity: O(log(m+n))

# int getkth(int s[], int m, int l[], int n, int k){
#         // let m <= n
#         if (m > n)
#             return getkth(l, n, s, m, k);
#         if (m == 0)
#             return l[k - 1];
#         if (k == 1)
#             return min(s[0], l[0]);
#
#         int i = min(m, k / 2), j = min(n, k / 2);
#         if (s[i - 1] > l[j - 1])
#             return getkth(s, m, l + j, n - j, k - j);
#         else
#             return getkth(s + i, m - i, l, n, k - i);
#         return 0;
#     }

test = Solution()
res = test.findMedianSortedArrays([2,3],[])
print(res)