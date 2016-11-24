#include "avl.h"
#include <cstdlib>

int main(){
    AVLTree< int> tree;
    for (int i = 0; i < 100; i++){
        tree.insert(rand() % 100);
        tree.showTree();
    }
}

