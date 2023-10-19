def trapping_rain_water_42_i(height):
    # go to h1. go to h2 till you can get just above it.
    # count a left pillar only when the adjacent right is smaller.
    # if it's equal continue till you get smaller.
    l, r = 0, 0
    amount = 0
    n = len(height)
    while l <= r and r < n:
        # 0 1 1 0
        # for this, the l should start from 2.

        # find the l now.
        if height[l] > height[l + 1]:
            # you fix the l and move r
            r += 1
            while height[r] < height[l]:
                amount += height[l] - height[r]
                r += 1
            l = r

        # i lost my mind at peak case. where the l point is the peak.

        else:
            l += 1
            r += 1


def trapping_rain_water_42(height):
    n = len(height)
    max_left, max_right = 0, 0
    max_left_l, max_right_l, min_lr = [0] * n, [0] * n, [0] * n

    for i in range(n):
        max_left_l[i] = max_left
        max_left = max(max_left, height[i])

    for i in range(n - 1, -1, -1):
        max_right_l[i] = max_right
        max_right = max(max_right, height[i])

    for i in range(n):
        min_lr[i] = min(max_left_l[i], max_right_l[i])

    amount = 0
    for i in range(n):
        # at i trapped = min(l,r) -
        trapped = min_lr[i] - height[i]
        if trapped > 0:
            amount += trapped

    return amount
