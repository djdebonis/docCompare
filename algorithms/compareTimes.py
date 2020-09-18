# preprocessing data for all tests
import process
# original function written
import original
# functions with getUnique preprocessing
import getUnique
# functions with clear
import clear

import time
import nltk.corpus as corpus
corpus.genesis.fileids()
genesis = corpus.genesis.raw('english-kjv.txt')
genesis

def openAndRead(infilePathAndName):
    """
    opens a file and returns a long long long string
    
    Parameters
    ----------
    infilePathAndName : str
        `infilePathAndName` is the string containing the filepath to the doc the user would like
        to read in; it is the relative filepath from the current working directory.
        
    Returns
    -------
    string : str
        returns a string with all of the text read in from the .txt document directed by `infilePathAndName`
    
    See Also
    --------
        functions.readData : function tailored to read the specific datasets in this repository
    
    
    """
    with open(infilePathAndName, 'r') as file:
        string = file.read()
        
    return(string)

revelationRaw = openAndRead("revelation.txt")

rose = "a rose is a rose is a rose is a rose is a rose is a rose"
# figure out how to deal with contractions
rose2 = "a rose is only a rose if a rose is a rose but could a rose be a rose if a rose is not a rose? how could a rose be a rose?"
size = 2
roseGram = process.nGrams(rose, size)
roseGram2 = process.nGrams(rose2, size)

# test the original function ##########################
timeOrigStart = time.time()

origUnion = original.getUnion(roseGram, roseGram2)
origIntersect = original.getIntersect(roseGram, roseGram2)

#print(origUnion)
#print(origIntersect)

timeOrigEnd = time.time()

timeOrig = timeOrigEnd - timeOrigStart
print(timeOrig)

#######################################################

# test the getUnique functions ########################
timeUniqueStart = time.time()

uniqueUnion = getUnique.getUnion(roseGram, roseGram2)
uniqueIntersect = getUnique.getIntersect(roseGram, roseGram2)

#print(uniqueUnion)
#print(uniqueIntersect)

timeUniqueEnd = time.time()

timeUnique = timeUniqueEnd - timeUniqueStart
print(timeUnique)

#######################################################

# test the clear functions ############################
timeClearStart = time.time()

clearUnion = clear.getUnion(roseGram, roseGram2)
clearIntersect = clear.getIntersect(roseGram, roseGram2)

timeClearEnd = time.time()

timeClear = timeClearEnd - timeClearStart
print(timeClear)

#######################################################
