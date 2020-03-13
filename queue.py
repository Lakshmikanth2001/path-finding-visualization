#queue Data structure
print('queue ds is imported')
class Queue:
    def __init__(self):
        self.q=list()
    def push(self,x):
        self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            print('queue is empty')
            return None
        else:
            del(self.q[0])
            return None
    def isempty(self):
        if len(self.q)==0:
            return True
        else:
            return False
    def front(self):
        if len(self.q)!=0:
            return self.q[0]
        else:
            print('queue is empty')
            return None
