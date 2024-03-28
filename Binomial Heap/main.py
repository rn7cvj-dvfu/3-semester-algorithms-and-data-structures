class Node:
    def __init__(self, data):
        self.data = data
        self.degree = 0
        self.child = None
        self.sibling = None
        self.parent = None

def newNode(key):
    return Node(key)

def unionBionomialHeap(l1, l2):
    _new = []
    it = iter(l1)
    ot = iter(l2)

    while True:
        try:
            if not ot:
                _new.append(next(it))
            elif not it:
                _new.append(next(ot))
            elif it.__next__().degree <= ot.__next__().degree:
                _new.append(it.__next__())
            else:
                _new.append(ot.__next__())
        except StopIteration:
            break

    return _new

def mergeBinomialTrees(b1, b2):
    if b1.data > b2.data:
        b1, b2 = b2, b1

    b2.parent = b1
    b2.sibling = b1.child
    b1.child = b2
    b1.degree += 1

    return b1

def adjust(_heap):
    if len(_heap) <= 1:
        return _heap

    new_heap = []
    it1 = iter(_heap)
    it2 = iter(_heap[1:])
    it3 = iter(_heap[2:])

    while True:
        try:
            if it1.__next__().degree < it2.__next__().degree:
                new_heap.append(it1.__next__())
            elif it1.__next__().degree == it2.__next__().degree:
                new_heap.append(mergeBinomialTrees(it1.__next__(), it2.__next__()))
        except StopIteration:
            break

    return new_heap

def insertATreeInHeap(_heap, tree):
    temp = []
    temp.append(tree)
    temp = unionBionomialHeap(_heap, temp)
    return adjust(temp)

def removeMinFromTreeReturnBHeap(tree):
    heap = []
    temp = tree.child

    while temp:
        lo = temp
        temp = temp.sibling
        lo.sibling = None
        heap.insert(0, lo)

    return heap

def insert(_head, key):
    temp = newNode(key)
    return insertATreeInHeap(_head, temp)

def getMin(_heap):
    return min(_heap, key=lambda node: node.data)

def extractMin(_heap):
    new_heap = []
    temp = getMin(_heap)

    for node in _heap:
        if node != temp:
            new_heap.append(node)

    lo = removeMinFromTreeReturnBHeap(temp)
    new_heap = unionBionomialHeap(new_heap, lo)
    new_heap = adjust(new_heap)
    return new_heap

def printTree(h):
    while h:
        print(h.data, end=" ")
        printTree(h.child)
        h = h.sibling

def printHeap(_heap):
    for node in _heap:
        printTree(node)

_heap = []
_heap = insert(_heap, 10)
_heap = insert(_heap, 20)
_heap = insert(_heap, 30)
_heap = insert(_heap, 40)
_heap = insert(_heap, 50)
_heap = insert(_heap, 60)
_heap = insert(_heap, 70)

print("Heap elements after insertion:")
printHeap(_heap)

temp = getMin(_heap)
print("\nMinimum element of heap", temp.data)

_heap = extractMin(_heap)
print("Heap after deletion of minimum element")
printHeap(_heap)