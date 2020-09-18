from nltk.tokenize import regexp_tokenize
import re

def getTokens_basic(string):
    tokens = string.split(" ")
    return(tokens)

def getTokens(tokens, pattern = r"\w+|\d+"):
    """
    Uses re and nltk to tokenize each string (sentence) in a list into a list of tokens (words).
    
    Parameters
    ----------
    lsOfSent : list of str(s)
        `lsOfSent` is a list of strings, where each string is a sentence (one token of the total doc).
        
    Returns
    -------
    lsOfLsOfToken : list of list(s) of str(s)
        returns a string with all of the text read in from the .txt document directed by `infilePathAndName`
    
    See Also
    --------
        functions.readData : function tailored to read the specific datasets in this repository
    
    """
    
    # pattern = r"\w+|\d+" # grabs words and numbers; removes punctuation
    tokens = regexp_tokenize(token, pattern)
    
    return(tokens)

def get_nGrams(tokens, n):
    """
    Takes in a cleaned string (more cleaning features will
    be brought in later) and returns a list of lists
    of n-grams from the str `string` given that each sublist
    will be of len(`n`).
    
    `n` 
    
    """
    lastTokenLimit = len(tokens) - (n-1)
    grams = []
    for i in range(lastTokenLimit):
        grams.append(tokens[i:(i+n)])
    
    return(grams)

def nGrams(string, n):
    tokens = getTokens(string)
    grams = get_nGrams(tokens, n)
    
    return(grams)