import preprocessing

def load() -> dict[str, str]:
    cvs = {}
    with open("./UpdatedResumeDataSet.csv", "Ur") as file:
        cvList = file.read().split("\n")
        for cv in cvList:
            cvs[cv.split(",")[0]] = cv.split(",")[1]
    return cvs

if __name__ == "__main__":
    stepOne = preprocessing.Preprocessing("Hello World, I'm thinking of code. I said super microcode!".lower(), "./stop_words.csv", "./prefixes.csv", "./postfixes.csv")
    stepOne.removeStopWords()
    stepOne.removePrefixes()
    stepOne.removePostfixes()
    print(stepOne.outputTokens())
    print(stepOne.outputFrequencyDict())