def contains_duplicate_217(nums):
    return len(nums) != len(set(nums))

# brute force
def contains_duplicate_217_i(nums):
    # TLE
    # o(n^2)
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False

# sort and compare adjacent
def contains_duplicate_217_ii(nums):
    n = len(nums)
    a = sorted(nums)
    for i in range(n-1):
        if a[i] == a[i+1]:
            return True
    return False

# hashmap, comparing seen ones
def contains_duplicate_217_iii(nums):
    seen = {}
    for num in nums:
        if num in seen and seen[num] >= 1:
        # seen[num] >= 1?
        # gre eq 1 ah? how?
        #
        # lets say arr = [9, 10, 9, 7]
        # lets say seen = { 9: 1, 10: 1 } ila undhi.
        # 
        # now, after two iterations
        # num = 9.
        #
        # num in seen? 9 in seen? ya.
        # i hold 2nd 9 in my hand. 
        # seen[num] >= 1? ya it's 1. so ya
        # 
        # 1 unna duplicates unnatte endhukante. i hold one number, seen already has 1 so 2 numbers are there.
        # therefore, duplicates.
        #
            return True
        seen[num] = seen.get(num, 0) + 1
    return False