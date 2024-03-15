frequency_map = {}
a = ["eren", "zeke", "toji", "zeke", "thorfinn", "kenzo", "dr-tenma"]


# method #1
# m[x] = get m[x] + 1
# but what if there is no key x?
# then default value = 0. by m.get(x, 0)

for character in a:
    frequency_map[character] = frequency_map.get(character, 0) + 1
print(frequency_map)


# method #2

for character in a:
    if character not in frequency_map:
        frequency_map[character] = 1
    else:
        frequency_map[character] += 1
print(frequency_map)


def add_to_d(n, d):
    d[n] = d.get(n, 0) + 1


d = {1: 2, 2: 4}
add_to_d(3, d)
print(d)
