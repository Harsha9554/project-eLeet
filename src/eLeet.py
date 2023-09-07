import sys

from leets.arrays_and_hashing.valid_anagram_242 import valid_anagram_242


sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        x, y = map(str, input().split())
        valid_anagram_242(x, y)


main()
