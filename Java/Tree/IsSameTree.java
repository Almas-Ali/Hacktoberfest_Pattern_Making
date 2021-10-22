package com.company;

public class IsSameTree {
    public static void main(String[] args) {
        TreeNode root1 = new TreeNode(1, null, new TreeNode(2, new TreeNode(3), null));
        TreeNode root2 = new TreeNode(1, null, new TreeNode(2, new TreeNode(3), null));
        System.out.println(isSameTree(root1, root2));
    }

    public static boolean isSameTree(TreeNode p, TreeNode q) {
        if (p != null && q != null) {
            return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        } else {
            return p == q;
        }
    }
}
