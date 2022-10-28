# CREATE A LINKED LIST:
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class ll:
    def __init__(self):
        self.head=None
        
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        
        
    def print_linkedlist(self):
        if self.head is not None:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
            
           
        else:
             print('linked list is empty')
            
ll1=ll()

ll1.add_begin(10)
ll1.add_begin(9)
ll1.add_begin(8)
ll1.print_linkedlist()

        
    
       
        
        
    
       

        

        
        
        
