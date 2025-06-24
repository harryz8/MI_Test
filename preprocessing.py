def _splitPunctuation(word : str) -> list[str]:
        """
        no middle puctuation is split on
        """
        for punc in [".", ",", "'","\"", ";", ":", "?", "!", "(", ")", "&"]:
            if (word.startswith(punc)):
                revRecur : list[str] = _splitPunctuation(word[1:])
                revRecur.reverse()
                revRecur.append(word[0])
                revRecur.reverse()
                return revRecur
        for punc in [".", ",", "'","\"", ";", ":", "?", "!", "(", ")", "&"]:
            if (word.endswith(punc)):
                revRecur = _splitPunctuation(word[:-1])
                revRecur.append(word[-1])
                return revRecur
        # for punc in [".", ",", "'","\"", ";", ":", "?", "!", "(", ")", "&"]:
        #     if (punc in word):
        #         loc = word.find(punc)
        #         revRecur = _splitPunctuation(word[:loc])
        #         revRecur.append(word[loc:])
        #         return revRecur
        return [word]

def tokenize(text : str) -> list[str]:
        orig = text.split(" ")
        multiList = [_splitPunctuation(word) for word in orig]
        return [word for listR in multiList for word in listR]

def splitMiddlePunctuation(word : str) -> list[str]:
        for punc in [".", ",", "'","\"", ";", ":", "?", "!", "(", ")", "&"]:
            if (punc in word and (not word.startswith(punc)) and (not word.endswith(punc))):
                loc = word.find(punc)
                revRecur = self._splitMiddlePunctuation(word[:loc])
                revRecur.append(word[loc:])
                return revRecur
        return [word]

class Preprocessing:
    def __init__(self, text : str, lStopWordsFile : str):
        self._stopWordsFile = lStopWordsFile
        self._tokens = tokenize(text)

    def removeStopWords(self):
        stopWords = [".", ",", "'","\"", ";", ":", "?", "!", "(", ")", "&"]
        newTokens = []
        with open(self._stopWordsFile, "r") as file:
            stopWords.extend(file.read().split(", "))
        for word in self._tokens:
            if word not in stopWords:
                newTokens.append(word)
        self._tokens = newTokens

    def output(self) -> list[str]:
         return self._tokens