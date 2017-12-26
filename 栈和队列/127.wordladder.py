def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    def difference(s1, s2):
        index = 0
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                index += 1
        return index == 1
    
    q = [[beginWord, 0]]
    A = set(beginWord)
    while q:
        word = q[0][0]
        step = q[0][1]
        q.remove(q[0])
        
        if difference(word, endWord):
            return step + 1

        for s in wordList:
            if difference(word, s) and (s not in A):
                q.append([s, step+1])
                print q
                A.add(s)
    
    return 0


def ladderLength(self, beginWord, endWord, wordList):
    wordDict = set(wordList)
    if endWord not in wordDict:
        return 0
    length = 2
    front, back = set([beginWord]), set([endWord])
    wordDict.discard(beginWord)
    while front:
        # generate all valid transformations
        front = wordDict & (set(word[:index] + ch + word[index+1:] \
                            for word in front 
                            for index in range(len(beginWord)) \
                            for ch in 'abcdefghijklmnopqrstuvwxyz'))
        if front & back:
            # there are common elements in front and back, done
            return length
        length += 1
        if len(front) > len(back):
            # swap front and back for better performance (fewer choices in generating nextSet)
            front, back = back, front
        # remove transformations from wordDict to avoid cycle
        wordDict -= front
    return 0
