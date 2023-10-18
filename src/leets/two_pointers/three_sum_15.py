def three_sum_15(nums):
    # -1 0 1 2 -1 -4
    # -4 -1 -1 0 1 2

    # takeaway:
    # to actually consider 3 variables in a list:
    # loop 1 (oka variable ki)
    # inner loop for other two variables using 2 pointers
    triplets = set()
    n = len(nums)
    nums = sorted(nums)
    for i in range(n):
        j = i + 1
        k = n - 1
        while j < k:
            trip_sum = nums[i] + nums[j] + nums[k]
            if trip_sum == 0:
                triplets.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif trip_sum > 0:
                k -= 1
            else:
                j += 1

    result = []
    for triplet in triplets:
        result.append([*triplet])
    return result
