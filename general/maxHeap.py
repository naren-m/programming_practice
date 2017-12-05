# Max heap

#                   25(1)
#          15(2)                  20(3)
#    5(4)        10(5)      20(6)      1(7)
# 2(8) 3(9)  5(10)

# [0, 25, 15, 20, 5, 10, 20, 1, 2, 3, 5] - heap
#  0,  1,  2,  3, 4,  5,  6, 7, 8, 9, 10 - indices for above array

# Given an index
#  parent - index//2
#  left child - index *2
#  right child - index *2 +1

# function in heap peek, pop, push
# internal functions __swap, __floatUp, __bubbleDown or __maxifyHeap
class Heap:
    def __init__(self, items=[]):
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, i):
        self.heap.append(i)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        # Scenario #3 - Heap has more than one element
        #               1. Swap the max element with end elemnt of the list
        #               2. pop the end element(which is now the max element)
        #               3. Bubble down or max heapity the array.
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        # Scenario #2 - Heap has only one element
        elif len(self.heap) == 2:
            max = self.heap.pop()
        # Scenario #1 - Heap is empty
        else:
            max = False

        return max
    
    def __swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1] 

    def __floatUp(self, index):
        if index <= 1:
            return

        parent = index // 2

        if self.heap[parent] < self.heap[index]:
            self.__swap(parent, index)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if left < len(self.heap) and self.heap[largest] < self.heap[left]:
            largest = left
        if right < len(self.heap) and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

l = [25, 15, 20, 5, 10, 21, 1, 2, 3, 5]
h = Heap(l)

print h.heap
print l

print h.pop()
print h.heap

h.push(24)
print h.heap

print h.peek()


            
