# preprocessing data for all tests
import process
# original function written
import original
# functions with getUnique preprocessing
import getUnique
# functions with clear
import clear

import time

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
