# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:59:30 2026

@author: reina
"""

"""
A recursive function to count items in a linked list.
"""

class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
        
class linkedlist():
    def __init__(self,val):
        self.head=Node(val)
    
    def add(self,val):
        curr_node=self.head
        while curr_node.next!=None:
            curr_node=curr_node.next
        curr_node.next=Node(val)
        
    def __len__(self):
        def helper(node):
            if not node:
                return 0
            return 1+helper(node.next)
        return helper(self.head)
    
    def __repr__(self):
        values=[]
        curr_node=self.head
        while curr_node!=None:
            values.append(curr_node.val)
            curr_node=curr_node.next
        return f"{values}"
    
    
if __name__ == '__main__':
    ll=linkedlist(2)
    ll.add(3)
    ll.add(4)
    ll.add(11)
    print(ll)
    print(len(ll))