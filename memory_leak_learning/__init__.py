# import pandas as pd

import gc

# Enable GC debugging
gc.set_debug(gc.DEBUG_LEAK)

# Simulate a function that may cause a leak
def create_leak():
    l = []
    l.append(l)  # Creates a self-referential cycle



def run_program():

    create_leak()

    # Force garbage collection
    print("Collecting garbage...")
    gc.collect()

    # Inspect uncollectable objects
    if gc.garbage:
        print("Uncollectable objects found:")
        for obj in gc.garbage:
            print(f"Leaked object: {repr(obj)}")
            print(f"Type: {type(obj)}")
            print(f"Referrers: {gc.get_referrers(obj)}")
    else:
        print("No memory leaks detected.")