# preprocessing data for all tests
import process
# original function written
import original
# functions with getUnique preprocessing
import getUnique
# functions with clear
import clear

rose = "a rose is a rose is a rose"
rose2 = "a rose is only a rose if a rose is a rose but could a rose be a rose if a rose isn't a rose?"
size = 4
roseGram = process.nGrams(rose, size)
roseGram2 = process.nGrams(rose2, size)