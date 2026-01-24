import string
import math

LOWERCASE = 26
UPPERCASE = 26
NUMERICAL = 10
SYMBOLS = 32
SPACE = 1

def getSize(password):
    return len(password)

def getUppercaseCount(password):
    upperCount = 0
    for i in password:
        if (i.isupper()):
            upperCount += 1
    return upperCount
            
def getLowercaseCount(password):
    lowerCount = 0
    for i in password:
        if (i.islower()):
            lowerCount += 1
    return lowerCount
    
def getNumericCount(password):
    numericCount = 0
    for i in password:
        if (i.isnumeric()):
            numericCount += 1
    return numericCount

def getSymbolsCount(password):
    symbols = list(string.punctuation)
    symbolsCount = 0
    for i in password:
        if i in symbols:
            symbolsCount += 1
    return symbolsCount

def getSpaceCount(password):
    spaceCount = 0
    for i in password:
        if i == " ":
            spaceCount += 1
    return spaceCount

def getEntropy(password):
    r = 0
    if getLowercaseCount(password):
        r += LOWERCASE
    
    if getUppercaseCount(password):
        r += UPPERCASE
    
    if getNumericCount(password):
        r += NUMERICAL
    
    if getSymbolsCount(password):
        r += SYMBOLS
    
    if getSpaceCount(password):
        r += SPACE
        
    e = math.log2(r**getSize(password))
    
    return e
    
        

# WIP