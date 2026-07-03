class Solution(object):
    def mostWordsFound(self, sentences):
        maxi = 0
        for sentence in sentences:
            words = sentence.split()
            maxi = max(maxi, len(words))
        return maxi

        