def container_with_most_water_11(height):
    n = len(height)
    l, r = 0, n - 1
    max_area = -1
    while l < r:
        hl, hr = height[l], height[r]
        max_area = max(max_area, (r - l) * min(height[l], height[r]))
        if hl > hr:
            r -= 1
        else:
            l += 1
    return max_area
