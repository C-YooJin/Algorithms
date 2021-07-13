package main;

import com.sun.source.tree.Tree;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class SymmetricTree {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> list = new LinkedList<>();

        TreeNode tree = new TreeNode();
    }

    public static boolean isSymmetric(TreeNode root) {

        return check(root.left, root.right);
    }


    public static boolean check(TreeNode left, TreeNode right){
        if (left == null && right == null) return true;
        else if (left == null || right == null) return false;

        if (left.val == right.val) {
            return check(left.right, right.left) && check(left.left, right.right);
        }
        else return false;
    }

}
