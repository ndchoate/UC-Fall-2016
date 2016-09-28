#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <time.h>
using namespace std;

int select(vector<int> seq, int start){
	int minIndex = start;
	for (int i = start + 1; i < seq.size(); i++)
		if (seq[minIndex] > seq[i]) minIndex = i;
	return minIndex;
}

void selectionSort(vector<int> seq){
	for (int i = 0; i < seq.size() - 1; i++){
		int minIndex = select(seq, i);
		int tmp = seq[i];
		seq[i] = seq[minIndex];
		seq[minIndex] = tmp;
	}
}

void randomize(vector<int> seq){
	for (int j = 1; j < seq.size(); j++){
		int tmp = seq[j];
		int pos = rand() % j;
		seq[j] = seq[pos];
		seq[pos] = tmp;
	}
}

void checkSorting(vector<int> seq){
	for (int i = 0; i < seq.size(); i++) if (seq[i] != i) printf("error\n");
}

int sortWithAlgorithm(vector<int> seq, void (*algorithm)(vector<int>)){
	clock_t starttime, endtime;
	vector<int> lst2(seq);
	starttime = clock();
	algorithm(lst2);
	endtime = clock();
	checkSorting(lst2);
	return endtime - starttime;
}

void compareAlgorithms(){
	for (int N = 0; N < 6; N++){
		int size = 1000 * (N + 1);
		vector<int> lst(size);
		for (int j = 0; j < size; j++) lst[j] = j;
		randomize(lst);
		int S = sortWithAlgorithm(lst, selectionSort);
		printf("%d\n", S);
	}
}

int main(){
	compareAlgorithms();
}