class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for i in range(len(num)):
            num[i] = (num[i], i+1)
        num_sorted = sorted(num)

        i = 0
        j = len(num) - 1
        while i<j:
            if num_sorted[i][0] + num_sorted[j][0] > target:
                j -= 1
            elif num_sorted[i][0] + num_sorted[j][0] < target:
                i += 1
            else:
                return tuple(sorted([num_sorted[i][1], num_sorted[j][1]]))

