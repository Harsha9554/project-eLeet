def generate_parentheses_22(n):
    def gen_helper(l, r, s, n, res):
        if l < 0 or r < 0:
            return
        if l > r:
            return
        elif l == 0 and r == 0:
            res.append(s)
            return
        else:
            gen_helper(l - 1, r, s + "(", n, res)
            gen_helper(l, r - 1, s + ")", n, res)

    l = r = n
    res = []
    gen_helper(l, r, "", n, res)
    return res
