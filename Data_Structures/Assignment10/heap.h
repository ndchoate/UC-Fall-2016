class Heap{
    double* values;
    int size;
    int* data;
    void __siftUpFrom(int);
    void __siftDownFrom(int);
public:
    Heap(double* v, int s): values(v), size(s){
        data = new int[size];
        for (int i = 0; i < size; i++) data[i] = i;
    }
    void build(){ for (int i = 1; i < size; i++) __siftUpFrom(i); }
    int removeTop(){
        int ret = data[0];
        data[0] = data[size - 1];
        size--;
        __siftDownFrom(0);
        return ret;
    }
};

void Heap::__siftUpFrom(int childIndex){
    int parentIndex = (childIndex - 1)/2;
    if (parentIndex >= 0 && values[data[childIndex]] > values[data[parentIndex]]){
        int tmp = data[childIndex];
        data[childIndex] = data[parentIndex];
        data[parentIndex] = tmp;
        __siftUpFrom(parentIndex);
    }
}

void Heap::__siftDownFrom(int parentIndex){
    int bestChild = -1;
    int leftChildIndex = 2 * parentIndex + 1;

    if (leftChildIndex >= size) {
        return;
    }

    if (leftChildIndex + 1 >= size) {
        bestChild = leftChildIndex;
    } else if (values[data[leftChildIndex]] < values[data[leftChildIndex + 1]]) {
        bestChild = leftChildIndex + 1;
    } else {
        bestChild = leftChildIndex;
    }

    if (values[data[parentIndex]] < values[data[bestChild]]) {
        int temp = data[bestChild];
        data[bestChild] = data[parentIndex];
        data[parentIndex] = temp;
        __siftDownFrom(bestChild);
    }
}

