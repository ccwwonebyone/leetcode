from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dps(0, graph, [0], res)
        return res

    def dps(self, index, graph, path: List[int], paths: List[List[int]]):
        if len(graph) - 1 in path:
            paths.append(path)
            return

        for i in graph[index]:
            pathc = path.copy()
            pathc.append(i)
            self.dps(i, graph, pathc, paths)


if __name__ == "__main__":
    solution = Solution()
    # print(solution.allPathsSourceTarget([[1, 2], [3], [3], []]))
    # print(solution.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
    print(solution.allPathsSourceTarget([[4,3,1],[3,2,4],[],[4],[]]))
