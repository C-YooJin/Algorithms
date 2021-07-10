package main;

public class RangeSumOfBST {
    int sum = 0;
    public int rangeSumBST(TreeNode root, int L, int R) {

        if (root == null) {
            return 0
        }
        else {
            if (root.val >= L && root.val <= R) {
                sum += root.val
            }

            rangeSumBST(root.left, L, R);
            rangeSumBST(root.rignt, L, R);
        }

        return sum;

}
