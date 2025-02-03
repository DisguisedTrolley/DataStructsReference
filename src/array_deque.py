from typing import Any, List


class ArrayDeque:
    def __init__(self) -> None:
        # Initialize a backing array and a variable to keep track of it's limit.
        # The limit variable is used here because it's cleaner than calling len(self.backing_array)
        # each time we need the max size the array can hold as there is no way in python to limit a list to a particular size.
        self.backing_array: List[Any] = [None] * 1
        self.array_limit = len(self.backing_array)

        # Variable to hold the size of the array is required as None elements are
        # considered as no elements for the purposes of our implementation.
        # calling len(self.backing_array) will return the array_limit which includes the None values.
        self.head = 0
        self.array_size = 0

    def get(self, index: int) -> Any:
        val = self.backing_array[(self.head + index) % self.array_limit]
        return val

    def set(self, index: int, value: Any) -> Any:
        original_val = self.backing_array[(self.head + index) % self.array_limit]
        # Set the new value.
        self.backing_array[(self.head + index) % self.array_limit] = value

        return original_val

    def add(self, index: int, value: Any) -> None:
        return

    def __repr__(self) -> str:
        return f"Array: {self.backing_array}, Limit: {self.array_limit}, Size: {self.array_size}"
