class Node:
 
    # Constructor to create a new node
    def __init__(self, value):
        self.v  = value
        self.l = None
        self.r = None
 
# Find Successor function
def findSuccessor(root, value):
 
    if root is None:
        return
 
    # If value is at root
    if root.v == value: 
 
      
        if root.r is not None:
            tmp = root.r
            while(tmp.l):
                tmp = tmp.l
            findSuccessor.suc = tmp
 
        return
 
    if root.v > value :
        findSuccessor.suc = root
        findSuccessor(root.l, value)
 
    else: 
        findSuccessor.pre = root
        findSuccessor(root.r, value)

def add(node , value):
    if node is None:
        return Node(value)
 
    if value < node.v:
        node.l = add(node.l, value)
 
    else:
        node.r = add(node.r, value)
 
    return node

 
root = None
root = add(root, 3)
add(root, 4);
add(root, 0);
add(root, 8);
add(root, 2);
add(root, 6);
add(root, 10);

findSuccessor.suc = None

value = 4
findSuccessor(root,value)
print ("Successor of", value ,"is", findSuccessor.suc.v)
