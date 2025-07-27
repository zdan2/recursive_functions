from perfect_tree import create_tree

def search_bst(node, target):
    if node is None:
        return None
    if node.value == target:
        return node
    elif target < node.value:
        return search_bst(node.left, target)
    else:
        return search_bst(node.right, target)

tree=create_tree(15)
print(tree.left.left.left.value)
r=search_bst(tree,5)
print(r)

def preorder(node):
    if node is None:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)

preorder(tree)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)

inorder(tree)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)

postorder(tree)
