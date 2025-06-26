import dictaccess

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
                revRecur = splitMiddlePunctuation(word[:loc])
                revRecur.append(word[loc:])
                return revRecur
        return [word]

def removePrefixes(word : str, prefixFile : str) -> str:
    if dictaccess.isValidWord(word) == False:
        return word
    prefixes = []
    with open(prefixFile, "r") as file:
            prefixes.extend(file.read().split(", "))
    for prefix in prefixes:
        if (word.startswith(prefix)):
            if (len(word[len(prefix) : len(word)]) == 0):
                return word
            if (not dictaccess.isValidWord(word[len(prefix) : len(word)])):
                return word
            return removePrefixes(word[len(prefix) : len(word)], prefixFile)
    return word

def removePostfixes(word : str, postfixFile : str) -> str:
    if dictaccess.isValidWord(word) == False:
        return word
    postfixes = []
    with open(postfixFile, "r") as file:
            postfixes.extend(file.read().split(", "))
    for postfix in postfixes:
        if (word.endswith(postfix)):
            if (len(word[0: -len(postfix)]) == 0):
                return word
            if (not dictaccess.isValidWord(word[0: -len(postfix)])):
                return word
            return removePostfixes(word[0: -len(postfix)], postfixFile)
    return word

class Preprocessing:
    def __init__(self, text : str, lStopWordsFile : str, prefixFile : str, postfixFile : str):
        self._stopWordsFile = lStopWordsFile
        self._tokens = tokenize(text)
        self._prefixFile = prefixFile
        self._postfixFile = postfixFile

    def removeStopWords(self):
        stopWords = [".", ",", "'","\"", ";", ":", "?", "!", "(", ")", "&"]
        newTokens = []
        with open(self._stopWordsFile, "r") as file:
            stopWords.extend(file.read().split(", "))
        for word in self._tokens:
            if word not in stopWords:
                newTokens.append(word)
        self._tokens = newTokens

    def removePrefixes(self):
        newTokens = []
        for word in self._tokens:
            newTokens.append(removePrefixes(word, self._prefixFile))
        self._tokens = newTokens

    def removePostfixes(self):
        newTokens = []
        for word in self._tokens:
            newTokens.append(removePostfixes(word, self._postfixFile))
        self._tokens = newTokens

    def outputTokens(self) -> list[str]:
        return self._tokens
    
    def outputFrequencyDict(self) -> dict[str, int]:
        freqDict = {}
        for word in self._tokens:
            if (word in freqDict.keys()):
                freqDict[word] = freqDict[word] + 1
            else:
                freqDict[word] = 1
        return freqDict