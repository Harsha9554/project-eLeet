import sys

from leets.binary_search.search_a_2d_matrix_74 import search_a_2d_matrix_74


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        mat = []
        for _ in range(r):
            mat.append(list(map(int, input().split())))
        t = int(input())
        print(search_a_2d_matrix_74(mat, t))


main()
