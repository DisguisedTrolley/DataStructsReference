from src.array_queue import ArrayQueue


# Test initialization
def test_initialization():
    size = 5
    queue = ArrayQueue(size)
    assert queue.arr_limit == size
    assert queue.arr_size == 0
    assert queue.head == 0
    assert queue.backing_array == [None] * size


# Test adding elements
def test_add_elements():
    queue = ArrayQueue(3)
    assert queue.add(1)
    assert queue.add(2)
    assert queue.add(3)
    assert queue.arr_size
    assert queue.backing_array == [1, 2, 3]

    # Test adding beyond initial size to trigger resize
    assert queue.add(4)
    assert queue.arr_size == 4
    assert queue.arr_limit == 6  # Should have doubled the size
    assert queue.backing_array[0:4] == [1, 2, 3, 4]


# Test removing elements
def test_remove_elements():
    queue = ArrayQueue(3)
    queue.add(1)
    queue.add(2)
    queue.add(3)

    assert queue.remove() == 1
    assert queue.arr_size == 2
    assert queue.head == 1

    assert queue.remove() == 2
    assert queue.arr_size == 1
    assert queue.head == 0

    assert queue.remove() == 3
    assert queue.arr_size == 0
    assert queue.head == 0

    # Test removing from an empty queue
    assert queue.remove() is None


# Test resizing
def test_resize():
    queue = ArrayQueue(2)
    queue.add(1)
    queue.add(2)
    assert queue.arr_limit == 2

    # Trigger resize by adding a third element
    queue.add(3)
    assert queue.arr_limit == 4
    assert queue.arr_size == 3
    assert queue.backing_array[0:3] == [1, 2, 3]

    # Trigger resize by removing elements
    queue.remove()
    queue.remove()
    assert queue.arr_limit == 2  # Should have resized down
    assert queue.arr_size == 1
    assert queue.backing_array[0:1] == [3]


# Test edge cases
def test_edge_cases():
    queue = ArrayQueue(0)
    assert queue.arr_limit == 0
    assert queue.add(1)
    assert queue.arr_limit == 1
    assert queue.arr_size == 1
    assert queue.remove() == 1
    assert queue.arr_size == 0

    queue2 = ArrayQueue(1)
    queue2.add(1)
    assert queue2.add(2)
    assert queue2.arr_limit == 2
    assert queue2.arr_size == 2
    assert queue2.remove() == 1
    assert queue2.remove() == 2
    assert queue2.arr_size == 0


# Test wrapping around the array
def test_wrap_around():
    queue = ArrayQueue(3)
    queue.add(1)
    queue.add(2)
    queue.add(3)
    assert queue.remove() == 1
    assert queue.remove() == 2
    queue.add(4)
    queue.add(5)
    assert queue.backing_array == [3, 4, 5, None]
    assert queue.head == 0
    assert queue.arr_size == 3

    assert queue.remove() == 3
    assert queue.remove() == 4
    assert queue.remove() == 5
    assert queue.arr_size == 0


# Test adding and removing alternately
def test_add_remove_alternately():
    queue = ArrayQueue(2)
    queue.add(1)
    assert queue.remove() == 1
    queue.add(2)
    assert queue.remove() == 2
    queue.add(3)
    assert queue.remove() == 3
    assert queue.arr_size == 0


# Test adding None values
def test_add_none_values():
    queue = ArrayQueue(3)
    queue.add(None)
    queue.add(None)
    queue.add(None)
    assert queue.arr_size == 3
    assert queue.backing_array == [None, None, None]

    assert queue.remove() is None
    assert queue.remove() is None
    assert queue.remove() is None
    assert queue.arr_size == 0


# Test adding different types
def test_add_different_types():
    queue = ArrayQueue(3)
    queue.add(1)
    queue.add("hello")
    queue.add(3.14)
    assert queue.arr_size == 3
    assert queue.backing_array == [1, "hello", 3.14]

    assert queue.remove() == 1
    assert queue.remove() == "hello"
    assert queue.remove() == 3.14
    assert queue.arr_size == 0


# Test adding and removing with resizing
def test_add_remove_with_resizing():
    queue = ArrayQueue(2)
    queue.add(1)
    queue.add(2)
    assert queue.arr_limit == 2

    queue.add(3)  # Trigger resize
    assert queue.arr_limit == 4
    assert queue.arr_size == 3

    assert queue.remove() == 1
    assert queue.remove() == 2
    assert queue.remove() == 3
    assert queue.arr_size == 0
    assert queue.arr_limit == 1


# Test removing from an empty queue
def test_remove_from_empty_queue():
    queue = ArrayQueue(3)
    assert queue.remove() is None
    assert queue.arr_size == 0


# Test adding to a queue with size 0
def test_add_to_zero_size_queue():
    queue = ArrayQueue(0)
    assert queue.add(1)
    assert queue.arr_limit == 1
    assert queue.arr_size == 1
    assert queue.remove() == 1
    assert queue.arr_size == 0


# Test adding to a queue with size 1
def test_add_to_one_size_queue():
    queue = ArrayQueue(1)
    assert queue.add(1)
    assert queue.arr_size == 1
    assert queue.add(2)  # Trigger resize
    assert queue.arr_limit == 2
    assert queue.arr_size == 2
    assert queue.remove() == 1
    assert queue.remove() == 2
    assert queue.arr_size == 0


# Test adding and removing with a large queue
def test_large_queue():
    size = 1000
    queue = ArrayQueue(size)
    for i in range(size):
        queue.add(i)
    assert queue.arr_size == size
    assert queue.arr_limit == size

    queue.add(size)  # Trigger resize
    assert queue.arr_limit == 2 * size
    assert queue.arr_size == size + 1

    for i in range(size + 1):
        assert queue.remove() == i
    assert queue.arr_size == 0


# Test adding and removing with a large queue and wrapping around
def test_large_queue_wrap_around():
    size = 1000
    queue = ArrayQueue(size)
    for i in range(size):
        queue.add(i)
    for i in range(size // 2):
        assert queue.remove() == i
    for i in range(size // 2):
        queue.add(size + i)
    assert queue.arr_size == size
    assert queue.arr_limit == size

    for i in range(size // 2, size):
        assert queue.remove() == i
    for i in range(size // 2):
        assert queue.remove() == size + i
    assert queue.arr_size == 0
