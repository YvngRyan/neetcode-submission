class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        lettersAfter = { c : [] for w in words for c in w } 
        for i in range(1, len(words)):
            if not (self.compareWords(words[i - 1], words[i], lettersAfter)):
                return ""
        
        return self.topSort(lettersAfter)
        
    def compareWords(self, w1, w2, lettersAfter):
        w1Idx = 0
        w2Idx = 0

        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return False

        while w1Idx < len(w1) and w2Idx < len(w2):
            if w1[w1Idx] != w2[w2Idx]:
                lettersAfter[w1[w1Idx]].append(w2[w2Idx])
                return True
            w1Idx += 1
            w2Idx += 1
        return True
        

    def topSort(self, lettersAfter):
        # lettersAfter = { "z" : ["o"] }
        topo = ""
        visit = set()
        path = set()
        def dfs(letter):
            nonlocal topo
            if letter in path:
                return False
            if letter in visit:
                return True
            
            path.add(letter)
            for ltrAfter in lettersAfter[letter]:
                if not dfs(ltrAfter):
                    return False
            
            topo += letter
            path.remove(letter)
            visit.add(letter)
            return True

        
        for letter in lettersAfter:
            if not dfs(letter):
                return ""
        
        return topo[::-1]