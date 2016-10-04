/* sudoku.cpp CS2028 2016 cheng
   C++ version of sudoku4.py (or sudoku.py)
   set is implemented as bool[]
   no map is used but an int[] is used as counters
*/

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
using namespace std;

bool matrix[9][9][9];  // The third dimension is the set dimension
int groups[27][9][2];  // 27 groups of 9 cell each, identified with row/col in matrix in the third dim

void readPuzzle(){
	char filename[100];
	ifstream infile;
	string line;

	cout << "Please enter a Sudoku puzzle file name: ";
	cin >> filename;
	infile.open( filename );
	if (!infile){
		cerr << filename << " could not be opened " << endl;
		exit(1);
	}
	for (int i = 0; i < 9; i++){
		getline(infile, line);
		for (int j = 0; j < 9; j++){
			char c = line[j * 2];
			if (c == 'x')
				for (int k = 0; k < 9; k++) matrix[i][j][k] = 1;
			else{
				int l = c - '1';
				for (int k = 0; k < 9; k++) matrix[i][j][k] = 0;
				matrix[i][j][l] = 1;
			}
		}
	}
	infile.close();
}

void showMatrix(){
	for (int i = 0; i < 9; i++){
		for (int j = 0; j < 9; j++){
			int size = 0;
			for (int k = 0; k < 9; k++) if (matrix[i][j][k]) size++;
			if (size == 1){
				int k = 0; for (; k < 9; k++) if (matrix[i][j][k]) break;
				cout << k + 1 << " ";
			}else cout << "x ";
		}
		cout << endl;
	}
	cout << endl;
}

void showMatrix2(){  // never used but can show all cells as sets
	for (int i = 0; i < 9; i++){
		for (int j = 0; j < 9; j++){
			for (int k = 0; k < 9; k++) if (matrix[i][j][k]) cout << k+1;
				else cout << " ";
			cout << "|";
		}
		cout << endl;
	}
	cout << endl;
}


void getGroups(){
	for (int i = 0; i < 9; i++)
		for (int j = 0; j < 9; j++){
			groups[i][j][0] = i; // row i
			groups[i][j][1] = j;
			groups[9 + i][j][0] = j;
			groups[9 + i][j][1] = i; // column i
		}
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++){
			int gid = 18 + i * 3 + j;
			for (int k = 0; k < 3; k++)
				for (int l = 0; l < 3; l++){
					groups[gid][k * 3 + l][0] = i * 3 + k;
					groups[gid][k * 3 + l][1] = j * 3 + l;
				}
		}
}

int size(bool *set){  // equivalent to len(set) in Python
	int size = 0;
	for (int i = 0; i < 9; i++) if (set[i]) size++;
	return size;
}

bool isSubset(bool *set1, bool *set2){  // equivalent to set1 <= set2 in Python
	for (int i = 0; i < 9; i++) if (set1[i] && !set2[i]) return 0;
	return 1;
}

bool isDisjoint(bool *set1, bool *set2){  // equivalent to set1.isdisjoint(set2) in Python
	for (int i = 0; i < 9; i++) if (set1[i] && set2[i]) return 0;
	return 1;
}

void difference_update(bool *set1, bool *set2){  // equivalent to set1 -= set2 in Python
	for (int i = 0; i < 9; i++) if (set1[i] && set2[i]) set1[i] = 0;
}	

bool rule1(int (*g)[2]){  // g is a group
	bool changed = 0;
	for (int i = 0; i < 9; i++){  // with 9 cells
		int count = 1;
		bool *cell = matrix[g[i][0]][g[i][1]];  // each cell
		for (int j = 0; j < 9; j++)   // if another cell is a subset
			if (j != i && isSubset(matrix[g[j][0]][g[j][1]], cell))
				count++;
		if (count == size(cell)){  // count < 9 may be added
			for (int j = 0; j < 9; j++){
				bool *cell2 = matrix[g[j][0]][g[j][1]];  // all other cells
				if (!isSubset(cell2, cell) &&  
					!isDisjoint(cell2, cell)){
						difference_update(cell2, cell);
						changed = 1;
				}
			}
		}
	}
	return changed;
}

bool rule2(int (*g)[2]){
	bool changed = 0;
	int counts[9];  // number of cells containing each item
	for (int j = 0; j < 9; j++) counts[j] = 0;
	for (int i = 0; i < 9; i++){
		bool *cell = matrix[g[i][0]][g[i][1]];
		for (int j = 0; j < 9; j++)
			if (cell[j]) counts[j]++;
	}
	for (int j = 0; j < 9; j++)
		if (counts[j] == 1)  // only one cell containing j
			for (int i = 0; i < 9; i++){
				bool *cell = matrix[g[i][0]][g[i][1]];
				if (cell[j] && size(cell) > 1){  // this is the cell containing j
					// Your code to make cell the set of j alone
					changed = 1;
				}
			}
	return changed;
}

bool reduceGroup(int (*g)[2]){
	bool changed = 0;
	if (rule1(g)) changed = 1;
	if (rule2(g) && !changed) changed = 1;
	return changed;
}


bool reduceGroups(){
	bool changed = 0;
	for (int i = 0; i < 27; i++)
		if (reduceGroup(groups[i])) changed = 1;
	return changed;
}

void reduce(){
	while (reduceGroups()) showMatrix();
}


int main()
{
	readPuzzle();
	showMatrix();
	getGroups();
	reduce();
}