"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

class LinkedList():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next

class Solution():
      def merge_list(self,list1,list2):
          head = LinkedList()
          current = head

          while list1 and list2:
              if list1.val < list2.val:
              
                  current.next= list1
                  list1 = list1.next

              else:
                  current.next= list2
                  list2 = list2.next
              current = current.next
          current.next = list1 or list2

          return head.next

    
        
        
        
