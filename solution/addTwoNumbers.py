# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l2Str = l1Str = ''
        while l1.next != None:
            l1Str += str(l1.val)
            l1 = l1.next
        l1Str += str(l1.val)

        while l2.next != None:
            l2Str += str(l2.val)
            l2 = l2.next
        l2Str += str(l2.val)
        total = int(l1Str[::-1]) + int(l2Str[::-1])
        return [int(i) for i in str(total)[::-1]]



if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()
    print(solution.addTwoNumbers(l1,l2))