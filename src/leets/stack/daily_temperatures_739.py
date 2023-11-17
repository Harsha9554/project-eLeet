def daily_temperatures_739(temps):
    class Node:
        def __init__(self, val, ind):
            self.val = val
            self.ind = ind

    n = len(temps)
    res = [0] * n
    stack = []

    for i, t in enumerate(temps):
        t_node = Node(t, i)
        while stack and t_node.val > stack[-1].val:
            popped_node = stack.pop()
            res[popped_node.ind] = t_node.ind - popped_node.ind
        stack.append(t_node)
    return res


def daily_temperatures_739_i(temps):
    # 30 40 50 60 40 20
    ans = []
    n = len(temps)
    temps = temps[::-1]
    for i in range(n):
        if i == 0:
            ans.insert(0, 0)
        else:
            value = 0
            found = False
            for j in range(i - 1, -1, -1):
                if temps[j] <= temps[i]:
                    value += 1
                elif temps[j] > temps[i]:
                    value += 1
                    found = True
                    break
            if found:
                ans.insert(0, value)
            else:
                ans.insert(0, 0)
    return ans
