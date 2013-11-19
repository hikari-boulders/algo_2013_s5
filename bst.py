class Bst(object):
    def __init__(self):
        self.root = []
    
    def _height(self, tree, depth):
        if tree:
            depth += 1
            l = self._height(tree[1], depth)
            r = self._height(tree[2], depth)
            return max(l, r)            
        return depth
            
    def height(self):
        return self._height(self.root, 0)

    def insert(self, data):
        """ insert node """
        if data is None:
            return
        node = self.root
        while node:
            d, l, r = node
            if d > data:
                node = l
            else:
                node = r
        node[:] = [data, [], []]
        if not self.is_balanced():
            self.balance()

    def is_balanced(self):
        lh = self._height(self.root[1], 0)
        rh = self._height(self.root[2], 0)
        
        if abs(lh - rh) > 1:
            return False        

    def _values(self, tree):
        if tree:
            yield tree[0]
            for i in self._values(tree[1]):
                if i is not None:
                    yield i
            for i in self._values(tree[2]):
                if i is not None:
                    yield i       

    def values(self):
        return list(self._values(self.root))

    def _get_balanced(self, values):
        """ values have to be sorted """
        if values:
            i = len(values)//2
            r = values[i]
            return [r, self._get_balanced(values[0:i]),
                    self._get_balanced(values[i+1:])]
        return []

    def balance(self):
        """ balance the tree out """
        
        # find avg element and set it as the new
        # root -> then add the rest of the values
        # in a good way... 

        self.root = self._get_balanced(
            sorted(self.values()))

    def _find(self, tree, data):
        """ Find with different root """ 
        if tree is None:
            return tree
        elif data == tree[0]:
            return tree
        elif data < tree[0]:
            return self._find(tree[1], data)
        else:
            return self._find(tree[2], data)

    def find(self, data):
        """ Find with data """
        node = self.root
        return self._find(node, data) 
        
    def remove(self, data):
        """ Removes first node with `data` """
        node = self.find(data)
        self.remove_node(node)

    def _find_min(self, tree):
        node = tree
        while node and node[1]:
            node = node[1]
        return node

    def _del(self, node, parent):
        pass

    def _remove_node(self, tree, node):
        if tree is None:
            return tree
        elif node == tree:
            d, l, r = node
            if l and r:
                # find minimum in right subtree
                succ = self._find_min(r)
                # replace current value with succ
                # value
                node[0] = succ[0]
                # remove the successor
                self._remove_node(r, succ)
            elif not l and not r: # leaf
                node[:] = []
            elif not l:
                # replace current
                node[:] = r
            elif not r:
                node[:] = l
        elif node[0] < tree[0]:
            return self._remove_node(tree[1], node)
        else:
            return self._remove_node(tree[2], node) 

    def remove_node(self, node):
        """ Removes the given node """
        if node is None:
            return None
        return self._remove_node(self.root, node)
           
    def _pprint(self, node, max_depth, show_key, spacer=2):
        """
        Returns a (top_lines, mid_line, bot_lines) tuple,
        """
        if max_depth == 0:
            return ([], '- ...', [])
        elif not node:
            return ([], '- EMPTY', [])
        else:
            top_lines = []
            bot_lines = []
            mid_line = '-%r' % node[0]
            if len(node) > 3: mid_line += ' (key=%r)' % node[0]
            if node[2]:
                t,m,b = self._pprint(node[2], max_depth-1,
                                     show_key, spacer)
                indent = ' '*(len(b)+spacer)
                top_lines += [indent+' '+line for line in t]
                top_lines.append(indent+'/'+m)
                top_lines += [' '*(len(b)-i+spacer-1)+'/'+' '*(i+1)+line
                              for (i, line) in enumerate(b)]
            if node[1]:
                t,m,b = self._pprint(node[1], max_depth-1,
                                     show_key, spacer)
                indent = ' '*(len(t)+spacer)
                bot_lines += [' '*(i+spacer)+'\\'+' '*(len(t)-i)+line
                              for (i, line) in enumerate(t)]
                bot_lines.append(indent+'\\'+m)
                bot_lines += [indent+' '+line for line in b]
            return (top_lines, mid_line, bot_lines)

    def pprint(self, max_depth=10, frame=True, show_key=True):
        """
        Return a pretty-printed string representation of this binary
        search tree.
        """
        t,m,b = self._pprint(self.root, max_depth, show_key)
        lines = t+[m]+b
        if frame:
            width = max(40, max(len(line) for line in lines))
            s = '+-'+'MIN'.rjust(width, '-')+'-+\n'
            s += ''.join('| %s |\n' % line.ljust(width) for line in lines)
            s += '+-'+'MAX'.rjust(width, '-')+'-+\n'
            return s
        else:
            return '\n'.join(lines)

if __name__ == '__main__':
    bt = Bst()
    bt.insert(0)
    bt.insert(10)
    bt.insert(14)
    bt.insert(5)
    bt.insert(4)
    bt.insert(6)
    print(bt.pprint())
    
    bt.remove(5)
    print(bt.pprint())
    
    bt.insert(5)
    bt.insert(7)
    bt.insert(8)
    bt.insert(9)
    print(bt.pprint()) 

    print(bt.height()) 

    print(bt.is_balanced())
    print(bt.values())
    print(bt.balance())
    print(bt.pprint()) 

    print(bt.find(10))
