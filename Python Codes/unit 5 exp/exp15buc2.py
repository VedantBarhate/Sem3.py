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

def track_gc_generations():
    print("Initial garbage collection counts:", gc.get_count())
    gc.enable()
    obj1, obj2, obj3 = create_objects()
    print("GC counts after creating objects:", gc.get_count())
    del obj1, obj2, obj3
    print("GC counts after deleting objects (before GC):", gc.get_count())
    gc.collect()
    print("GC counts after manual garbage collection:", gc.get_count())
    print("Enabling garbage collection and creating new objects...")
    obj1, obj2, obj3 = create_objects()
    print("GC counts after creating new objects with GC enabled:", gc.get_count())

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    track_gc_generations()
