/* sorting.cpp CS2028 2016 Cheng
   implementing sorting.py in C++ with arrays
   Usage: g++ sorting.cpp
   Usage: ./a
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int select(int *seq, int seqLen, int start){
	int minIndex = start;
	for (int i = start + 1; i < seqLen; i++)
		if (seq[minIndex] > seq[i]) minIndex = i;
	return minIndex;
}

void selectionSort(int *seq, int seqLen){
	for (int i = 0; i < seqLen - 1; i++){
		int minIndex = select(seq, seqLen, i);
		int tmp = seq[i];
		seq[i] = seq[minIndex];
		seq[minIndex] = tmp;
	}
}

void randomize(int *seq, int seqLen){
	for (int j = 1; j < seqLen; j++){
		int tmp = seq[j];
		int pos = rand() % j;
		seq[j] = seq[pos];
		seq[pos] = tmp;
	}
}

void checkSorting(int *seq, int seqLen){
	for (int i = 0; i < seqLen; i++) if (seq[i] != i) printf("error\n");
}

int binarysearch(int *seq, int high, int key){
// need work
}

void insert(int *seq, int index){
// need work
}

void insertWithBinarysearch(int *seq, int index){
// need work
}

void insertionSort(int *seq, int seqlen){
	for (int i = 1; i < seqlen; i++) insert(seq, i);
}

void insertionSortWithBinarysearch(int *seq, int seqlen){
	for (int i = 1; i < seqlen; i++) insertWithBinarysearch(seq, i);
}

int sortWithAlgorithm(int *seq, int seqLen, void (*algorithm)(int*, int)){
	clock_t starttime, endtime;
	int lst2[seqLen];
	for (int j = 0; j < seqLen; j++) lst2[j] = seq[j];
	starttime = clock();
	algorithm(lst2, seqLen);
	endtime = clock();
	checkSorting(lst2, seqLen);
	return endtime - starttime;
}

void merge(int *seq, int start, int mid, int stop){
	int lst[stop - start];
	int i = start;
	int j = mid;
        int pos = 0;
	while (i < mid && j < stop)
		if (seq[i] < seq[j]) lst[pos++] = seq[i++];
		else lst[pos++] = seq[j++];
	while (i < mid) lst[pos++] = seq[i++];
	for (i = 0; i < pos; i++) seq[start + i] = lst[i];
}

void mergeSortRecursively(int *seq, int start, int stop){
// need work
}

void mergeSort(int *seq, int seqlen){
	mergeSortRecursively(seq, 0, seqlen);
}

int partition(int *seq, int start, int stop){
// need work
}

void quicksortRecursively(int *seq, int start, int stop){
// need work
}

void quicksort(int *seq, int seqlen){
	randomize(seq, seqlen);
	quicksortRecursively(seq, 0, seqlen);
}

bool bubbleRound(int *seq, int stop){
// need work
}

void bubbleSort(int *seq, int seqlen){
	int stop = seqlen;
	while (bubbleRound(seq, stop--));
}

void compareAlgorithms(){
	for (int N = 0; N < 6; N++){
		int size = 10000 * (N + 1);  // ten times longer than Python
		int lst[size];
		for (int j = 0; j < size; j++) lst[j] = j;
		randomize(lst, size);
		int S = sortWithAlgorithm(lst, size, selectionSort);
		int I = sortWithAlgorithm(lst, size, insertionSort);
		int IB = sortWithAlgorithm(lst, size, insertionSortWithBinarysearch);
		int M = sortWithAlgorithm(lst, size, mergeSort);
		int Q = sortWithAlgorithm(lst, size, quicksort);
		int B = sortWithAlgorithm(lst, size, bubbleSort);
		printf("%d %d %d %d %d %d\n", S, I, IB, M, Q, B);
	}
}

int main(){
	compareAlgorithms();
}