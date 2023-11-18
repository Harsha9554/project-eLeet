def binary_search_704(nums, t):
    n = len(nums)
    l, r = 0, n - 1
    if nums[l] == t:
        return l
    if nums[r] == t:
        return r
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == t:
            return mid
        elif t > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1
