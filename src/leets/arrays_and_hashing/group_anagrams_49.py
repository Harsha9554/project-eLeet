def group_anagrams_49(strs):
    anagram_dict = {}
    result = []
    for word in strs:  # m
        s_word = "".join(sorted(word))  # n log n
        if s_word in anagram_dict.keys():
            anagram_dict[s_word].append(word)
        else:
            anagram_dict[s_word] = [word]

    for k in anagram_dict.keys():
        result.append(anagram_dict[k])

    return result
