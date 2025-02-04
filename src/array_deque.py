from typing import Any, List


class ArrayDeque:
    def __init__(self) -> None:
        # Initialize a backing array and a variable to keep track of it's limit.
        # The limit variable is used here because it's cleaner than calling len(self.backing_array)
        # each time we need the max size the array can hold as there is no way in python to limit a list to a particular size.
        self.backing_array: List[Any] = [None]
        self.array_limit = 1
        # calling len(self.backing_array) will return the array_limit which includes the None values.
        self.head = 0
        self.array_size = 0

    def resize(self) -> None:
        new_array = [None] * max(1, 2 * self.array_size)
        for k in range(self.array_size):
            new_array[k] = self.backing_array[(self.head + k) % self.array_limit]

        self.backing_array = new_array
        self.head = 0
        self.array_limit = len(self.backing_array)

    def get(self, index: int) -> Any:
        # TODO: Add index out of range exception
        val = self.backing_array[(self.head + index) % self.array_limit]
        return val

    def set(self, index: int, value: Any) -> Any:
        # TODO: Add index out of range exception
        original_val = self.backing_array[(self.head + index) % self.array_limit]
        self.backing_array[(self.head + index) % self.array_limit] = value

        return original_val

    def add(self, index: int, value: int) -> None:
        # Check if the array has full. If yes, resize.
        if self.array_size == self.array_limit:
            self.resize()

        # Check if the index to be inserted at is less than half the array size.
        # If it is, then we shift all the elements from 0 to index - 1 to left by one position.
        if index < int((self.array_size) / 2):
            # Decerement the head pointer by 1
            # Mod operator is used is head is already at 0, the new head value will wrap around to the end.
            self.head = (self.head - 1) % self.array_limit
            for k in range(index):
                new_val = self.backing_array[(self.head + k + 1) % self.array_limit]
                self.backing_array[(self.head + k) % self.array_limit] = new_val

        # If index is greater than half the array size,
        # shift all the elements from index + 1 to n(included) right by one place
        else:
            for k in range(self.array_size, index, -1):
                new_val = self.backing_array[(self.head + k - 1) % self.array_limit]
                self.backing_array[(self.head + k) % self.array_limit] = new_val

        # Append the new value to the now emptied slot.
        self.backing_array[(self.head + index) % self.array_limit] = value
        self.array_size += 1

        return

    def remove(self, index: int) -> Any:
        # Save the element to remove.
        rem_val = self.backing_array[(self.head + index) % self.array_limit]

        if index < int(self.array_size / 2):
            # The range start from where the new array starts holding the values from.
            # if the original values are in indices 0, 1, 2, and they have to be moved right,
            # The new values should start from the higher value and move back, that is, the new indices are 3, 2, 1.

            for k in range(index, 0, -1):
                new_val = self.backing_array[(self.head + k - 1) % self.array_limit]
                self.backing_array[(self.head + k) % self.array_limit] = new_val

            self.head = (self.head + 1) % self.array_limit

        else:
            for k in range(index, self.array_size):
                new_val = self.backing_array[(self.head + k + 1) % self.array_limit]
                self.backing_array[(self.head + k) % self.array_limit] = new_val

        self.array_size -= 1

        if self.array_limit >= 3 * self.array_size:
            self.resize()

        return rem_val

    def __repr__(self) -> str:
        ret_string = "["
        for k in range(self.array_size):
            ret_string += f" {self.get(k)},"

        return ret_string + "]"
