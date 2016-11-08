// heap2.h CS2028 2016 cheng
// To be included by dijkstra.cpp

#include <string>
#include <vector>
using namespace std;

struct Edge{
	int v1;
	int v2;
	int weight;
};

struct Vertex{
	string label;
	vector<Edge*> adjacentTo;
	int heapPosition;
	int cost;
	int path;
};

class Heap{
	int* data;
	void __siftDownFrom(int);
public:
	Vertex* values;
	int size;
	Heap(Vertex* v, int s): values(v), size(s){
		data = new int[size];
		for (int i = 0; i < size; i++) data[i] = i;
	}
	void siftUpFrom(int);
	int removeTop(){
		int ret = data[0];
		data[0] = data[size - 1];
		size--;
		__siftDownFrom(0);
		values[ret].heapPosition = -1;
		return ret;
	}
};

void Heap::siftUpFrom(int childIndex){
	int parentIndex = (childIndex - 1)/2;
	if (parentIndex >= 0 && values[data[childIndex]].cost < values[data[parentIndex]].cost){
		int tmp = data[childIndex];
		data[childIndex] = data[parentIndex];
		data[parentIndex] = tmp;
		values[data[childIndex]].heapPosition = childIndex;
		values[data[parentIndex]].heapPosition = parentIndex;
		siftUpFrom(parentIndex);
	}
}

void Heap::__siftDownFrom(int parentIndex){
	int bestChild = -1;
	int leftChildIndex = parentIndex * 2 + 1;
	if (leftChildIndex >= size) return;
	if (leftChildIndex + 1 >= size) bestChild = leftChildIndex;
	else if (values[data[leftChildIndex]].cost > values[data[leftChildIndex + 1]].cost)
		bestChild = leftChildIndex + 1;
	else bestChild = leftChildIndex;
	if (values[data[parentIndex]].cost > values[data[bestChild]].cost){
		int tmp = data[bestChild];
		data[bestChild] = data[parentIndex];
		data[parentIndex] = tmp;
		values[data[bestChild]].heapPosition = bestChild;
		values[data[parentIndex]].heapPosition = parentIndex;
		__siftDownFrom(bestChild);
	}
}

