package main;

import javax.swing.tree.TreeNode;
import java.util.*;
import java.lang.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Pair {
    public TreeNode first;
    public Integer second;
    public Pair(TreeNode first, Integer second) {
        this.first = first;
        this.second = second;
    }
}
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        Map<TreeNode, TreeNode> parents = new HashMap<>();
        dfs(parents, root, null);

        Queue<Pair> queue = new LinkedList<>();
        Set<TreeNode> seen = new HashSet<>();

        queue.add(new Pair(target, 0));
        seen.add(target);
        while(!queue.isEmpty()) {
            if(queue.peek().second == K) {          
                List<Integer> result = new ArrayList<>();
                while(!queue.isEmpty())
                    result.add(queue.remove().first.val);
                return result;
            }

            // 이웃한 노드로 이동
            Pair cur = queue.remove();
            TreeNode node = cur.first;
            int dist = cur.second;

            TreeNode[] neighbors = {
                    node.left,
                    node.right,
                    parents.get(node)
            };
            for(TreeNode neighbor : neighbors) {
                if(neighbor != null && !seen.contains(neighbor)) {
                    int new_dist = dist + 1;
                    seen.add(neighbor);
                    queue.add(new Pair(neighbor, new_dist));
                }
            }
        }
        return new ArrayList<Integer>();
    }

    // 기본 그래프 만들기
    private void dfs(Map<TreeNode, TreeNode> parents, TreeNode node, TreeNode parent) {
        if(node != null) {                  // 노드가 null이 아니면
            parents.put(node, parent);
            dfs(parents, node.left, node);
            dfs(parents, node.right, node);
        }
    }
}