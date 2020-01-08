class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # 1. Read the words and expansion count into a Dict/Tuple

        # 2. Find in which word K lies after expansion

        # 3. If K lies after n words, Substract the expanded lenght of the n words from K. (n could be 0 makind putting K in first word)

        # 4. After fixing in on the word, get the expansion and find the modulous of K % repition. 

        # 5. Return the index value calcuated step 4 and retun the value at that index of the word 

        # Step 1
        words = list()
        import re

        regex = r"([a-zA-Z]+)(\d*)"

        matches = re.finditer(regex, S, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            r = match.groups()[1]
            words.append( (match.groups()[0],  int(r) if r else 0 ) )

        
        print(words)
        # Step 2, 3
        wordAtIndex = None
        l = 0
        k = K

        for w, r in words:
            l = len(w) * r
            wordAtIndex = w
            if k >= l:
                k = k - l
            else:
                break
            print("word %s r %d k %d l %d " %(w, r, k, l) )

        # Step 4
        index = (k % len(wordAtIndex))
        print(wordAtIndex)

        return wordAtIndex[index ]


s = Solution()

a = s.decodeAtIndex(S = "leet2code3", K = 10)
print(a)


# a = s.decodeAtIndex(S = "ha11", K = 5)
# print(a)
# a = s.decodeAtIndex(S = "a2345678999999999999999", K = 1)
# print(a)

# a = s.decodeAtIndex(S = "abc", K = 1)
# print(a)

# a = s.decodeAtIndex(S = "a2b3c4d5e6f7g8h9", K = 3)
# print(a)

# a = s.decodeAtIndex(S = "a2b3c4d5e6f7g8h9", K = 9)
# print(a)
