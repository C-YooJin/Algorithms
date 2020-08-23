class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        curn = l1
        num = 1
        pre_num = 0

        while curn:
            pre_num += curn.val * num
            num *= 10
            curn = curn.next

        curn = l2
        num = 1
        post_num = 0

        while curn:
            post_num += curn.val * num
            num *= 10
            curn = curn.next

        result = pre_num + post_num

        head = None
        for i in reversed(str(result)):
            print(i)
            if not head:
                head = ListNode(int(i))
                curn = head
            else:
                curn.next = ListNode(int(i))
                curn = curn.next

        return head


