import sys

from data_structures.linked_list import ListNode
from leets.linked_list.merge_two_sorted_lists_21 import merge_two_sorted_lists_21


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def generate_list(nodes):
    if not nodes:
        return None

    root = ListNode(nodes[0])
    cur_node = root
    for val in nodes[1:]:
        cur_node.next = ListNode(val)
        cur_node = cur_node.next

    return root


def main():
    t = int(input())
    for _ in range(t):
        l1_nodes = list(map(int, input().split()))
        l2_nodes = list(map(int, input().split()))
        l1 = generate_list(l1_nodes)
        l2 = generate_list(l2_nodes)
        print(merge_two_sorted_lists_21(l1, l2))
        print()


main()
