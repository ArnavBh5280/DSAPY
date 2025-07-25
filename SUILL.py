# IMPLEMENATION OF STACK BY INHERITING SINGLY LINKED LIST

# 1. Import module containing singly linked list code in your python file.
# 2. Define a class Stack to implement stack data structure by inheriting SLL class.
# 3. Define a method is_empty() to check if the stack is empty in Stack class.
# 4. In Stack class, define push() method to add data onto the stack.
# 5. In Stack class, define pop() method to remove top element from the stack.
# 6. In Stack class, define peek() method to return top element on the stack.
# 7. In Stack class, define size() method to return size of the stack that is number of items present in the stack.

from SLL import *

class Stack(SLL):
    def __init__(self):
        self.item_count=0
        
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
        
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
            
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack Underflow")
        
    def size(self):
        return self.item_count 
        
        
            
        