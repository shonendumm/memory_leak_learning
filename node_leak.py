import gc

# Enable detailed debug logs
gc.set_debug(gc.DEBUG_LEAK)

# Example of a circular reference
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a circular reference
a = Node(1)
b = Node(2)
a.next = b
b.next = a

# Break strong references to trigger GC
a = None
b = None

# Force garbage collection
gc.collect()

# Check uncollectable objects
if gc.garbage:
    print("Uncollectable objects:")
    for obj in gc.garbage:
        print(f"Leaked object: {repr(obj)}")
        print(f"Referrers: {gc.get_referrers(obj)}")
else:
    print("No memory leaks detected.")
