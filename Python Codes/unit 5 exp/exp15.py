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

def manual_garbage_collection():
    print("Memory usage before garbage collection:", get_memory_usage())
    obj1, obj2, obj3 = create_objects()
    print("Memory usage after creating objects:", get_memory_usage())
    del obj1, obj2, obj3
    print("Collecting garbage manually...")
    gc.collect()
    print("Memory usage after garbage collection:", get_memory_usage())

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    gc.enable()
    manual_garbage_collection()
