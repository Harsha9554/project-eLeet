def longest_consecutive_sequence_128_i(nums):
    # oka real life contest persp. chusthey, i'm sure i would be thinking this as a dp or recursion or graph based q. becaus of
    # my half knowledge

    # let's say the hint is it is a hashmap problem now what?

    # 100 4 200 1 3 2
    # basically i can track if i had this number in past. for sure. it's index. for sure

    # --
    # 100: 1
    # 4: 1
    # 200: 1
    # 1: 1
    # 3: 2
    # 2: 4
    # --

    # --
    # 0: 2
    # 3: 1
    # 7: 1
    # 2: 2
    # 5: 1
    # 8: 2
    # 4: 3
    # 6: 5
    # 1: 4
    # --

    # this is bullshit.

    # i'll try brute force, sort and get the lcs

    sorted_nums = sorted(set(nums))
    ml, cl = -1, 1
    l, r = 0, 1
    n = len(nums)
    if n == 0:
        return 0
    print(sorted_nums)
    while l < r and r < n:
        if sorted_nums[r - 1] == sorted_nums[r] - 1:
            cl += 1
            r += 1
        else:
            # l is at 4, r is at 100
            ml = max(ml, cl)
            cl = 1
            l += 1
            r += 1
    ml = max(ml, cl)

    return ml


def longest_consecutive_sequence_128(nums):
    # sequence? set and head.

    num_set = set(nums)
    ml = -1
    for x in num_set:
        if x - 1 not in num_set:
            lc = 1
            i = 1
            flag = True
            while flag:
                if x + i not in num_set:
                    flag = False
                    ml = max(ml, lc)
                    break
                else:
                    i += 1
                    lc += 1
    ml = max(ml, lc)
    return ml
