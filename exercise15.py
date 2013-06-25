class BinaryTreeNode:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right=node

    def get_value(self):
        return self.value

    def set_value(self, number):
        self.value=number

def depth_first_traversal(node):
    # check to see if a node has children, if so, go there.
    #r=[]
    #if node.left != None:
   #      depth_first_traversal(node.left) 
   #      r.append(object)

   #  #if node.right != None:
   #      depth_first_traversal(node.right)
   # pass 
