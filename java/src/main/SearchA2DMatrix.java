package main;

public class SearchA2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) return false;

        int row = matrix.length - 1;
        int col = 0;   // 왼쪽 아래서 시작하니까 컬럼값은 0

        while(row >= 0 && col < matrix[0].length) {
            int value = matrix[row][col];

            if (target == value) {
                return true;
            } else if (target < value) {
                row--;      // 타겟이 value보다 작으면 위로
            } else {
                col++;
            }
        }


        return false;
    }
}
