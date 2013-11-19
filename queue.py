class Queue(object):
    def __init__(self):
        self.data = []
    
    def put(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[0]
        del self.data[0]
        return item

    def __len__(self):
        return len(self.data)

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
