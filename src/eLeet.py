import sys

sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        print(x**2)


main()
