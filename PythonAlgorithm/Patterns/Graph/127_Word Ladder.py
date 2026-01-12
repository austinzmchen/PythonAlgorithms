class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        from collections import defaultdict, deque
        adj_dict = defaultdict(list)
        
        bw = beginWord
        wordList.append(bw)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                adj_dict[pattern].append(word)

        visit = set([bw])
        q = deque([bw])
        
        res = 1
        while q:
            size = len(q)
            for i in range(size):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for nb in adj_dict.get(pattern, []):
                        if nb not in visit:
                            visit.add(nb)
                            q.append(nb)
            res += 1
            
        return 0
    
    
print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))