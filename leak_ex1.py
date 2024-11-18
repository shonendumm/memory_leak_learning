import gc
import sys
from io import StringIO

# Create a StringIO buffer to capture stderr output
stderr_buffer = StringIO()

# Redirect stderr to capture garbage collection logs
sys.stderr = stderr_buffer

# Enable gc.DEBUG_LEAK to print debug information
gc.set_debug(gc.DEBUG_LEAK)

class LeakyObject:
    def __init__(self):
        self.ref = self  # Create a reference cycle

    def __del__(self):
        pass  # __del__ method makes the object uncollectable in cycles

# Create a list of objects
leaks = [LeakyObject()]

# Delete the list
del leaks

# Force garbage collection
gc.collect()

# Get the captured output from stderr_buffer
debug_output = stderr_buffer.getvalue()

# Filter out the unwanted lines containing "collectable"
filtered_output = '\n'.join(line for line in debug_output.splitlines() if "collectable" not in line)

# Print the filtered output
print(filtered_output)

# Check uncollectable objects in gc.garbage
if gc.garbage:
    print("Uncollectable objects:")
    for obj in gc.garbage:
        print(f"Leaked object: {obj}")
        # Optionally, print referrers of leaked objects:
        # print(f"Referrers: {gc.get_referrers(obj)}")
else:
    print("No memory leaks detected.")

# Restore stderr to its original state
sys.stderr = sys.__stderr__
