def merge_two_sorted_lists_21(l1, l2):
    if not l1 and not l2:
        return l1

    if l1 and not l2:
        return l1

    if l2 and not l1:
        return l2

    p1 = l1
    p2 = l2

    if p1.val <= p2.val:
        p3 = p1
        p1 = p1.next
    else:
        p3 = p2
        p2 = p2.next

    ans = p3

    while p1 and p2:
        if p1.val <= p2.val:
            p3.next = p1
            p1 = p1.next
        else:
            p3.next = p2
            p2 = p2.next
        p3 = p3.next

    if p1:
        p3.next = p1

    if p2:
        p3.next = p2

    return ans
