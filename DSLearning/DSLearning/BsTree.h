#include "Nodes.h"

class BsTree
{
	public:
		bool CheckIfBST(BstNode* root);
		BstNode* InsertNode(BstNode* root, int data);
		BstNode* SearchNode(BstNode* root, int data);
		BstNode* DeleteNode(BstNode* root, int data);
		BstNode* GetMaxNode(BstNode* root);
		BstNode* GetMinNode(BstNode* root);
		int GetHeight(BstNode* root);

		// Breadth first traversal
		void LevelOrderTraversal(BstNode* root);

		// Depth first traversal
		void PreOrderTraversal(BstNode* root);
		void Inorder(BstNode* root);
		void PostOrder(BstNode* root);

	private:
		BstNode* GetNewNode(int data);
};