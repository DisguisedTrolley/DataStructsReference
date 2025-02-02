from typing import Any


class ArrayQueue:
    def __init__(self, size: int):
        # Since this is implemented in python, it will be hilariously simple.
        # We don't have to worry about growing or shrinking the backing array.
        # Let's artificially limit the size of the backing array.
        # To simulate that, we will init the array with None type elements.
        self.backing_array = [None] * size
        self.arr_limit = size
        self.head = 0
        # The number of elements stored in the array.
        # for the purposes of this impl. The 'None' element is considered as no element.
        self.arr_size = 0

    def resize(self) -> None:
        new_array = [None] * max(1, (2 * self.arr_size))

        # Preferably use the inbuilt copy functionality in other languages to do this.
        for k in range(0, self.arr_size):
            new_array[k] = self.backing_array[(self.head + k) % self.arr_limit]

        self.backing_array = new_array
        self.head = 0
        self.arr_limit = max(1, 2 * self.arr_size)

    def add(self, value: Any) -> bool:
        # Check if the backing array is already full.
        # If it is already full, then call the resize method.
        if self.arr_size + 1 > self.arr_limit:
            self.resize()

        self.backing_array[(self.head + self.arr_size) % self.arr_limit] = value
        self.arr_size += 1

        return True

    def remove(self) -> Any:
        # Technically this is not necessary, because an "empty" array here only has 'None' values anyways.
        # To replicate a 'Index out of bounds' edge case, the folloing condition is added.
        if self.arr_size == 0:
            return None

        # get the value stored at the head of the array. This will be returned later.
        ret_value = self.backing_array[self.head]
        self.backing_array[self.head] = None

        # Increment the head to represent the next value in the queue.
        # And decrement the size of the array, because it has one less element now.
        self.head = (self.head + 1) % self.arr_limit
        self.arr_size -= 1

        # Resize if necessary.
        if self.arr_limit >= 3 * self.arr_size:
            self.resize()

        return ret_value

    def __repr__(self) -> str:
        return f"Array Elements: {self.backing_array}, Head: {self.head}, Size: {self.arr_size}, Max size: {self.arr_limit}"
