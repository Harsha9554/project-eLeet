# basically 2 pointers

# None, 1 -> 2 -> 3 -> 4 -> 5 -> None
#  p    c
#       p    c
#            p    c
#                 p    c
#                      p    c

# bond changes are done on current node

# like this,    1 -> 2 -> 3 -> 4
#               p    c

#               1 <- 2 -x-> 3 -> 4
#               p    c

#               1 <- 2 <- 3 -x-> 4
#                    p    c


# but the magic happens before you sever the cur.next bond
# by making it cur.next = prev.
# save the cur.next in temp

# loop condition is cur

# prev becomes cur
# it is like prev++, cur++ but links changed.


def reverse_linked_list_206(head):
    if not head or not head.next:
        return head

    prev, cur = None, head
    temp = cur

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return prev
