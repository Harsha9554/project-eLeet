import sys

from data_structures.linked_list import ListNode
from leets.linked_list.reverse_linked_list_206 import reverse_linked_list_206


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
        nodes = list(map(int, input().split()))
        root = generate_list(nodes)
        print(reverse_linked_list_206(root))


main()
