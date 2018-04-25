from Constants import *


# Recursive function for maintenance of list of lists
# Returns: A list properly updated with the added mxdName
def increCount(listOfLists, mxdName):
    if len(listOfLists)==0:
        return [[mxdName, 1]]
    else:
        firstElem = listOfLists[0]
        if firstElem[0] == mxdName:
            firstElem[1] += 1
            return listOfLists
        else:
            res = increCount(listOfLists[1:],mxdName)
            return [firstElem] + res


"""
Returns dataDict - a dictionary that contains DB data names as keys, and empty arrays as
values.
Ex output => {"GIS.FederalAidEligibleRoads":[],"GIS.RIS_LINEAR_FEATURES_TEST":[]...}
"""
def fromDBData():
    # Open data file (has list of all Data in Oracle DB) 
    dbDataPath = DB_DATA_OUTPUT
    dbData = open(dbDataPath, 'r')

    # Make a Dict with the data names as keys and empty arrays as values
    # (arrays will keep track of data from the MXD_OUTPUT file)
    dataDict = {}
    for line in dbData:
        # To make sure no line separators are present
        line = line.rstrip('\n')
        line = line.rstrip('\r\n')
        # Initial value
        dataDict[line] = []

    # Close dbData
    dbData.close()

    return dataDict


"""
Params - dataDict - a dictionary that contains DB data names as keys, and empty arrays as
values.
This function processes MXD_OUTPUT data and updates dataDict value arrays with which mxd used
the dbData and keeps a count of how many times that data is used in each mxd that uses it
Ex output => {"GIS.FederalAidEligibleRoads":[["FAE.mxd", 3],["maintviewer.mxd", 1]],
              "GIS.RIS_LINEAR_FEATURES_TEST":[["RestAreas.mxd", 2]], ...}

Returns: List containing mystery data - data that is in an mxd, but is not in the DB
"""
def fromMxdData(dataDict):
    
    # Open file with .mxds data
    mxdsDataPath = MXD_OUTPUT
    mxdsData = open(mxdsDataPath, 'r')

    firstLine = mxdsData.readline() # get special 1st csv line
    headers = firstLine.split(';')
    mxdNameIndex = headers.index("Map Document")

    dataNameIndex = headers.index("Data Name")

    mysteryData = [] # Mxd data names not in dataDict

    for line in mxdsData:
        line = line.replace('\n','')
        splitLine = line.split(';')
        mxdName = splitLine[mxdNameIndex]
        dataName = splitLine[dataNameIndex]
        
        try:
            dataDict[dataName] = increCount(dataDict[dataName], mxdName)
        except:
            if dataName not in mysteryData:
                mysteryData.append(dataName)

    # Close mxdsData
    mxdsData.close()

    # Loop through dict, find any keys that still have empty array as value. Update to
    # show no map is using that data
    for key, val in dataDict.items():
        if len(val) == 0:
            val.append(['No Map Using', 0])

    return mysteryData
    


def firstFormat(dataDict):
    outputFile = open(FINAL_OUTPUT_1, "w+")

    outputFile.write("Data Name;MxdUsedIn;CountPerMxd;CountTotal\n")

    dictCounter = 0
    writerCounter = 0
    # Output
    for key, val in dataDict.items():
        dictCounter += 1
    ##    print(dictCounter)
        if key == 'FW.State':
            # print(key)
            # print(val)
            pass
        dataName = key

        count = 0
        for mxdAndNum in val: # Calculate total
            count += mxdAndNum[1]
        for mxdAndNum in val:
            seq = (dataName, mxdAndNum[0], str(mxdAndNum[1]), str(count))
            writerCounter += 1
            #print('In write')
            outputFile.write(';'.join(seq)+'\n')
            #print(writerCounter)


    outputFile.close()
    #print("Data not in DB", mysteryData)

def secondFormat(dataDict):
    outputFile = open(FINAL_OUTPUT_2, "w+")

    outputFile.write("DataName;UsedInMxd;CountUsed\n")

    collector = []

    # Output
    for key, val in dataDict.items():
        dataName = key
        count = 0
        for mxdAndNum in val: # Calculate total
            count += mxdAndNum[1]
        collector.append([dataName, count])
        

    def sortFunc(ls):
        return ls[0][0]

    sortedList = sorted(collector, key=sortFunc)

    for elem in sortedList:
        dataName = elem[0]
        count = elem[1]
        seq = (dataName, 'No' if count==0 else 'Yes', str(count))
        outputFile.write(';'.join(seq)+'\n')

    
    outputFile.close()
    

### Main Logic ####
def run():

    dataDict = fromDBData()
   # print(dataDict)
    mysteryData = fromMxdData(dataDict)
    # print(dataDict)



    # print mysteryData
    # print("Data not in DB", mysteryData)

    ### Choose which Format to make
    firstFormat(dataDict)
    secondFormat(dataDict)

    #########################


