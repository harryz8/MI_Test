import requests

def isValidWord(text : str) -> bool:
    siteHTML = requests.get("https://www.dictionary.com/browse/{}".format(text)).text
    return text in siteHTML