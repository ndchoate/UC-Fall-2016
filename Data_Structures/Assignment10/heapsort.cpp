#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include "heap.h"
using namespace std;

const int MAXLINE = 120;
const int capacity = 152000;
char *names[capacity];
int counts[capacity];
float pctwhite[capacity];
float pctblack[capacity];
float pctapi[capacity];
int numberOfNames = 0;

void processLine(char *line, int n)
{
        char * pch = strtok(line, ",");
        int len = strlen(pch);
        names[n] = new char[len + 1];
        strcpy(names[n], pch);
        counts[n] = atoi(strtok(NULL, ","));
        float pcts[6];
        for (int i = 0; i < 6; i++)
        {
            pch = strtok(NULL, ",");
            pcts[i] = pch[0] == '(' ? 0 : atof(pch);
        }
        pctwhite[n] = pcts[0];
	pctblack[n] = pcts[1];
	pctapi[n] = pcts[2];
}

void readlines()
{
    char line[MAXLINE];
    ifstream inputfile;
    inputfile.open("../programs/names.csv");
    if (!inputfile) return;
    inputfile.getline(line, MAXLINE);
    inputfile.getline(line, MAXLINE);
    while (!inputfile.eof())
    {
        processLine(line, numberOfNames++);
        inputfile.getline(line, MAXLINE);
    }
    inputfile.close();
}

void findMostPopular(){
	double values[numberOfNames];
	int selected[numberOfNames];
	int size = 0;
	for (int i = 0; i < numberOfNames; i++) if (pctblack[i] > 0){ 
	    selected[size] = i; 
            values[size++] = counts[i] * pctblack[i] / 100;
	}
	Heap heap(values, size);
	heap.build();
	for (int i = 0; i < 20; i++){
		int top = heap.removeTop();
		cout << names[selected[top]] << " " << values[top] << endl;
	}

}

int main(){
	readlines();
	findMostPopular();
}

