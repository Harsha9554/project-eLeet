# class car:
#     def __init__(self, pos, spd):
#         self.pos = pos
#         self.spd = spd

#     def __str__(self):
#         return f"(p:{self.pos}, s:{self.spd})"

#     def __repr__(self):
#         return f"(p:{self.pos}, s:{self.spd})"


# def get_collision_point(c1, c2):
#     # s0: 0-4, 4-2
#     # s1: 4-4, 6-2
#     # s2: 8-4, 8-2
#     t = (c2.pos - c1.pos) / (c1.spd - c2.spd)
#     print(c1.pos + c1.spd * t)
#     return c1.pos + c1.spd * t


# def does_collide(c1, c2, t):
#     if c1.spd <= c2.spd:
#         return False
#     else:
#         if get_collision_point(c1, c2) <= t:
#             return True
#         return False


# c1 = car(0, 3)
# c2 = car(2, 2)
# t = 5
# print(does_collide(c1, c2, t))

# a = [-1, 0, 3, 5, 9, 12]
# print(*a, sep=" ")
