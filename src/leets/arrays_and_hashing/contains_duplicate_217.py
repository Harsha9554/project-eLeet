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
    