# sorting.py CS2028 2016 Cheng
# Usage: python sorting.py
# time spent for each sorting algorithm on identical randomized sequences of 
# increasing sizes

import random
import time, datetime

# used by selectionSort
# returns the index of the smallest element in seq starting at start
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

# instead returns None when key is not in seq, it returns the index it should be at
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

# used by insertionSort
# precondition: seq[0:index] is sorted
# postcondition: seq[0:index + 1] is sorted
def insert(seq, index):
	value = seq[index]
	i = index -1
	while i >= 0 and seq[i] > value:
		seq[i + 1] = seq[i]
		i -= 1
	seq[i + 1] = value

# used by insertionSortWithBinarysearch
# precondition: seq[0:index] is sorted
# postcondition: seq[0:index + 1] is sorted
# binary search used on sorted seq[0:index] 
# faster than insert without binary search
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

# When seq is correctly sorted its ith element shuld be i.
def checkSorting(seq):
	for i in range(len(seq)):
		if seq[i] != i:
			print("error")

# precondition: seq[start:mid] and seq[mid:stop] are sorted
# postconditio: seq[start:stop] is sorted
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

# postcondition: returns j so that all elements in seq[start:j] are smaller than seq[j] and 
#        all elements in seq[j+1:stop] are not smaller than seq[j]
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

# random shuffle to rearrange elements of seq
def randomize(seq):
	for j in range(1, len(seq)):
		tmp = seq[j]
		pos = random.randint(0, j - 1)
		seq[j] = seq[pos]
		seq[pos] = tmp

def quicksortRecursively(seq, start, stop):
	if start >= stop:
		return 
	pivotIndex = partition(seq, start, stop)
	quicksortRecursively(seq, start, pivotIndex)
	quicksortRecursively(seq, pivotIndex+1, stop)

def quicksort(seq):
	randomize(seq)
	quicksortRecursively(seq, 0, len(seq))

# postcondition: the largest element at seq[stop - 1]
# returns True when seq has been mutated and False otherwise
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

# using the built-in sort function of Python list
def builtinSort(seq):
	seq.sort()

# apply six sorting algorithms on the same randomized seq and report times
# repeat this on ever larger seq (1000, 2000, ..., 6000)
def compareAlgorithms():

	# seq will not be mutated
	# lst is a clone of seq and will be sorted using algorithm
	# time in miliseconds will be returned as time spent
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

	for N in range(6):
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
		P = sortWithAlgorithm(lst, builtinSort)
		print(S, I, IB, M, Q, B, P)

def main():
	compareAlgorithms()	

if __name__ == "__main__":
	main()