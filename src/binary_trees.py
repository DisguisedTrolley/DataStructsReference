from typing import Any, List, Optional

from array_queue import ArrayQueue


class TreeNode:
    def __init__(self, value: Optional[Any] = None):
        self.val = value
        self.parent: Optional["TreeNode"] = None
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None

    def __eq__(self, value: "TreeNode") -> bool:
        return self.val is not None and self.val == value.val

    def __ne__(self, value: "TreeNode") -> bool:
        return self.val is not None and self.val != value.val

    def __lt__(self, value: "TreeNode") -> bool:
        return self.val is not None and self.val < value.val

    def __gt__(self, value: "TreeNode") -> bool:
        return self.val is not None and self.val > value.val

    def __le__(self, value: "TreeNode") -> bool:
        return self.val and self.val <= value.val

    def __ge__(self, value: "TreeNode") -> bool:
        return self.val and self.val >= value.val


class BSTree:
    def __init__(self):
        # We need to track the size of the tree and it's root node.
        self.__size = 0
        self.__root: Optional["TreeNode"] = None

    def find_eq(self, val: Any) -> TreeNode | None:
        current_node = self.__root

        while current_node is not None:
            if val < current_node.val:
                current_node = current_node.left
            elif val > current_node.val:
                current_node = current_node.right
            else:
                return current_node

        return None

    def add(self, val: Any) -> None:
        # Create a node from the value.
        node = TreeNode(val)
        # Find the node that will be the parent node of the target node.
        parent = self.__find_last(node)
        # Add the target node to the left or right of the parent node.
        return self.__add_child(parent, node)

    # Find and return the node we want to add, if it exists, don't add it.
    # If it doesn't exist, return the parent of our to-be value.
    def __find_last(self, node: TreeNode) -> TreeNode:
        # Start at the root.
        current_node = self.__root
        # The root doesn't have any parents. Set it to none.
        parent = None

        # Iterate over all nodes from the current root till we find target node or something close.
        while current_node is not None:
            # Set the parent to be the current node and then traverse down.
            parent = current_node

            if node < current_node:
                current_node = current_node.left
            elif node > current_node:
                current_node = current_node.right
            else:
                # when target and current nodes are equal, just return the current node as is.
                return current_node

        # If the current node is none, the target value was not found.
        # Return the target's parent value instead.
        return parent

    # Given a parent node and a new node,
    # Add the new node as a child to the parent node.
    def __add_child(self, parent: TreeNode, new: TreeNode) -> bool:
        # if there is no parent node, make new node the root node.
        if parent is None:
            self.__root = new
        else:
            # If the new node is greater than the parent, add it to the right.
            if new > parent:
                parent.right = new
            # If the new node is lesser than the parent, add it to the left.
            elif new < parent:
                parent.left = new

            # If the new node is equal to parent. Return False as there can be no duplicates.
            else:
                return False

            new.parent = parent

        self.__size += 1
        return True

    def remove(self, node: TreeNode) -> None:
        if not node.left or not node.right:
            self.__splice(node)

        else:
            # goto the right branch
            # get the leftmost value of the right branch
            current_node = node.right
            while current_node.left is not None:
                current_node = current_node.left

            node.val = current_node.val
            self.__splice(current_node)

    def __splice(self, node: TreeNode) -> None:
        # Splicing a node is only possible when the target node has only one child,
        # Or the target node is a leaf node.
        # Start by tracking the to be chil_node and its parent node.
        new_node = None
        parent = None

        # check if the target node has a left node.
        # If it does have one, make the left node the new node.
        if node.left:
            node.left = new_node
        # Repeat the same for right node.
        else:
            # Sets the right node to a node value if it exists, None otherwise
            node.right = new_node

        # If the given node is the root node, then just make the root node as the new node.
        # If the tree contains only the root node, then just remove the root node by setting it to None.
        if node == self.__root:
            self.__root = new_node

        # Any other node has a parent node.
        # Start by tracking the parent.
        else:
            parent = node.parent

            # Check which side of the parent our target node was present.
            # Set that side of the parent to the new node.
            if parent.left == node:
                parent.left = new_node
            else:
                parent.right = new_node

        # If after all this, a new node was present, set it's parent to the previous node's parent to complete the link.
        if new_node is not None:
            new_node.parent = parent

        # reduce the overall size of the tree by one node.
        self.__size -= 1

    def bf_trvel_range(self, lower: TreeNode, upper: TreeNode) -> List[Any]:
        q = ArrayQueue()
        if self.__root:
            q.add(self.__root)

        in_range_nodes = []
        visited_nodes = []

        while q.size() > 0:
            node: TreeNode = q.remove()
            visited_nodes.append(node.val)

            if node.left and node > lower:
                q.add(node.left)

            if lower <= node <= upper:
                in_range_nodes.append(node.val)

            if node.right and node < upper:
                q.add(node.right)

        print(visited_nodes)
        return in_range_nodes

    def bt_travel(self):
        q = ArrayQueue()
        if self.__root:
            q.add(self.__root)

        while q.size() > 0:
            node: TreeNode = q.remove()

            print(node.val)

            if node.left:
                q.add(node.left)

            if node.right:
                q.add(node.right)
