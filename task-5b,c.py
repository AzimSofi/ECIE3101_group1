class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def deepestBranch(self):
        depth = 0
        while self.left:
            depth += 1
            return
        while self.right:
            depth += 1
            return

        return

def printPreorder(node):
    if node:
        print("-->",node.val, end=" ")
        printPreorder(node.left)
        printPreorder(node.right)

def printInorder(node):
    if node:
        printInorder(node.left)
        print("-->",node.val, end=" ")
        printInorder(node.right)

def printPostorder(node):
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print("-->",node.val, end=" ")

# BINARY SORT

def insertSort(node,val):
    if node is None:
        return Node(val)
    else:
        if node.val is val:
            return node
        elif node.val < val:
            node.right = insertSort(node.right, val)
        else:
            node.left = insertSort(node.left, val)
    return node



# Test
root = Node('Haziman Sairin')
insertSort(root,'Zikri Hakim')
insertSort(root,'Jameel Majdi')
insertSort(root,'Raniya Waleed')
insertSort(root,'Syukri Talib')
insertSort(root,'Saif al-Din')
insertSort(root,'Nuqman Aliff')
insertSort(root,'Abd al-Karim Mumtaz')
insertSort(root,'Kizzy Harriette')
insertSort(root,'Zharif Aiman')
insertSort(root,'Sharifa Harun')
insertSort(root,'Najma Fuad')
insertSort(root,'Amir Su\'ad')
print("Preorder: ")
printPreorder(root)
print("\nInorder: ")
printInorder(root)
print("\nPostorder: ")
printPostorder(root)
# root.deepestBranch()
