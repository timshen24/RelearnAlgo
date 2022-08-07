from typing import List
from collections import deque
from string import ascii_lowercase


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        if not endWord in wordList:
            return []
        q = deque([[beginWord, [beginWord]]])
        wordSet = set(wordList) - {beginWord}
        while len(q) > 0:
            for _ in range(len(q)):
                word, curPath = q.popleft()
                for i, char in enumerate(word):
                    for c in ascii_lowercase:
                        nextWord = word[:i] + c + word[i + 1:]
                        if nextWord == endWord:
                            curPath.append(endWord)
                            res.append(curPath)
                        elif nextWord in wordSet:
                            q.append([nextWord, curPath + [nextWord]])
                            wordSet.remove(nextWord)
                            if not wordSet:
                                return []
            if res:
                return res


solution = Solution()
print(solution.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution.findLadders("a", "c", ["a", "b", "c"]))
print(solution.findLadders("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]))
