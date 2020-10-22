from collections import deque
from collections import defaultdict
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges) -> list:
        # 简单无向图：套路是建图并遍历
        # 建图：邻接表
        # 邻接表为map,其值为list,它的size就是入度数
        if n == 2:
            return [0,1]
        if n == 1:
            return [0]

        adjs = defaultdict(list) # defaultdict写法很有用
        for x in edges: # 图的邻接表表示法,基本是模板
            adjs[x[0]].append(x[1]) # 1:{2}
            adjs[x[1]].append(x[0]) # 2:{1}

        # BFS队列: 初始队列放入初始元素,size=1的为叶子,入队
        queue = deque() # 固定写法
        for key, value in adjs.items():
            if len(value) == 1:
                queue.append(key)

        # BFS两个大循环
        while(queue): # 固定写法
            size = len(queue)  # 固定写法
            n = n - size

            for _ in range(size):
                v = queue.popleft()
                v_adj = adjs[v].pop() # v的邻接仅一个,弹出即删除
                adjs[v_adj].remove(v) # 在v的邻接元素的邻接列表里删除v
                if len(adjs[v_adj]) == 1:
                    queue.append(v_adj)

            if n == 1:
                return [queue.popleft()]
            if n == 2:
                return [queue.popleft(), queue.popleft()]



# class Solution(object):
#     def findMinHeightTrees(self, n, edges):
#         """
#         :type n: int
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         # 思路:
#         # 从最外层遍历,最后一层即为结果.
#
#         if n == 1:
#             return [0]
#
#         # 构造邻接表和度
#         adjs = defaultdict(list)
#         degrees = [0 for _ in range(n)]
#         for (f, t) in edges:
#             adjs[f].append(t)
#             adjs[t].append(f)
#             degrees[f] += 1
#             degrees[t] += 1
#
#         print(adjs)
#         print(degrees)
#         # BFS
#         # 第一层(最外层)
#         layer = []
#         for ind, val in enumerate(degrees):
#             if val == 1:
#                 layer.append(ind)
#         print(layer)
#         # 层层缩进:遍历当前层,确定下一层节点.
#         while layer:
#             next_layer = []
#             for node in layer:
#                 for neighbor in adjs[node]:
#                     degrees[neighbor] -= 1
#                     if degrees[neighbor] == 1:
#                         next_layer.append(neighbor)
#             if not next_layer:  # 下一层没东西了,说明当前遍历的最后一层,也就是我们需要的
#                 return layer
#             layer = next_layer


# class Solution:
#     queue = deque()

#     def findMinHeightTrees(self, n: int, edges: list) -> list:
#         graph = {}
#         for k, v in edges:
#             if k not in graph.keys():
#                 graph[k] = []
#                 graph[k].append(v)
#             else:
#                 graph[k].append(v)

#         print(graph)
#         # bfs start

#         queue += graph

#         _result = set({})
#         minLength = n

#         return list(_result)


if __name__ == "__main__":
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    tests = Solution()
    _data = tests.findMinHeightTrees(n, edges)
    print(_data)

    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    tests2 = Solution()
    _data = tests2.findMinHeightTrees(n, edges)
    print(_data)
