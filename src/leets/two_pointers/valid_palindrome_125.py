def clean_string(s):
    s = s.lower()
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char
    return new_s


def valid_palindrome_125(s):
    s = clean_string(s)
    n = len(s)
    l, r = 0, n - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True
