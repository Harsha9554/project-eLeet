matrix = [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]]

# 01 03 05 07
# 09 11 13 15
# 17 19 21 23

# iterate overalapping 2x2 blocks
# 01 03 09 11
# 03 05 11 13
# 05 07 13 15
# ..

# iterate overalapping 2x2 blocks
# rows = 3
# columns = 4
# r = 3
# c = 4
# for i in range(r):
#     for j in range(c):
