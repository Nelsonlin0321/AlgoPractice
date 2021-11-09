# https://leetcode.com/problems/candy/

"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # at the begining
        candies = [1 for _ in range(len(ratings))]

        for idx in range(len(ratings) - 1):
            left = ratings[idx]
            right = ratings[idx + 1]

            if left < right:
                candies[idx + 1] = candies[idx] + 1

        start = len(ratings) - 2
        end = -1
        for idx in range(start, end, -1):
            left = ratings[idx]
            right = ratings[idx + 1]

            if left > right:
                candies[idx] = max(candies[idx], candies[idx + 1] + 1)

        return sum(candies)


if __name__ == "__main__":
    ratings = [1, 3, 4, 5, 2]
    # start = len(ratings) - 2
    # end = -1
    #
    # for i in range(start, end, -1):
    #     print(i)
    print(Solution().candy(ratings))