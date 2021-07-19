package main;

public class TreeNode {
    int val;
    TreeNode left;      // 왼쪽 child
    TreeNode right;     // 오른쪽 child

    // 생성자
    TreeNode() {
    }

    // 파라미터가 하나인 경우
    TreeNode(int val) {
        this.val = val;
    }

    // 파라미터가 두개인 경우
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
