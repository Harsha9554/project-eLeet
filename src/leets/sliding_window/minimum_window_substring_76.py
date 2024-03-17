def is_got_em_all(sd, td):
    for k, v in sd.items():
        if v < td[k]:
            return False
    return True


def add_to_s_set(char, sd):
    sd[char] = sd.get(char, 0) + 1


def get_min(a, b):
    if len(a) < len(b):
        return a
    return b


def minimum_window_substring_76(s, t):
    st, lt = len(s), len(t)
    if lt > st:
        return ""

    sd, td = {}, {}

    t_set = set(t)

    for char in t:
        td[char] = td.get(char, 0) + 1

    for k in td.keys():
        sd[k] = 0

    min_w = "0" * (st + 1)
    l, r = 0, 0

    while l < st:
        if r < st and not is_got_em_all(sd, td):
            if s[r] in t_set:
                add_to_s_set(s[r], sd)
            r += 1
        else:
            if is_got_em_all(sd, td):
                min_w = get_min(min_w, s[l:r])
            if s[l] in t_set:
                sd[s[l]] -= 1
            l += 1

    if min_w == "0" * (st + 1):
        return ""

    return min_w


def minimum_window_substring_76_ii(s, t):
    st, lt = len(s), len(t)
    if lt > st:
        return ""

    sd, td = {}, {}

    t_set = set(t)

    for char in t:
        td[char] = td.get(char, 0) + 1

    for k in td.keys():
        sd[k] = 0

    min_w = "0" * (st + 1)
    l, r = 0, 0

    while l <= r and r < st:
        if is_got_em_all(sd, td):
            min_w = get_min(min_w, s[l:r])
            if s[l] in t_set:
                sd[s[l]] -= 1
            l += 1
        else:
            if s[r] in t_set:
                add_to_s_set(s[r], sd)
                r += 1
            else:
                r += 1

    while l < r:
        if is_got_em_all(sd, td):
            min_w = get_min(min_w, s[l:r])
            if s[l] in t_set:
                sd[s[l]] -= 1
            l += 1
        else:
            break

    if min_w == "0" * (st + 1):
        return ""

    return min_w
