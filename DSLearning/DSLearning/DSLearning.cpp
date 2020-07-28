#include <iostream>
#include "BsTree.h"

using namespace std;

int main()
{
	BsTree* tree = nullptr;
	BstNode* mainRoot = nullptr;
    mainRoot = tree->InsertNode(mainRoot, 15);
	tree->LevelOrderTraversal(mainRoot);
}


