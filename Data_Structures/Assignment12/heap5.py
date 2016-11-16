# heap5.py CS2028 2016 Cheng
# smallest-on-top heap, to be used with dijkstra2.py

class Heap:
	def __init__(self,values):
		self.values = values
		self.size = len(values)
		self.data = []
		for i in range(self.size):
			self.data.append(i)

	def getVal(self,index):	
		return self.values[index].cost + self.values[index].distanceToGoal

	def siftUpFrom(self, childIndex):
		parentIndex = (childIndex - 1)//2
		if parentIndex >= 0 and self.getVal(self.data[childIndex]) < self.getVal(self.data[parentIndex]):
			tmp = self.data[childIndex]
			self.data[childIndex] = self.data[parentIndex]
			self.data[parentIndex] = tmp
			self.values[self.data[childIndex]].heapPosition = childIndex
			self.values[self.data[parentIndex]].heapPosition = parentIndex
			Heap.siftUpFrom(self, parentIndex)

	def removeTop(self):
		ret = self.data[0]
		self.data[0] = self.data[self.size - 1]
		self.size -= 1
		Heap.__siftDownFrom(self, 0)
		self.values[ret].heapPosition = -1
		return ret

	def __siftDownFrom(self, parentIndex):
		leftChildIndex = parentIndex * 2 + 1
		if leftChildIndex >= self.size:
			return
		if leftChildIndex + 1 >= self.size:
			bestChild = leftChildIndex
		elif self.getVal(self.data[leftChildIndex]) > self.getVal(self.data[leftChildIndex + 1]):
			bestChild = leftChildIndex + 1
		else:
			bestChild = leftChildIndex
		if self.getVal(self.data[parentIndex]) > self.getVal(self.data[bestChild]):
			tmp = self.data[bestChild]
			self.data[bestChild] = self.data[parentIndex]
			self.data[parentIndex] = tmp
			self.values[self.data[bestChild]].heapPosition = bestChild
			self.values[self.data[parentIndex]].heapPosition = parentIndex
			Heap.__siftDownFrom(self, bestChild)
