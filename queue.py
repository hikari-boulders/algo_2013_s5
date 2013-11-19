class Node(object):
    def __init__(self, data=None, succ=None, prec=None):
        self.data=data
        self.succ=succ
        self.prec=prec

class Queue(object):
    def __init__(self):
        root = Node()
        root.succ = root
        root.prec = root
        self.root = root        

    def put(self, item):
        r = self.root
        last = r.prec
        node = Node(data=item)
        node.succ = last.succ        
        last.succ.prec=node
        last.succ = node
        node.prec = last

    def pop(self):
        r = self.root
        first = r.succ
        if first != r:
            node = first
            first.prec.succ = first.succ
            first.succ.prec = first.prec        
            return node.data            

    def __len__(self):
        i = 0
        r = self.root
        succ = r.succ
        while succ != r:
            i+=1
            succ = succ.succ
        return i

    @property
    def empty(self):
        return not bool(len(self))

if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    assert len(q) == 3
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert len(q) == 0
    assert q.empty
    q.put(2)
    q.put(4)
    assert q.pop() == 2
    assert q.pop() == 4
