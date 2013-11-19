class Stack(object):
    def __init__(self):
        self.data = []
    
    def put(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        return item

    def __len__(self):
        return len(self.data)

    @property
    def empty(self):
        return not bool(len(self))
    

if __name__ == '__main__':
    s = Stack()
    s.put(1)
    s.put(2)
    s.put(3)
    assert len(s) == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert len(s) == 0
    assert s.empty
    s.put(3)
    s.put(2)
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 3
