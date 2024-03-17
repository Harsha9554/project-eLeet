def is_got_em_all(d, k):
    if len(d.keys()) == 1:
        return True
    vals = sorted(d.values())
    return sum(vals[:-1]) <= k


def add_to_dict(d, char):
    d[char] = d.get(char, 0) + 1


def longest_repeating_character_replacement_424(s, k):
    l = 0
    n = len(s)
    sd = {}

    max_l = 0

    for r in range(0, n):
        char = s[r]
        add_to_dict(sd, char)

        if is_got_em_all(sd, k):
            max_l = max(max_l, r - l + 1)
        else:
            sd[s[l]] -= 1
            l += 1

    return max_l


def longest_repeating_character_replacement_424_ii(s, k):
    l, r = 0, 0
    n = len(s)
    sd = {}

    if k == 0:
        if len(set(s)) == 1:
            return n

    if k >= n:
        return n

    max_l = 0

    while l <= r and r < n:
        print(s[l : r + 1])
        add_to_dict(sd, s[r])
        if is_got_em_all(sd, k):
            max_l = max(max_l, r - l + 1)
            r += 1
        else:
            sd[s[l]] -= 1
            l += 1
    print(l, r)

    while l < r:
        print("i was here")
        if is_got_em_all(sd, k):
            max_l = max(max_l, r - l + 1)
            r += 1
        else:
            sd[s[l]] -= 1
            l += 1
    return max_l
