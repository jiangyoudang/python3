class Solution(object):
  def containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    if t < 0 or k < 1:
      return False
    bukets = {}
    vol = t+1
    for i, num in enumerate(nums):
      bukets_i = num//vol
      if i> k:
        del bukets[nums[i-k-1]//vol]

      if (bukets_i in bukets
          or (bukets_i-1 in bukets and abs(num - bukets[bukets_i-1]) <= t)
          or (bukets_i+1 in bukets and abs(num - bukets[bukets_i+1]) <= t)):
        return True

      bukets[bukets_i] = num

    return False

nums = [1, 3, 1]
k = 2
t = 1
print(Solution().containsNearbyAlmostDuplicate(nums, k, t))