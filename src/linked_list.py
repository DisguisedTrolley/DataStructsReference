from typing import Any, Optional


class SLLNode:
    def __init__(self, value: Optional[Any] = None) -> None:
        self.val = value
        self.next: Optional["SLLNode"] = None


class SLList:
    def __init__(self):
        self.size = 0
        self.head: Optional["SLLNode"] = None
        self.tail: Optional["SLLNode"] = None

    """
    Pushes a value to the head of the list.
    Used in implementing a stack DS.

    Args:
        value: value that the Node holds.
    Returns:
        None
    """

    def push(self, value: Any) -> None:
        new_node = SLLNode(value)
        new_node.next = self.head

        self.head = new_node

        if self.size == 0:
            self.tail = new_node

        self.size += 1

        return

    """
    Pops value the head of the linked list.
    useful for both stack and queue implimentations.

    Args:
        None
    Returns:
        The head node's value.
    """

    def pop(self) -> Any:
        if self.size == 0:
            return None

        ret_value = self.head.val
        self.head = self.head.next

        self.size -= 1

        if self.size == 0:
            self.tail = None

        return ret_value

    """
    Same as the `pop` function.
    Used in queue operation only.
    
    Args: 
        None

    Returns:
        The head node's value.
    """

    def remove(self) -> Any:
        return self.pop()

    """
    Adds a node to the tail of the linked list.
    Used in implementation of queue operation.

    Args:
        Value: the value to be added to the list.

    Returns:
        True on successful entry.
    """

    def add(self, value: Any) -> bool:
        new_node = SLLNode(value)

        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

        return True

    def __repr__(self) -> str:
        ret_val = "["
        curr_node = self.head
        while curr_node:
            ret_val += f"{curr_node.val}, "
            curr_node = curr_node.next

        return ret_val + "]"
