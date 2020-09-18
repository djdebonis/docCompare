def getUnion(set1, set2):
    """
    Takes two sets (each set is a list of lists) and returns
    the union of the two sets (a list of lists); i.e. returns
    a single set of all of the unique sets between the two sets
    given in the arguments. (what a mouth-full)
    
    """
    
    unionSet = []
    
    for index,ngram in enumerate(set1):
        if ngram not in unionSet:
            unionSet.append(ngram)
            
    for index,ngram in enumerate(set2):
        if ngram not in unionSet:
            unionSet.append(ngram)
            
    return(unionSet)

def getIntersect(set1, set2):
    """
    Takes two sets (each set is a list of lists) and returns
    the intersection of the two sets (a list of lists); i.e. returns
    a single set of all of the unique sets that are in both `set1` 
    and `set2`
    
    *This is an extremely heavy function and is going to take some*
    *algorithm analysis to make more efficient*
    
    
    * What if we first isolate each set to only have uniques, then compare them?
    
    """
    
    intersectSet = []
    
    # two options:
    
    # option 1: first check if already in intersectionSect then check if in both sets
    for index,ngram in enumerate(set1):
        if ngram not in intersectSet:
            if ngram in set2:
                intersectSet.append(ngram)
                set1.clear(ngram)
                set2.clear(ngram)
    
 
    return(intersectSet)