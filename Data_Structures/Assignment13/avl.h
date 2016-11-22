// avl.h CS2028 2016 cheng
// uses linkedliststackqueue0.h and is used by avl.cpp

#include <iostream>
#include "linkedliststackqueue0.h"
using namespace std;

template< typename T >
class Node{
public: 
      Node(T v, Node* l = 0, Node* r = 0, int b = 0): val(v), left(l), right(r), balance(b){ }
      T getVal(){  return val; }
      Node* getLeft(){ return left; }
      Node* getRight(){ return right; }
      int getBalance(){ return balance; }
      void setVal(T val){ this->val = val; }
      void setLeft(Node* left){ this->left = left; }
      void setRight(Node* right){ this->right = right; }
      void setBalance(int b){ this->balance = b; }
      void dfs(int depth){
	if (right) right->dfs(depth + 1);
	for (int i = 0; i < depth; i++) cout << "  ";
	cout << val << " " << balance << endl;
	if (left) left->dfs(depth + 1);
      }
      Node* rotateLeft();
      Node* rotateRight();
      Node* rotateLeftThenRight();
      Node* rotateRightThenLeft();
private:
      T val;
      Node* left;
      Node* right;
      int balance;
};

template< typename T >
class AVLTree{
public:
   AVLTree(){ root = 0; }
   bool isEmpty(){ return root == 0; }
   void insert(T);
   bool search(T val);
   void showTree(){ if (isEmpty()) cout << "The tree is empty." << endl;
		else root->dfs(0); cout << endl; }
private:
   Node<T>* root;
   Stack< Node<T> > theStack;
};

   template< typename T >
   void AVLTree<T>::insert(T val){
	cout << "inserting " << val << endl;
	if (AVLTree<T>::search(val)) return;  // Steps 1 and 2, stack is global, pivot is not needed
	Node<T>* child = new Node<T>(val);  // Step 3
	Node<T>* grandchild = 0;
	if (theStack.isEmpty()){ root = child; return; }  // Step 4
	Node<T>* parent = theStack.pop();  // Step 5
	if (val < parent->getVal()) parent->setLeft(child); else parent->setRight(child);
	while (parent->getBalance() == 0){  // Step 6
		// Your code for Step 6.1: parent’s balance is assigned -1 or 1, 
		// depending on whether the child is its left or right child

		if (theStack.isEmpty()){ cout << "case 1" << endl;  return; } // Step 6.2
		grandchild = child; child = parent; parent = theStack.pop(); // Step 6.3
	}
	Node<T>* newTree = 0;
	if (parent->getLeft() == child)
		if (parent->getBalance() == 1){   // Step 7
			cout << "case 2" << endl;
			parent->setBalance(0);
			return;
		}else if (child->getLeft() == grandchild){ // Step 8
			cout << "case 3A" << endl;
			 newTree = parent->rotateRight();  
			}else{  			// Step 9
			cout << "case 3B" << endl;  
			 newTree = parent->rotateLeftThenRight();  
			}
	else 	if (parent->getBalance() == -1){   // The mirror image
			cout << "case 2" << endl;
			// Your code for Step 7
			return;
		}else if (child->getRight() == grandchild){
			cout << "case 3A" << endl;
			 newTree = // Your code for Step 8
			}else{
			cout << "case 3B" << endl;  
			 newTree = // Your code for Step 9
			}
	if (theStack.isEmpty()) root = newTree;  // Step 10
	else{				// Step 11
		Node<T>* grandparent = theStack.pop();
		if (grandparent->getLeft() == parent) grandparent->setLeft(newTree);
		else grandparent->setRight(newTree);
	}
   }

   template< typename T >
   bool AVLTree<T>::search(T val){
	while (!theStack.isEmpty()) theStack.pop();  // clear the stack
	Node<T>* current = root;
	while (current){
		theStack.push(current);
		if (val == current->getVal()) return 1;
		if (val < current->getVal()) current = current->getLeft();
		else current = current->getRight();
	}
	return 0;
   }

   template< typename T >
   Node<T>* Node<T>::rotateLeft(){
	cout << "rotateLeft " << this->getVal() << endl;
	// Your code, mirror image of rotateRight
   }

   template< typename T >
   Node<T>* Node<T>::rotateRight(){
	cout << "rotateRight " << this->getVal() << endl;
	Node<T>* child = this->getLeft();
	this->setLeft(child->getRight());
	this->setBalance(0);
	child->setRight(this);
	child->setBalance(0);
	return child;
   }

   template< typename T >
   Node<T>* Node<T>::rotateLeftThenRight(){
	cout << "rotateLeftThenRight " << this->getVal() << endl;
	// Your code, mirror image of rotateRightThenLeft
	// The setBalance lines could be the same
   }

   template< typename T >
   Node<T>* Node<T>::rotateRightThenLeft(){
	cout << "rotateRightThenLeft " << this->getVal() << endl;
	int CBalance = this->getRight()->getLeft()->getBalance();
	this->setRight(this->getRight()->rotateRight());
	Node<T>* newTree = this->rotateLeft();
	if (CBalance == -1) newTree->getRight()->setBalance(1);
	else if (CBalance == 1) newTree->getLeft()->setBalance(-1);
	return newTree;
   }



