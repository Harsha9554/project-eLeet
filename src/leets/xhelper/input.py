n = int(input)                          # number
s = input()                             # string
l1 = list(map(int, input().split()))    # number list
l2 = list(map(str, input().split()))    # string list
x, y = map(int, input().split())        # input only 2


# input 2D array
matrix = []
col, row = 4, 4
for _ in range(col):
    matrix.append(list(map(int, input().split())))

for row in matrix:
    print(row)

# TODO: input a never knew how many lines to scan