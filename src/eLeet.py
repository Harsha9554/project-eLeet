import sys

from leets.arrays_and_hashing.top_k_frequent_elements_347 import (
    top_k_frequent_elements_347,
    top_k_frequent_elements_347_ii,
)


sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        strs = list(map(str, input().split()))
        k = int(input())
        print(top_k_frequent_elements_347_ii(strs, k))


main()
