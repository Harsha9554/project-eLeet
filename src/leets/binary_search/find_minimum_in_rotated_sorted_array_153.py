def binary_search(nums, l, r, x):
    m = (l + r) // 2

    if l > r:
        return -1

    if nums[m] == x:
        return m
    elif nums[m] > x:
        return binary_search(nums, m + 1, r, x)
    else:
        return binary_search(nums, l, m - 1, x)


def get_pivot_index(nums, l, r):
    m = (l + r) // 2

    # 3 4 5 6 7 8 0 1 2
    # 0 1 2 3 4 5 6 7 8
    if m == len(nums) - 1 or nums[m] > nums[m + 1]:
        return m

    # 11 13 15 17
    #        l  r
    #        m

    # in the above case im just searching left instead of right array
    # so instead of nums[l] < nums[m] it is "nums[l] <= nums[m]"
    else:
        if nums[l] <= nums[m]:
            return get_pivot_index(nums, m + 1, r)
        else:
            return get_pivot_index(nums, l, m - 1)


def find_minimum_in_rotated_sorted_array_153(nums):
    # my initial reaction was to find pivot and get adjacent one.
    n = len(nums)
    l, r = 0, n - 1

    p_ind = get_pivot_index(nums, l, r)
    return nums[(p_ind + 1) % n]
