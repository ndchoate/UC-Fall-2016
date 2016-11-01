class Heap:
	def __init__(self,values):
		self.values = values
		self.size = len(values)
		self.data = []
		for i in range(self.size):
			self.data.append(i)

	def getVal(self,index):	
		return self.values[index]

	def __siftUpFrom(self, childIndex):
		parentIndex = (childIndex - 1)//2
		if parentIndex >= 0 and self.getVal(self.data[childIndex]) > self.getVal(self.data[parentIndex]):
			tmp = self.data[childIndex]
			self.data[childIndex] = self.data[parentIndex]
			self.data[parentIndex] = tmp
			Heap.__siftUpFrom(self, parentIndex)

	def build(self):
		for i in range(self.size):
			Heap.__siftUpFrom(self,i)

	def removeTop(self):
		ret = self.data[0]
		self.data[0] = self.data[self.size - 1]
		self.size -= 1
		Heap.__siftDownFrom(self, 0)
		return ret

	def __siftDownFrom(self, parentIndex):
		leftChildIndex = parentIndex * 2 + 1
		if leftChildIndex >= self.size:
			return
		if leftChildIndex + 1 >= self.size:
			bestChild = leftChildIndex
		elif self.getVal(self.data[leftChildIndex]) < self.getVal(self.data[leftChildIndex + 1]):
			bestChild = leftChildIndex + 1
		else:
			bestChild = leftChildIndex
		if self.getVal(self.data[parentIndex]) < self.getVal(self.data[bestChild]):
			tmp = self.data[bestChild]
			self.data[bestChild] = self.data[parentIndex]
			self.data[parentIndex] = tmp
			Heap.__siftDownFrom(self, bestChild)
