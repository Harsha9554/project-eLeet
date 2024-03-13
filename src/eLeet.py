import sys

from leets.sliding_window.best_time_to_buy_and_sell_stock_121 import (
    best_time_to_buy_and_sell_stock_121,
)


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    t = int(input())
    for _ in range(t):
        stocks = list(map(int, input().split()))
        print(best_time_to_buy_and_sell_stock_121(stocks))


main()
