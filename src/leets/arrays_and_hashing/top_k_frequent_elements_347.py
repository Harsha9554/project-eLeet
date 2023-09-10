def top_k_frequent_elements_347(nums, k):
    # 9: 4
    # 6: 2
    # 7: 2
    # 0: 3
    # 2: 1
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    items = list(freq_map.items())
    items.sort(key=lambda item: -item[1])

    result = []
    for i in range(k):
        result.append(int(items[i][0]))
    return result


import heapq


class FreqNode:
    def __init__(self, v, k):
        self.v = v
        self.k = k

    def __repr__(self):
        return self.v

    def __lt__(self, other):
        return self.k > other.k


def top_k_frequent_elements_347_ii(nums, k):
    freq_map = {}
    freq_list = []
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    for key, freq in freq_map.items():
        freq_list.append(FreqNode(key, freq))

    heapq.heapify(freq_list)

    result = []
    for _ in range(k):
        result.append(heapq.heappop(freq_list))
    return result
