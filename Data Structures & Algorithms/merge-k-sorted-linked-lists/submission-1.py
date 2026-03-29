# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoList(list1, list2):
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next

            if list1:
                tail.next = list1
            elif list2:
                tail.next = list2
                
            return dummy.next

        if len(lists) ==0 or not lists[0]:
            return None
        
        dummy = mergeTwoList(lists[0], lists[1])
        for i in range(2,len(lists)):
            dummy = mergeTwoList(dummy, lists[i])

        return dummy