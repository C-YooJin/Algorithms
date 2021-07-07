# Algorithms
Algorithms source code (python, java)

- LeetCode
- Programmers
- Baekjoon
- Codility
- Real Coding Test

# Commit m
- ex) [leetcode/easy] Number of Steps to Reduce a Number to Zero (url)
- ex) [leetcode/easy] Number of Steps to Reduce a Number to Zero (solve)
<br>

# Solve Everyday

### 2021.06.15 (Tue)
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
  - 이건 우선탐색문제라고 생각하고 집었는데, 그것보다 자바의 TreeNode 타입에 대해서 생각해보게 해 준 문제다 
  - `root.val, root.left, root.right` 이런 것들 
  - leaf node: 자식 노드가 없는 노드

### 2021.06.16 (Wed)
- [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)
  1. 주어진 root값(TreeNode)를 그래프로 만든다
  2. BFS로 탐색
     - `target`에서 모든 노드로 탐색해서 `distance`가 `K`면 멈춘다
  3. Corner case를 고민한다
     - `target`으로부터 `distance`가 `K`인 노드가 없는 경우
     - 애초에 `root`가 `None`인 경우
  4. 가능하다면 시간복잡도 최적화

### 2021.06.17 (Thu)
- [542. 01 Matrix](https://leetcode.com/problems/01-matrix/)

### 2021.06.18 (Fri)
- [Review] leetcode 100, 863, 542

### 2021.06.19 (Sat)
- [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
  1. jewels에 할당 된 문자가 stone에 몇 개 있는지 count해서 return
  2. 2중 loop로 하면 간단하지만 다른 케이스도 찾아
  - 다른 케이스
    - `toCharArray()` 활용하는 방법
    - 문자열 -> 배열 -> 집합(`set`) -> `contains`

### 2021.06.20 (Sun) 
- 일주일동안 푼 문제 다시 풀고, 못 풀었다면 원인 체킹

### 2021.06.21 (Mon)
- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
  1. 두 노드가 Null인 경우 check
  2. 한 노드만 Null인 경우 check
  3. 두 노드의 값이 같은 경우 check -> 재귀

### 2021.06.22 (Tue)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

### 2021.06.23 (Wed)
- 회사 업무

### 2021.06.24 (Thu)
- 회사 업무

### 2021.06.25 (Fri)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

### 2021.06.26 (Sat)
- 앞에 푼 문제들 복습
  - 100, 863, 542, 771, 101, 70 

### 2021.06.27 (Sun) - 2021.07.02 (Fri)
- 프로젝트 발표 기간이라 알고리즘 잠깐 홀딩. 앞에 푼 문제들 보면서 체화.

### 2021.07.06 (Tue)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### 2021.07.07 (Wed)
- [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
  - 재귀로는 쉽게 풀리는데 Iterative 접근방식은 알아야 할 빌트인 자료구조가 많은편. 학습중.
