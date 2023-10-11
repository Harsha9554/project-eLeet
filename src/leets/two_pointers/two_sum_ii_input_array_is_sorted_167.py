def two_sum_ii_input_array_is_sorted_167(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
