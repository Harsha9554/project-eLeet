import sys

from leets.arrays_and_hashing.contains_duplicate_217 import contains_duplicate_217_i

sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        a = list(map(int, input().split()))
        print(contains_duplicate_217_i(a))


main()
