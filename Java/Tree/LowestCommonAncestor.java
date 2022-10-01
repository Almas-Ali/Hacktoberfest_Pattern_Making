class Solution {
    public boolean find(TreeNode root,TreeNode n)
    {
           if(root==null)return false;
            return root.val==n.val || find(root.left,n) || find(root.right,n);
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode a, TreeNode b) {
       // if(root==null) return null;
        if(a.val==root.val || b.val==root.val)return root;
        
        if(find(root.left,a))
        {
            if(find(root.left,b)) return lowestCommonAncestor(root.left,a,b);
            else return root;
        }
        else if(find(root.right,b)) return lowestCommonAncestor(root.right,a,b);
        
        else return root;
    }
}
