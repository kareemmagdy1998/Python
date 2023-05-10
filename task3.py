class queue:

   def __init__(self, l): 
    self.l = l

   def enqueue(self,n):
        self.l.insert(len(self.l),n)

   def dequeue(self):
        self.l.pop(0)

   def is_empty(self):
       if len(self.l) == 0:
           return True
       else:
           return False    
            
l=[0,1,2,3]
q=queue(l)
q.enqueue(4)
print(l)
q.dequeue()
print(l)
print(q.is_empty())
print(q.l)


class modified_queue(queue):
    def __init__ (self,name,size,l):
        super(modified_queue,self).__init__(l)
        self.name=name
        self.size=size

    def enqueue(self,n):
        if len(self.l) >= self.size:
            raise IndexError("out of index range")
        else:
            self.l.insert(len(self.l),n)    
    
q2=modified_queue("q2",5,l)
q2.enqueue(5)
q2.enqueue(6)
print(l)
        
        
           