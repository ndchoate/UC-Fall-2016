# almostSorted.py CS2028 2016 Cheng
# Usage: python almostSorted.py
# time spent for each sorting algorithm on identical almost sorted sequences of 
# increasing sizes

import random
import time, datetime

def select(seq, start):
	minIndex = start
	for i in range(start+1, len(seq)):
		if seq[minIndex] > seq[i]:
			minIndex = i
	return minIndex

def selectionSort(seq):
	for i in range(len(seq)-1):
		minIndex = select(seq, i)
		tmp = seq[i]
		seq[i] = seq[minIndex]
		seq[minIndex] = tmp

def binarysearch(seq, high, key):
	lo = 0
	hi = high
	while lo <= hi:
		mid = (lo + hi) // 2
		if seq[mid] == key:
			return mid
		elif key < seq[mid]:
			hi = mid - 1
		else:
			lo = mid + 1
	return lo

def insert(seq, index):
	value = seq[index]
	i = index -1
	while i >= 0 and seq[i] > value:
		seq[i + 1] = seq[i]
		i -= 1
	seq[i + 1] = value

def insertWithBinarysearch(seq, index):
	value = seq[index]
	lo = binarysearch(seq, index, value)
	for i in range(index - 1, lo - 1, -1):
		seq[i + 1] = seq[i]
	seq[lo] = value

def insertionSort(seq):
	for i in range(1, len(seq)):
		insert(seq, i)

def insertionSortWithBinarysearch(seq):
	for i in range(1, len(seq)):
		insertWithBinarysearch(seq, i)

def checkSorting(seq):
	for i in range(len(seq)):
		if seq[i] != i:
			print("error")

def merge(seq, start, mid, stop):
	lst = []
	i = start
	j = mid
	while i < mid and j < stop:
		if seq[i] < seq[j]:
			lst.append(seq[i])
			i+=1
		else:
			lst.append(seq[j])
			j+=1
	while i < mid:
		lst.append(seq[i])
		i+=1
	for i in range(len(lst)):
		seq[start + i] = lst[i]

def mergeSortRecursively(seq, start, stop):
	if start >= stop - 1:
		return
	mid = (start + stop) // 2
	mergeSortRecursively(seq, start, mid)
	mergeSortRecursively(seq, mid, stop)
	merge(seq, start, mid, stop)

def mergeSort(seq):
	mergeSortRecursively(seq, 0, len(seq))

def partition(seq, start, stop):
	pivotIndex = start
	pivot = seq[pivotIndex]
	i = start+1
	j = stop-1
	while i <= j:
		while i <= j and not pivot < seq[i]:
			i+=1
		while i <= j and pivot < seq[j]:
			j-=1
		if i < j:
			tmp = seq[i]
			seq[i] = seq[j]
			seq[j] = tmp
			i+=1
			j-=1
	seq[pivotIndex] = seq[j]
	seq[j] = pivot
	return j

# only two randomly selected elements are exchanged
def randomize(seq):
		a = random.randint(0, len(seq) - 1)
		b = random.randint(0, len(seq) - 1)
		tmp = seq[a]
		seq[a] = seq[b]
		seq[b] = tmp

def quicksortRecursively(seq, start, stop):
	if start >= stop:
		return 
	pivotIndex = partition(seq, start, stop)
	quicksortRecursively(seq, start, pivotIndex)
	quicksortRecursively(seq, pivotIndex+1, stop)

# no randomize(seq) in this quicksort
# since seq is almost sorted, this quicksort will be worst
# there may be as many recursive calls as size of seq
# program may crash because the run-time stack is used up
def quicksort(seq):
	quicksortRecursively(seq, 0, len(seq))

def bubbleRound(seq, stop):
	bubbled = False
	for i in range(1, stop):
		if seq[i] < seq[i - 1]:
			tmp = seq[i]
			seq[i] = seq[i - 1]
			seq[i - 1] = tmp
			bubbled = True
	return bubbled

def bubbleSort(seq):
	stop = len(seq)
	while bubbleRound(seq, stop):
		stop-=1

def compareAlgorithms():
	def sortWithAlgorithm(seq, algorithm):
		size = len(seq)
		lst2 = [None] * size
		for j in range(size):
			lst2[j] = seq[j]
		starttime = datetime.datetime.now()
		algorithm(lst2)
		endtime = datetime.datetime.now()
		checkSorting(lst2)
		return (endtime - starttime).total_seconds() * 1000

	for N in range(2):
		size = 1000 * (N + 1)
		lst = [None] * size
		for j in range(size):
			lst[j] = j
		randomize(lst)
		S = sortWithAlgorithm(lst, selectionSort)
		I = sortWithAlgorithm(lst, insertionSort)
		IB = sortWithAlgorithm(lst, insertionSortWithBinarysearch)
		M = sortWithAlgorithm(lst, mergeSort)
		Q = sortWithAlgorithm(lst, quicksort)
		B = sortWithAlgorithm(lst, bubbleSort)
		print(S, I, IB, M, Q, B)

def main():
	compareAlgorithms()	

if __name__ == "__main__":
	main()