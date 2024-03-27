def binary_search(nums, l, r, x):
    m = (l + r) // 2

    if l > r:
        return -1

    else:
        if nums[m] == x:
            return m
        elif nums[m] > x:
            return binary_search(nums, l, m - 1, x)
        else:
            return binary_search(nums, m + 1, r, x)


def get_pivot_index(nums, l, r):
    m = (l + r) // 2

    # stuck at size 2 case

    # 1 2 3 4 5 6 7
    if m == len(nums) - 1 or nums[m] > nums[m + 1]:
        return m

    if nums[l] <= nums[m]:
        # [4,5,6,7,8,1,2,3]
        return get_pivot_index(nums, m + 1, r)
    else:
        # [7,8,1,2,3,4,5,6]
        return get_pivot_index(nums, l, m - 1)


def search_in_rotated_sorted_array_33(nums, x):
    n = len(nums)

    l, r = 0, n - 1

    p_ind = get_pivot_index(nums, l, r)

    if nums[l] <= x <= nums[p_ind]:
        return binary_search(nums, l, p_ind, x)
    else:
        return binary_search(nums, p_ind + 1, r, x)

    ## initial finding of left or right part

    ## if num < L part then
    ## normal BS on right sub part
    ## if num >= L part then
    ## normal BS on left sub part

    # then normal binary search on it

    # [4,5,6,7,8,1,2,3]
    # case where my logic doesnt work

    # in simple words just because num > l, doest mean that it exists in left part always
    # here left part is 4 5 6 7
    # right part is 8 1 2 3
    # target is 8

    # 1 3 was wrong
    # now 3 1 is wrong as

    # get the pivot
    # search left part of pivot or right part
