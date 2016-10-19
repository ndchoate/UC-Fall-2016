#include <iostream>
#include <stdlib.h>
#include "binarysearchtree1.h"
using namespace std;

int main(){
	BinarySearchTree<int> tree;
	char choice[128];
	char value[128];
	cout << "Binary Search Tree Program" << endl;
	cout << "--------------------------" << endl;
	while (1){
		cout << "Make a choice..." << endl;
		cout << "1. Insert into tree." << endl;
		cout << "2. Delete from tree." << endl;
		cout << "3. Lookup value." << endl;
		cout << "Choice? (0 to end) ";
		cin >> choice;
		if (choice[0] == '1'){
			while (1){
				cout << "insert? (0 to end) ";
				cin >> value;
				if (value[0] == '0') break;
				tree.insert(atoi(value));
			}
			tree.showTree();
		}else if (choice[0] == '2'){
			while (1){
				cout << "delete? (0 to end) ";
				cin >> value;
				if (value[0] == '0') break;
				tree.remove(atoi(value));
			}
			tree.showTree();
		}else if (choice[0] == '3'){
			while (1){
				cout << "value? (0 to end) ";
				cin >> value;
				if (value[0] == '0') break;
				if (tree.search(atoi(value)))
					cout << "Yes, " << value << " is in the tree." << endl;
				else cout << "No, " << value << " was not in the tree." << endl;
			}
		}else break;
	}
}