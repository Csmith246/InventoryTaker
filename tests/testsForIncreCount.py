
# Recursive function for maintenance of list of lists
# Returns: A list properly updated with the added mxdName
def increCount(listOfLists, mxdName):
##    print("NEW ITERATION| listOfLists Input ---->", listOfLists)
    if len(listOfLists)==0:
##        print("IN BASE Case")
        return [[mxdName, 1]]
    else:
##        print("NOT IN BASE")
        firstElem = listOfLists[0]
##        print('firstElem', firstElem)
        if firstElem[0] == mxdName:
            firstElem[1] += 1
##            print('firstElem in case where matches', firstElem)
            return listOfLists
        else:
##            print('firstElem in case where does not match', firstElem)
            res = increCount(listOfLists[1:],mxdName)
##            print('res of FUNC CALL', res)
            return [firstElem] + res


###### increCount function testing #######

### helper func for testing
def comp(LOLtest, LOLtrue):
    if len(LOLtest)!=len(LOLtrue):
        return False
    for el1, el2 in zip(LOLtest, LOLtrue):
        if el1[0]==el2[0] and el1[1]==el2[1]:
            pass # elems are the same. result is still true
        else:
            return False
    return True


LOL1 = [['hello',1],['IamAmap',7]]

LOL1 = increCount(LOL1,'hello')
print(comp(LOL1, [['hello',2],['IamAmap',7]]))

LOL1 = increCount(LOL1,'herrow')
print(comp(LOL1, [['hello',2],['IamAmap',7],['herrow',1]]))

LOL1 = increCount(LOL1,'hello')
print(comp(LOL1, [['hello',3],['IamAmap',7],['herrow',1]]))

LOL1 = increCount(LOL1,'map4')
print(comp(LOL1, [['hello',3],['IamAmap',7],['herrow',1],['map4',1]]))

print('\nNew LOL\n')
LOL2 = []

LOL2 = increCount(LOL2, 'Test1')
print(comp(LOL2, [['Test1',1]]))

LOL2 = increCount(LOL2, 'Test2')
print(comp(LOL2, [['Test1',1],['Test2',1]]))

LOL2 = increCount(LOL2, 'Test3')
print(comp(LOL2, [['Test1',1],['Test2',1],['Test3',1]]))

LOL2 = increCount(LOL2, 'Test1')
print(comp(LOL2, [['Test1',2],['Test2',1],['Test3',1]]))


##
######## END TESTING ########
