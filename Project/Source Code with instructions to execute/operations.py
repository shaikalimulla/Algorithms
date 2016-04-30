#Class to represent the node of the AVL Tree  
class avlNode(object):
    '''
    #Function to initialize the values of the nodes of the AVL Tree  
    #Input: None
    #Output: None 
    '''
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    '''
    #Function to display the content of the nodes of the AVL Tree  
    #Input: None
    #Output: None 
    '''
    def __str__(self):
        return str(self.key)

#Class to represent operations of the AVL Tree  
class avlTree(object):   
    '''
    #Function to initialize the nodes and values of the AVL Tree  
    #Input: None
    #Output: None 
    '''
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    '''
    #Function to insert entry in the AVL tree  
    #Input: Self or Current object and inputValue which need to be inserted  
    #Output: None 
    '''
    def insertEntryInTree(self, inputValue):
        node = avlNode(inputValue)
 
        if (not self.node):
            self.node = node
            self.node.left = avlTree()
            self.node.right = avlTree()
        elif (inputValue[0] > self.node.key[0]):
            self.node.right.insertEntryInTree(inputValue)
        elif (inputValue[0] < self.node.key[0]):
            self.node.left.insertEntryInTree(inputValue)
            
        self.balanceAVLTree()

    '''
    #Function to search entry in the AVL tree  
    #Input: Self or Current object and inputValue which need to be looked in tree  
    #Output: Node we are looking for if it present in the tree else none 
    '''
    def searchEntryInTree(self, inputValue):
        output = []
        
        while ((self.node is not None)):
            val = self.node.key[0]
            if (inputValue < val):
                self = self.node.left
            elif (inputValue > val):
                self = self.node.right
            else:
                output.append(self.node.key)
                break;        

        return output

    '''
    #Function to search entry in the AVL tree  
    #Input: Self or Current object, inputValue which need to be deleted in tree and variable indicates entry is found or not  
    #Output: None 
    '''
    def deleteEntryInTree(self, inputValue, isEntryFound):
        if (self.node != None):
            if (self.node.key[0] == inputValue):
                isEntryFound.append(True)
                if (not self.node.left.node and not self.node.right.node):
                    self.node = None
                elif (not self.node.left.node):                
                    self.node = self.node.right.node
                elif (not self.node.right.node):
                    self.node = self.node.left.node
                else:
                    successor = self.node.right.node  
                    while (successor and successor.left.node):
                        successor = successor.left.node
 
                    if (successor):
                        self.node.key[0] = successor.key[0]
 
                        self.node.right.deleteEntryInTree(successor.key[0], isEntryFound)
 
            elif (inputValue < self.node.key[0]):
                self.node.left.deleteEntryInTree(inputValue, isEntryFound)
 
            elif (inputValue > self.node.key[0]):
                self.node.right.deleteEntryInTree(inputValue, isEntryFound)

            self.balanceAVLTree()
        
    '''
    #Function to balance all the nodes of the AVL tree  
    #Input: Self or Current object   
    #Output: None 
    '''
    def balanceAVLTree(self):
        self.updateTreeHeights(isRecursive=False)
        self.updateTreeBalances(False)

        while (self.balance < -1 or self.balance > 1): 
            if (self.balance < -1):                
                if (self.node.right.balance > 0):
                    self.node.right.rotateTreeToRight()
                    self.updateTreeHeights()
                    self.updateTreeBalances()
 
                self.rotateTreeToLeft()
                self.updateTreeHeights()
                self.updateTreeBalances()

            if (self.balance > 1): 
                if (self.node.left.balance < 0):
                    self.node.left.rotateTreeToLeft()
                    self.updateTreeHeights()
                    self.updateTreeBalances()
 
                self.rotateTreeToRight()
                self.updateTreeHeights()
                self.updateTreeBalances()

    '''
    #Function to rotate nodes of the tree to left  
    #Input: Self or Current object   
    #Output: None 
    '''
    def rotateTreeToLeft(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node
 
        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    '''
    #Function to rotate nodes of the tree to right  
    #Input: Self or Current object  
    #Output: None 
    '''
    def rotateTreeToRight(self):
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node
 
        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    '''
    #Function to update heights of the nodes of the tree   
    #Input: Self or Current object  
    #Output: None 
    '''
    def updateTreeHeights(self, isRecursive=True):
        if (self.node): 
            if (isRecursive): 
                if (self.node.left): 
                    self.node.left.updateTreeHeights()
                if (self.node.right):
                    self.node.right.updateTreeHeights()
            
            self.height = 1 + max(self.node.left.height, self.node.right.height)

        else: 
            self.height = -1
 
    '''
    #Function to update balances of the nodes of the tree  
    #Input: Self or Current object  
    #Output: None 
    '''
    def updateTreeBalances(self, isRecursive=True):
        if (self.node):
            if (isRecursive):
                if (self.node.left):
                    self.node.left.updateTreeBalances()
                if (self.node.right):
                    self.node.right.updateTreeBalances()
 
            self.balance = self.node.left.height - self.node.right.height

        else:
            self.balance = 0 

    '''
    #Function to display nodes of the tree   
    #Input: Self or Current object, node and level of the tree  
    #Output: None 
    '''
    def display(self, node=None, level=0):
        if (not node):
            node = self.node
            file = open('result.txt', 'w')
            file.close()            
 
        file = open('result.txt', 'a')
        
        if (not self.node):
            print ("Error!!! No Nodes exist in the tree")
            return                

        if (node.right.node):
            self.display(node.right.node, level + 1)

            for _ in range(0, level):
                file.write("\t")                
            file.write("    /")    
            file.write("\n")

        for _ in range(0, level):
            file.write("\t")                
        file.write(str(node))
        file.write("\n")                
        file.close()
                
        if (node.left.node):
            if file.closed:
                file = open('result.txt', 'a')

            for _ in range(0, level):
                file.write("\t")                
            file.write("    \\")    
            file.write("\n")
            file.close()                
            self.display(node.left.node, level + 1)

    '''
    #Function to return in-order traversal of the tree   
    #Input: Self or Current object  
    #Output: In-order traversal of the tree 
    '''
    def inorderTreeTraversal(self):
        result = []
 
        if (not self.node):
            return result
        
        result.extend(self.node.left.inorderTreeTraversal())
        result.append(self.node.key)
        result.extend(self.node.right.inorderTreeTraversal())
 
        return result