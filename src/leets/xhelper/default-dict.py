from collections import defaultdict


def aot_default_value():
    return "not-a-titan-shifter"


characters = ["eren", "reiner", "armin"]
normal_dict = {}
default_dict = defaultdict(aot_default_value)
for x in characters:
    # normal_dict[x] = normal_dict.get(x, "") + "titan-shifter"
    default_dict[x] = "titan-shifter"

print(normal_dict)
print(default_dict)
print(default_dict["levi"])
