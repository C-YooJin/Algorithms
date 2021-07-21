package main;

class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return solve(p, q);
    }

    private boolean solve(TreeNode root1, TreeNode root2) {

        if (root1 == null && root2 == null) return true;    // leaf node
        if (root1 == null || root2 == null) return false;   // leaf node인데 값이 서로 다른
        if (root1.val != root2.val) {
            return false;
        }

        // solve의 값이 false면 false.. 마지막까지 true면 true
        boolean answer1 = solve(root1.left, root2.left);
        if (answer1==false) return false;

        boolean answer2 = solve(root1.right, root2.right);
        if (answer2==false) return false;

        return true;

    }
}