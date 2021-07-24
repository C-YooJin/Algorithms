package test.java;

import org.junit.Test;
import java.util.*;

public class BinaryTreePathTest {

    public BinaryTreePathTest() {

    }

    @Test
    public static List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        dfs(root, "", result);
        return result;

    }
    public static void dfs(TreeNode root, String path, List<String> paths) {
        path += root.val;
        if (root.left == null && root.right == null) {
            paths.add(path);
            return;
        }

        if(root.left != null){
            dfs(root.left, path + "->", paths);
        }
        if(root.right != null) {
            dfs(root.right, path + "->", paths);
        }
    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode();
        root = [1,2,3,null,5];

        binaryTreePaths(root);
    }

}
