/* sudokuR.cpp CS2028 2016 cheng
   C++ version of sudoku5.py
   set is bool[9]
   groups is bool *[27][9]
*/
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
using namespace std;

bool (* readPuzzle())[9][9]{
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
    bool (*matrix)[9][9] = new bool[9][9][9];
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
    return matrix;
}

void showMatrix(bool (*matrix)[9][9], int depth){
    for (int i = 0; i < 9; i++){
        for (int d = 0; d < depth; d++) cout << "  ";
        for (int j = 0; j < 9; j++){
            int size = 0;
            for (int k = 0; k < 9; k++) if (matrix[i][j][k]) size++;
            if (size == 1){
                int k = 0; for (; k < 9; k++) if (matrix[i][j][k]) break;
                cout << k + 1 << " ";
            }else if (size == 0) cout << "  ";
            else cout << "x ";
        }
        cout << endl;
    }
    cout << endl;
}


bool * (* getGroups(bool (*matrix)[9][9]))[9]{
    bool * (* groups)[9] = new bool*[27][9];
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++){
            groups[i][j] = matrix[i][j]; // row i
            groups[9 + i][j] = matrix[j][i];  // column j
        }
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++){
            int gid = 18 + i * 3 + j;
            for (int k = 0; k < 3; k++)
                for (int l = 0; l < 3; l++)
                    groups[gid][k * 3 + l] = matrix[i * 3 + k][j * 3 + l];
        }
    return groups;
}

int size(bool *set){
    int size = 0;
    for (int i = 0; i < 9; i++) if (set[i]) size++;
    return size;
}

bool isSubset(bool *set1, bool *set2){
    for (int i = 0; i < 9; i++) if (set1[i] && !set2[i]) return 0;
    return 1;
}

bool isDisjoint(bool *set1, bool *set2){
    for (int i = 0; i < 9; i++) if (set1[i] && set2[i]) return 0;
    return 1;
}

void difference_update(bool *set1, bool *set2){
    for (int i = 0; i < 9; i++) if (set1[i] && set2[i]) set1[i] = 0;
}

int rule1(bool **g){
    int changed = 0;
    for (int i = 0; i < 9; i++){
        int count = 1;
        for (int j = 0; j < 9; j++)
            if (j != i && isSubset(g[j], g[i]))
                count++;
        if (count == size(g[i])){
            for (int j = 0; j < 9; j++){
                if (!isSubset(g[j], g[i]) &&
                    !isDisjoint(g[j], g[i])){
                        difference_update(g[j], g[i]);
                        changed = 1;
                }
            }
        }else if (count > size(g[i])) return -1;
    }
    return changed;
}

int rule2(bool **g){
    int changed = 0;
    int counts[9];
    for (int j = 0; j < 9; j++) counts[j] = 0;
    for (int i = 0; i < 9; i++){
        for (int j = 0; j < 9; j++)
            if (g[i][j]) counts[j]++;
    }
    for (int j = 0; j < 9; j++)
        if (counts[j] == 1){
            for (int i = 0; i < 9; i++)
                if (g[i][j] && size(g[i]) > 1){
                    for (int k = 0; k < 9; k++)
                        if (g[i][k] && k != j) g[i][k] = 0;
                    changed = 1;
                }
        }
    return changed;
}

int reduceGroup(bool **g){
    int changed = 0;
    int ret = rule1(g);
    if (ret == 1) changed = 1;
    else if (ret == -1) return -1;
    if (rule2(g) == 1 && changed == 0) changed = 1;
    return changed;
}


int reduceGroups(bool *(* groups)[9]){
    int changed = 0;
    for (int i = 0; i < 27; i++){
        int ret = reduceGroup(groups[i]);
        if (ret == 1) changed = 1;
        else if (ret == -1) return -1;
    }
    return changed;
}

int reduce(bool (*matrix)[9][9]){
    int changed = 1;
    bool * (*groups)[9] = getGroups(matrix);
    while (changed == 1){
        changed = reduceGroups(groups);
    }
    if (changed == -1) return -1;
    else return 0;
}

bool solutionViable(bool (* matrix)[9][9]){
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++)
            if (size(matrix[i][j]) == 0)
                return 0;
    return 1;
}

bool solutionOK(bool (* matrix)[9][9]){
// You need to translate the similar function in sudoku5.py into C++ here.
// This function should look very similar to solutionViable above.
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (size(matrix[i][j]) > 1) {
                return 0;
            }
        }
    }
    return 1;
}


bool (* solve(bool (*matrix)[9][9], int depth))[9][9]{
    showMatrix(matrix, depth);
    int ret = reduce(matrix);
    if (ret == -1){ cout << "dead end" << endl; return 0; }
    if (!solutionViable(matrix)) return 0;
    if (solutionOK(matrix)) return matrix;
    cout << "Searching..." << endl;
    int i, j;
    for (i = 0; i < 9; i++){
        for (j = 0; j < 9; j++)
            if (size(matrix[i][j]) > 1) break;
        if (j < 9) break;
    }
    if (i == 9) return 0;
    for (int k = 0; k < 9; k++) if (matrix[i][j][k]){
        cout << i << "," << j << "," << k + 1 << endl;
        bool (*mcopy)[9][9] = new bool[9][9][9];
        for (int p = 0; p < 9; p++)
            for (int q = 0; q < 9; q++)
                for (int r = 0; r < 9; r++)
                    mcopy[p][q][r] = matrix[p][q][r];
        for (int r = 0; r < 9; r++) mcopy[i][j][r] = 0;
        mcopy[i][j][k] = 1;
        bool (*result)[9][9] = solve(mcopy, depth + 1);
            if (result != 0){
                if (result!=mcopy) delete[] mcopy;
                return result;
            }
    }
    return 0;
}


int main()
{
    bool (*matrix)[9][9] = readPuzzle();
    showMatrix(matrix, 0);
    cout << "Begin Solving" << endl;
    matrix = solve(matrix, 0);
    if (!matrix){
        cout << "No solution found!" << endl;
        return 1;
    }
    showMatrix(matrix, 0);
}
