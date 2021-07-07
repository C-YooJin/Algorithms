package main;

import javax.swing.tree.TreeNode;

public class MaximumDepthOfBinaryTree {

    public int maxDepth(TreeNode root) {

        if (root == null)
            return 0;
        if (root.left == null && root.right == null)
            return 1;

        int depth1 = 1 + maxDepth(root.left);
        int depth2 = 1 + maxDepth(root.right);

        return Math.max(depth1, depth2);

    }

}
