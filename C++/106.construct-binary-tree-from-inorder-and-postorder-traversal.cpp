// 106. Construct Binary Tree from Inorder and Postorder Traversal
#include <bits/stdc++.h>
using namespace std;

class Node {
    public:
        int data;
        Node* left;
        Node* right;
    public:
        Node(int data) {
            this->data = data;
            left = NULL;
            right = NULL;
        }
};

int position(vector<int>& inorder, int element, int start, int end) {
    for(int i=start; i<=end; i++) {
        if(inorder[i] == element)
            return i;
    }
    return -1;
}

Node* solve(vector<int>& postorder, vector<int>& inorder, int &postorderIndex, int start, int end) {

    // Base Case
    if(postorderIndex < 0 || start > end) {
        return NULL;
    }

    // element save
    int element = postorder[postorderIndex--];
    Node* root = new Node(element);

    // search element in inorder array
    int pos = position(inorder, element, start, end);

    // find answer by recursion and merge left & right
    // first right call bcoz postorder LRN
    root->right = solve(postorder, inorder, postorderIndex, pos+1, end);
    root->left = solve(postorder, inorder, postorderIndex, start, pos-1);

    return root;
}

Node* buildTree(vector<int>& postorder, vector<int>& inorder) {
    int postorderIndex = postorder.size() - 1;
    return solve(postorder, inorder, postorderIndex, 0, postorder.size() - 1);
}

void lvlOrderTraversal(Node* root) {

    queue<Node*> q;
    q.push(root);
    //change no. 1
    q.push(NULL);

    while(!q.empty()) {
        //tu nikal
        Node* front = q.front();
        q.pop();
        if(front == NULL) {
            cout << endl;
            //catch here
            if(!q.empty())//still elements are present
                q.push(NULL);
        }
        else{
            cout << front->data << " ";

            //bache chor jaio
            if(front->left != NULL)
                q.push(front->left);
            if(front->right != NULL)
                q.push(front->right);
        }
    }
}

int main() {

    vector<int> inorder = {9,3,15,20,7};
    vector<int> postorder = {9,15,7,20,3};

    Node* root = buildTree(postorder, inorder);
    
    lvlOrderTraversal(root);

    return 0;
}