from random import shuffle

'''
初阶：有N个数，其中一个数的出现次数严格超过了一半。求这个数。
进阶1：有N个数，其中两个数的出现次数都超过了⅓ ，求这两个数。
进阶2：有N个数，其中一个数的出现次数严格超过了⅓，并且没有第二个这样的数。求这个数。
'''

nums = [1,2,3,1,3,4,1,4]


def maj1(nums):
    if not nums:
        return None
    vote = nums[0]
    count = 1
    for i in nums[1:]:
        if i == vote:
            count += 1
        else:
            if count == 1:
                vote = i
            else:
                count -= 1

    return vote

def maj2(nums):
    if not nums:
        return None

    votes = [None, None]
    count = [0,0]

    for num in nums:
        if num in votes:
            i = votes.index(num)
            count[i] += 1
        elif 0 in count:
            i = count.index(0)
            votes[i] = num
            count[i] = 1
            continue
        else:
            count[0] -= 1
            count[1] -= 1

    return votes

def maj3(nums):
    candidates = maj2(nums)


shuffle(nums)
print(nums)

print(maj2(nums))