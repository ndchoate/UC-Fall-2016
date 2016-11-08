// dijkstra.cpp CS2028 2016 cheng
// Dijkstra's algorithm with heap as priority queue
// To be used with roadGraph.txt or graphs with similar format

#include <iostream>
#include <fstream>
#include "heap2.h"
using namespace std;

int N, L;
Vertex *vertexList;
Edge *edgeList;

void readGraph(){
    ifstream inputfile;
    inputfile.open("roadGraph.txt");
    if (!inputfile) return;
    inputfile >> N >> L;
    vertexList = new Vertex[N];
    edgeList = new Edge[L];
    string x; string y;
    for (int i = 0; i < N; i++){
        inputfile >> vertexList[i].label >> x >> y;
        vertexList[i].heapPosition = i;
        vertexList[i].cost = 1000;
        vertexList[i].path = -1;
    }
    int u1; int u2; int w; string label;
    for (int i = 0; i < L; i++){
        inputfile >> u1 >> u2 >> w >> label;
        edgeList[i].v1 = u1;
        edgeList[i].v2 = u2;
        edgeList[i].weight = w;
    }
    inputfile.close();
}

void addNeighbors(){
    for (int i = 0; i < L; i++){
        vertexList[edgeList[i].v1].adjacentTo.push_back(edgeList + i);
        vertexList[edgeList[i].v2].adjacentTo.push_back(edgeList + i);
    }
}

void printGraph(){  // How to go through a vecter and 2 ways to use pointers to pointers
    for (int i = 0; i < N; i++){
        cout << vertexList[i].label << endl;
        for (vector<Edge*>::iterator iter = vertexList[i].adjacentTo.begin();
            iter < vertexList[i].adjacentTo.end(); iter++)
            cout << "\t" << vertexList[(**iter).v1].label << "\t"
                << vertexList[(*iter)->v2].label << endl;
    }
}

void printPath(int v){
    if (vertexList[v].path >= 0) printPath(vertexList[v].path);
    cout << vertexList[v].label << endl;
}

void dijkstra(int source, int destination){
    vertexList[source].cost = 0;
    Heap heap(vertexList, N);
    heap.siftUpFrom(source);
    while (heap.size > 0){
        int top = heap.removeTop();
        if (top == destination){
            printPath(top);
            return;
        }
        for (vector<Edge*>::iterator iter = vertexList[top].adjacentTo.begin();
            iter < vertexList[top].adjacentTo.end(); iter++){
            int adjacent = (**iter).v1 == top ? (**iter).v2 : (**iter).v1;
            if (vertexList[adjacent].heapPosition >= 0)
                if (vertexList[top].cost + (**iter).weight < vertexList[adjacent].cost){
                    // Your code here to update vertexList[adjacent].cost
                    // and then sift it up from its current heap position
                    vertexList[adjacent].cost = vertexList[top].cost + (**iter).weight;
                    vertexList[adjacent].path = top;
                    heap.siftUpFrom(vertexList[adjacent].heapPosition);
                }
        }
    }
}

int main(){
    readGraph();
    addNeighbors();
    dijkstra(7, 13);
}



