class NewNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_closest_val_bst(tree,target,closest):
    """
    Finding the closest number in a Binary Search tree
    given a target value
    Args:
        tree (bst): binary search tree node
        target (int): target value
        closest (infinit): infinit value
    """
    current_node = tree

    while current_node is not None:
        if current_node is None:
            return closest
        if abs(target-closest) > abs(target - current_node.data):
            closest = current_node.data
        if target < current_node.data:
            current_node = current_node.left
        elif target > current_node.data:
            current_node = current_node.right
        else:
            break
    return closest

root = NewNode(10)
root.left = NewNode(5)
root.left.left = NewNode(2)
root.left.right = NewNode(5)
root.left.left.left = NewNode(1)
root.right = NewNode(15)
root.right.left = NewNode(13)
root.right.right = NewNode(22)

print(find_closest_val_bst(root,12,float('inf')))