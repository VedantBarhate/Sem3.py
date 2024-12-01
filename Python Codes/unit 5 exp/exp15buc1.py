import gc
import sys

def create_objects():
    print("Creating objects...")
    obj1 = [1, 2, 3, 4]
    obj2 = {'a': 1, 'b': 2}
    obj3 = "Some string data"
    return obj1, obj2, obj3

def get_memory_usage():
    return sys.getsizeof(gc.get_objects())

def garbage_collection_experiment():
    print("Memory usage with GC enabled:", get_memory_usage())
    gc.enable()
    obj1, obj2, obj3 = create_objects()
    print("Memory usage after creating objects (GC enabled):", get_memory_usage())
    print("Disabling garbage collection...")
    gc.disable()
    del obj1, obj2, obj3
    print("Memory usage after deleting objects (GC disabled):", get_memory_usage())
    print("Manually collecting garbage...")
    gc.collect()
    print("Memory usage after manual GC (GC disabled):", get_memory_usage())
    print("Enabling garbage collection again...")
    gc.enable()
    obj1, obj2, obj3 = create_objects()
    print("Memory usage after creating new objects (GC enabled again):", get_memory_usage())

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    garbage_collection_experiment()
