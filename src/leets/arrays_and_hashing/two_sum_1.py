def two_sum_1(nums, target):
    # i take a number,
    #   i get the other part i.e target - number
    #   i take the other part and put it as a key and position as value
    #       i then move to the next and check if there is a key as my value i'm holding
    #           if yes?
    #               i got the 2 sum
    #           if no? i repeat
    # ** interesting edge case
    #       what if the target can be halved like t = 10 and there is only one 5 in the array. it shouldn't find the target actually.
    d = {}
    for i, x in enumerate(nums):
        if x not in d.keys():
            d[target - x] = i
        else:
            other_index = d[x]
            return [other_index, i]
