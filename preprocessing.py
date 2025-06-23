def _splitPunctuation(word : str) -> list[str]:
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
    for punc in [".", ",", "'","\"", ";", ":", "?", "!", "(", ")", "&"]:
        if (punc in word):
            loc = word.find(punc)
            revRecur = _splitPunctuation(word[:loc])
            revRecur.append(word[loc:])
            return revRecur
    return [word]

def tokenize(text : str) -> list[str]:
    orig = text.split(" ")
    multiList = [_splitPunctuation(word) for word in orig]
    return [word for listR in multiList for word in listR]