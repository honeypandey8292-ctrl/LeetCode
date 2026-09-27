# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Step 1: Ek dummy node create karte hain
        dummy = ListNode(-1)
        current = dummy
        
        # Step 2: Loop chala kar dono lists compare karte hain
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # Step 3: Jo list bach gayi hai use attach kar dete hain
        current.next = list1 if list1 else list2
        
        # Step 4: Final head return karte hain
        return dummy.next