from typing import (
    List,
)
from collections import defaultdict
from heapq import heapify, heappop, heappush

        
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    ##
    #   啥是输出的时候按照lexicographically，对这题有啥影响。
    #   如果同时在indegree==0的字符里出现了 b 和 c，先输出正常字典序最小的，所以这里使用最小堆很对口。
    ## 
    def alien_order2(self, words: List[str]) -> str:
        # get all chars and edges
        edges = set()
        chars = set(c for w in words for c in w)

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                  edges.add((w1[j], w2[j]))
                  break
        # init adj-dict and in-degrees
        adj_dict = {}
        in_degree = {}
        for c in chars:
          adj_dict[c] = []
          in_degree[c] = 0
          
        for e in edges:
            adj_dict[e[0]].append(e[1])
            in_degree[e[1]] += 1

        queue = [k for k, v in in_degree.items() if v == 0]
        # use heap because preserving natural order of the char
        heapify(queue)
        
        res = []
        while queue:
            node = heappop(queue)
            res.append(node)
            for adj in adj_dict[node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    heappush(queue, adj)
        
        # if there is loop for example
        if len(res) != len(chars):
          return ''
        return ''.join(res)


    """
    @param words: a list of words
    @return: a string which is correct order
    """
    # https://www.lintcode.com/problem/892/solution/16945
    def alien_order(self, words):
      # Construct Graph
      in_degree = {ch: 0 for word in words for ch in word}
      neighbors = {ch: [] for word in words for ch in word}
      for pos in range(len(words) - 1):
          for i in range(min(len(words[pos]), len(words[pos+1]))):
              pre, next = words[pos][i], words[pos+1][i]
              if pre != next:
                in_degree[next] += 1
                neighbors[pre].append(next)
                break
      
      # Topological Sort
      heap = [ch for ch in in_degree if in_degree[ch] == 0]
      heapify(heap)
      order = []
      while heap:
          for _ in range(len(heap)):
              ch = heappop(heap)
              order.append(ch)
              for child in neighbors[ch]:
                  in_degree[child] -= 1
                  if in_degree[child] == 0:
                      heappush(heap, child)
      
      # order is invalid
      if len(order) != len(in_degree):
          return ""
      return ''.join(order)


sol = Solution()
print("Character order: " + sol.alien_order(["wrt","wrf","er","ett","rftt"]))
print("Character order: " + sol.alien_order(["zy","zx"]))
print("Character order: " + sol.alien_order(["ab","adc"]))
print("Character order: " + sol.alien_order(["abc","ab"]))