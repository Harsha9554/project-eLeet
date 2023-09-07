def valid_anagram_242(s, t):
    # case of different lengths
    # if s = "a" t = "dkjahkasnckasdaoidjwldjp"
    # we don't need to check everything obviously. it's not going to be an anagram

    sn, tn = len(s), len(t)
    if sn != tn:
        return False

    # do hashmaps, like i will make a freq. map for both strings. and compare frequencies with other string's keys and values.

    # getting freq. map
    s_map, t_map = {}, {}

    for x in s:
        s_map[x] = s_map.get(x, 0) + 1

    for x in t:
        t_map[x] = t_map.get(x, 0) + 1

    is_anagram = True
    for k, v in s_map.items():
        if k not in t_map or t_map[k] != v:
            is_anagram = False
            break

    return is_anagram


def valid_anagram_242_i(s, t):
    # sort both, compare. ez.
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t


def valid_anagram_242_ii(s, t):
    freq_arr = [0] * 26

    for x in s:
        freq_arr[ord(x) - ord("a")] += 1

    for x in t:
        freq_arr[ord(x) - ord("a")] -= 1

    is_anagram = True
    for x in freq_arr:
        if x != 0:
            is_anagram = False
            break
    return is_anagram

    # hash table using arrays
    # 0 1 2 ... 25
    # a b c ... z

    # ord('a') = 97
    # ord('z') = 97 + 25

    # in other words we can get freq. using their ascii value mapped array.

    # we increase freq. every time we find a char. from string 's'
    # we decrease freq. every time we find a char. from strnig 't'

    # let's say words are cat rat

    # 0 1 2 ... i .. j ...
    # a b c ... r .. t ...
    # 1 0 1 ... 0 ...1 ... (s)
    # 0 0 1 ... -1 ..0 ... (t)

    # all are not 0s there fore they aren't anagrams
