def longest_substring_without_repeating_characters_3(s):
    n = len(s)

    if n <= 1:
        return n

    max_length = 0
    current_window = set()
    l, r = 0, 0

    while l <= r and r < n:
        max_length = max(max_length, len(current_window))
        if s[r] not in current_window:
            current_window.add(s[r])
            r += 1
        else:
            # abca
            # l--r
            if s[l] == s[r]:
                l += 1
                r += 1
            # acdbb
            # l---r
            # my thought is that, set it to b here

            # abcb
            # l--r
            # set it to cb here
            else:
                while s[r] in current_window:
                    current_window.remove(s[l])
                    l += 1
                current_window.add(s[r])
                r += 1
    max_length = max(max_length, len(current_window))
    return max_length
