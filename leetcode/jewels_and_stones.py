class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        cnt = 0

        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    cnt += 1

        return cnt