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
    int lo = 0;
    int hi = high;

    // Check if key is equal to, less than, or greater than mid.
    // If it is equal, return mid index. If it is less than,
    // resume search in lower half of sequence. If it is greater
    // than, resume search in upper half of sequence.
    while (lo <= hi) {
        int mid = (lo + hi) / 2;

        if (seq[mid] == key) {
            return mid;
        } else if (key < seq[mid]) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }

    return lo;
}

void insert(int *seq, int index){
    int value = seq[index];
    int i = index - 1;

    // Start iteration through sequence backwards
    // and keep iterating until a value greater than
    // value at index is found.

    while (i >= 0 && seq[i] > value) {
        seq[i + 1] = seq[i];
        i--;
    }

    seq[i + 1] = value;
}

void insertWithBinarysearch(int *seq, int index){
    int value = seq[index];
    int lo = binarysearch(seq, index, value);
    for (int i = index - 1; i > lo - 1; i--) {
        seq[i + 1] = seq[i];
    }

    seq[lo] = value;
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
    if (start >= stop - 1) {
        return;
    }

    // Make recursive calls until seq becomes only one item.
    int mid = (start + stop) / 2;
    mergeSortRecursively(seq, start, mid);
    mergeSortRecursively(seq, mid, stop);
    merge(seq, start, mid, stop);
}

void mergeSort(int *seq, int seqlen){
    mergeSortRecursively(seq, 0, seqlen);
}

int partition(int *seq, int start, int stop){
    int pivotIndex = start;
    int pivot = seq[pivotIndex];
    int i = start + 1;
    int j = stop - 1;

    // Loop through list, put all values less than pivot value
    // on left side of pivot, put all values greater than pivot
    // on right side of pivot.
    while (i <= j) {
        while (i <= j && pivot >= seq[i]) {
            i++;
        }

        while (i <= j && pivot < seq[j]) {
            j--;
        }

        if (i < j) {
            int temp = seq[i];
            seq[i] = seq[j];
            seq[j] = temp;
            i++;
            j--;
        }
    }

    seq[pivotIndex] = seq[j];
    seq[j] = pivot;
    return j;
}

void quicksortRecursively(int *seq, int start, int stop){
    if (start >= stop) {
        return;
    }

    // Keep making quicksort recursive call until there is only
    // one item in sequence.
    int pivotIndex = partition(seq, start, stop);
    quicksortRecursively(seq, start, pivotIndex);
    quicksortRecursively(seq, pivotIndex + 1, stop);
}

void quicksort(int *seq, int seqlen){
    randomize(seq, seqlen);
    quicksortRecursively(seq, 0, seqlen);
}

bool bubbleRound(int *seq, int stop){
    bool bubbled = false;

    for (int i = 1; i < stop; i++) {
        if (seq[i] < seq[i - 1]) {
            int tmp = seq[i];
            seq[i] = seq[i - 1];
            seq[i - 1] = tmp;
            bubbled = true;
        }
    }

    return bubbled;
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
