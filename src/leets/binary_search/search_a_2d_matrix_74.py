def search_a_2d_matrix_74(mat, t):
    # binary search 1st col
    def gen_col_arr(mat):
        res = []
        for row in mat:
            res.append(row[0])
        return res

    def binary_search(a, t):
        n = len(a)
        l, r = 0, n - 1
        if a[l] == t:
            return True
        elif a[r] == t:
            return True
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == t:
                return True
            elif a[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def get_col_index(a, t):
        n = len(a)
        l, r = 0, n - 1
        if a[l] == t:
            return l
        elif a[r] == t:
            return r
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == t:
                return mid
            elif a[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
        return r

    col_arr = gen_col_arr(mat)
    # print(col_arr)
    col_index = get_col_index(col_arr, t)
    return binary_search(mat[col_index], t)
    # binrary search that row based on col
