class createnode:
    def __init__(self,value):
        self.value=value
        self.lchild=None
        self.rchild=None
    
def insert(root,newnode):
    if root is None:
        root=createnode(newnode)
        return root
    if newnode<root.value:
        root.lchild=insert(root.lchild,newnode)
    else :
        root.rchild=insert(root.rchild,newnode)
    return root

def inorder(root):
    if root:
        inorder(root.lchild)
        print(root.value)
        inorder(root.rchild)

root=createnode(70)
root=insert(root,50)
root=insert(root,40)
root=insert(root,60)
root=insert(root,90)
root=insert(root,80)
root=insert(root,100)
inorder(root)