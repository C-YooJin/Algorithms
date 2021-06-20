class Solution {
    public int numJewelsInStones(String jewels, String stones) {

        int count = 0;

        for (Character c : stones.toCharArray()) {
            boolean check = jewels.contains(c.toString());
            if (check) count += 1;

        }
        return count;
    }
}