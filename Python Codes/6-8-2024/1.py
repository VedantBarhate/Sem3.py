from abc import ABC, abstractmethod


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, lst):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, lst):
        # bubble algo
        return "Sorted using bubblesort"

class SelectionSort(SortingStrategy):
    def sort(self, lst):
        # selection algo
        return "sorted using selection sort"
    
class MergeSort(SortingStrategy):
    def sort(self, lst):
        # merge algo
        return "sorted using merge sort"
    
class SortingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, lst):
        return self.strategy.sort(lst)
    
if __name__ == "__main__":
    bub = BubbleSort()
    sel = SelectionSort()
    mer = MergeSort()

    lst = [5,2,9,6,3,4,7,9]

    sortingcontext = SortingContext(bub)
    print(sortingcontext.sort(lst))

    sortingcontext.set_strategy(sel)
    print(sortingcontext.sort(lst))

    sortingcontext.set_strategy(mer)
    print(sortingcontext.sort(lst))