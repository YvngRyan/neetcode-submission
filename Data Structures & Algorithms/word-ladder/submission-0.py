class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        adjList = defaultdict(list)
        
        wordList.append(beginWord)

        for i in range(len(wordList)):
            w1 = wordList[i]
            for j in range(i + 1, len(wordList)):
                w2 = wordList[j]
                diff = 0
                for k in range(len(w1)):
                    if w1[k] != w2[k]:
                        diff += 1
                if diff <= 1:
                    adjList[w1].append(w2)
                    adjList[w2].append(w1)
        
        lvl = 1
        q = collections.deque([beginWord])
        visit = set([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return lvl
                
                for nei in adjList[word]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            lvl += 1
        return 0