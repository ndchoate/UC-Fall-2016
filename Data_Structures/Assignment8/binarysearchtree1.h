#include <iostream>
using namespace std;

template< typename T >
class Node{
public:
      Node(T v, Node* l = 0, Node* r = 0): val(v), left(l), right(r){ }
      T getVal(){  return val; }
      Node* getLeft(){ return left; }
      Node* getRight(){ return right; }
      void setVal(T val){ this->val = val; }
      void setLeft(Node* left){ this->left = left; }
      void setRight(Node* right){ this->right = right; }
      void dfs(int depth){
    if (right) right->dfs(depth + 1);
    for (int i = 0; i < depth; i++) cout << "  ";
    cout << val << endl;
    if (left) left->dfs(depth + 1);
      }
      T rightmost(){ Node* c = this; while (c->getRight()) c = c->getRight(); return c->getVal(); }
private:
      T val;
      Node* left;
      Node* right;
};

template< typename T >
class BinarySearchTree{
public:
   BinarySearchTree(){ root = 0; }
   bool isEmpty(){ return root == 0; }
   Node<T>* insertR(Node<T>*, T);
   void insert(T val){ root = insertR(root, val); }
   Node<T>* removeR(Node<T>*, T);
   void remove(T val){ root = removeR(root, val); }
   bool searchR(Node<T>*, T);
   bool search(T val){ return searchR(root, val); }
   void showTree(){ if (isEmpty()) cout << "The tree is empty." << endl;
        else root->dfs(0); }
private:
   Node<T>* root;
};

   template< typename T >
   Node<T>* BinarySearchTree<T>::insertR(Node<T> *root, T val){
    if (root == 0) return new Node<T>(val);
    if (val < root->getVal())
      root->setLeft(BinarySearchTree<T>::insertR(root->getLeft(), val));
    else root->setRight(BinarySearchTree<T>::insertR(root->getRight(), val));
    return root;
   }

   template< typename T >
   Node<T>* BinarySearchTree<T>::removeR(Node<T> *root, T val){
    if (root == 0) return root;
    if (val < root->getVal())
      root->setLeft(BinarySearchTree<T>::removeR(root->getLeft(), val));
    else if (val > root->getVal())
          root->setRight(BinarySearchTree<T>::removeR(root->getRight(), val));
        else{
      if (root->getLeft())
        if (root->getRight()){  // case 3
          int rightmostofleft = root->getLeft()->rightmost();
          root->setVal(rightmostofleft);

          // Code is made to assume that anything on the left is smaller
          // than the root, and anything equal or greater than is on right.
          // This changes the val of the node that originally had the rightmost
          // val to a smaller val so that it can be deleted with remove().
          if (root->getLeft()->getLeft() == 0 &&
                  root->getLeft()->getRight() == 0 &&
                  root->getLeft()->getVal() == root->getVal()) {
              int count = root->getLeft()->getVal() - 1;
              while (BinarySearchTree<T>::searchR(root->getLeft(), count)) {
                  count--;
              }
              Node<int>* lower_val = new Node<int>(count);
              root->setLeft(lower_val);
              BinarySearchTree<T>::removeR(root, count);
          }
          else {
              BinarySearchTree<T>::removeR(root, rightmostofleft);
            }
            }else return root->getLeft();  // case 2
      else if (root->getRight()) return root->getRight(); // another case 2
      else return 0;  // case 1
    }
    return root;
   }

   template< typename T >
   bool BinarySearchTree<T>::searchR(Node<T> *root, T val){
    if (root == 0) return 0;
    if (val < root->getVal())
      return BinarySearchTree<T>::searchR(root->getLeft(), val);
    else if (val > root->getVal())
      return BinarySearchTree<T>::searchR(root->getRight(), val);
    else return 1;
   }

