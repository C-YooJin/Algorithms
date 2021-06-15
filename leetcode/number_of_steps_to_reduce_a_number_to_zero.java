// [leetcode/easy] number_of_steps_to_reduce_a_number_to_zero

class Solution {
    public int numberOfSteps(int num) {

        int sum = 0;
        while (num != 0) {
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num -= 1;
            }
            sum += 1;
        }

        return sum;
    }
}