#Binary Tree 
#Rules: 
#nodes can have 0 1 or 2 parents
#each child can have 1 parent 
#prefect binary tree = 2 children or none 
    #sum of nodes on last level = sum of nodes above + 1
#full node has 2 or none
'''
    # of nodes = 2^h - 1; 
    log nodes = height

    Binary search tree Balanced vs Unbalanced 
    Balananced - log(n)
    unbalanced - O(n)

    pros BST 
        better tahn O(n)
        ordered 
        flexible size
    cons BST 
        NO O(1) operations 
'''

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)

        else:
            currNode = self.root
            prevNode = self.root
            while currNode:
                if currNode.data >= data:
                    prevNode = currNode
                    currNode = currNode.left
                else:
                    prevNode = currNode
                    currNode = currNode.right
            if prevNode.data >= data:
                prevNode.left = Node(data)
            else:
                prevNode.right = Node(data)

    def lookup(self, data):
        currNode = self.root
        while currNode:
            if currNode.data == data:
                return True
            if currNode.data >= data:
                currNode = currNode.left
            else: 
                currNode = currNode.right
        return False

    def remove(self, data):
        return False

'''       
tree = BST()
print(tree.lookup(170))  
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
'''
#AVL Tree 
#Red Black Tree 
'''
tree automatically balances themselves out
'''


#Binary Heap 
#two children 
'''
    max heap 
    min heap 
    top level greated than bottom 
    O(n) - look up 
    O(logN) - insert
    O(logN) - delete 

    less ordered left or right only upper level is greated 
    Data storage and prioity heaps 
    add left to right 
        preserve order of insert 
        can implement with arrays 
        memory efficient 

Priority Queues 
    a type of data where each element has a priority 
    Emergency room example 
    Airplane boarding - captin before passenger 
    Better than O(m)
    priority 
    flexible size
    fast inserts - usually
    cons: 
        slow look up

'''

#Trie
'''
    specialized tree used in searching most often in text 
    empty root node
    prefix trsee 
        problems specific to strings 
    search engines 
    IP routing 
    speed and space 
    finding a word 
    O(length of the word)
    space complexity save a lot of space by reusing letters 
'''