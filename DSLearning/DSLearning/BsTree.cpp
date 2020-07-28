#include <iostream>
#include "BsTree.h"
#include <queue>
#include <climits>

using namespace std;

bool CheckIfBST_Helper(BstNode* root, int minValue, int maxValue);
int max(int a, int b);

BstNode* BsTree::GetNewNode(int data)
{
	BstNode* tmp = new BstNode;
	tmp->data = data;
	tmp->left = tmp->right = nullptr;
	return tmp;
}

BstNode* BsTree::InsertNode(BstNode* root, int data)
{
	if(root == nullptr)
	{
		root = GetNewNode(data);
		return root;
	}

	if(data < root->data)
		return InsertNode(root->left, data);
	return InsertNode(root->right, data);
}

BstNode* BsTree::SearchNode(BstNode* root, int data)
{
	if(root == nullptr || data == root->data)
		return root;

	if(data < root->data)
		return SearchNode(root->left, data);
	return SearchNode(root->right, data);
}

BstNode* BsTree::DeleteNode(BstNode* root, int data)
{
	if(root == nullptr)
		return root;

	if(data < root->data)
		root->left = DeleteNode(root->left, data);
	else if(data > root->data)
		root->right = DeleteNode(root->right, data);
	else
	{
		// Zero children 
		if(root->left == nullptr && root->right == nullptr)
		{
			delete root;
			root = nullptr;
		}

		// Single child
		else if(root->left == nullptr)
		{
			BstNode* tmp = root;
			root = root->right;
			delete tmp;
		}
		else if(root->right == nullptr)
		{
			BstNode* tmp = root;
			root = root->left;
			delete tmp;
		}

		// Two children
		else
		{
			BstNode* tmp = GetMinNode(root->right);
			root->data = tmp->data;
			root->right = DeleteNode(root->right, tmp->data);
		}		
	}

	return root;
}

BstNode* BsTree::GetMinNode(BstNode* root)
{
	if(root == nullptr || root->left == nullptr)
		return root;

	return GetMinNode(root->left);
}

BstNode* BsTree::GetMaxNode(BstNode* root)
{
	if(root == nullptr || root->right == nullptr)
		return root;

	return GetMaxNode(root->right);
}

int BsTree::GetHeight(BstNode* root)
{
	if(root == nullptr)
		return -1;

	return 1 + max(GetHeight(root->left), GetHeight(root->right));
}

void BsTree::LevelOrderTraversal(BstNode* root)
{
	if(root == nullptr)
		return;

	queue<BstNode*> q;
	q.push(root);

	while (!q.empty())
	{
		BstNode* current = q.front();
		cout<<current->data<<" ";

		if(current->left != nullptr)
			LevelOrderTraversal(current->left);
		if(current->right != nullptr)
			LevelOrderTraversal(current->right);

		q.pop();			   
	}
}

void BsTree::PreOrderTraversal(BstNode* root)
{
	if(root == nullptr)
		return;

	cout<<root->data<<" ";
	PreOrderTraversal(root->left);
	PreOrderTraversal(root->right);
}

void BsTree::Inorder(BstNode* root)
{
	if(root == nullptr)
		return;

	PreOrderTraversal(root->left);
	cout<<root->data<<" ";
	PreOrderTraversal(root->right);
}

void BsTree::PostOrder(BstNode* root)
{
	if(root == nullptr)
		return;

	PreOrderTraversal(root->left);
	PreOrderTraversal(root->right);
	cout<<root->data<<" ";
}

bool BsTree::CheckIfBST(BstNode* root)
{
	return CheckIfBST_Helper(root, INT_MIN, INT_MAX);
}

bool CheckIfBST_Helper(BstNode* root, int minValue, int maxValue)
{
		if(root == nullptr)
			return true;

		if((minValue < root->data && maxValue > root->data) 
			&& CheckIfBST_Helper(root->left, minValue, root->data)
			&& CheckIfBST_Helper(root->right, root->data, maxValue))
			return true;
		else
			return false;
}

int max(int a, int b)
{
	if(a>b)
		return a;
	return b;
}
