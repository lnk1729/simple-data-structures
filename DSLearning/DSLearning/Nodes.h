#pragma once

typedef struct listNode{
	int data;
	struct listNode* next;
} ListNode;


typedef struct bstNode{
	int data;
	struct bstNode* left;
	struct bstNode* right;
} BstNode;

