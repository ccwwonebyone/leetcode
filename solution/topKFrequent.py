from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sort_info = {}
        for num in nums:
            if not sort_info.get(num):
                sort_info[num] = 1
            else:
                sort_info[num] += 1
        sort_info = sorted(sort_info.items(), key=lambda x:x[1], reverse=True)
        return [i[0] for i in sort_info[:k]]

if __name__ == '__main__':

    solution = Solution()
    print(solution.topKFrequent([23,3,3,3,2,2,2,23,3,3], 3))
