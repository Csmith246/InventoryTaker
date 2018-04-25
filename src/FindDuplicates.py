import copy
from Constants import *


# Duplicate output
dupOutput = open(DUPLICATES_OUTPUT, 'w+')

"""Returns line with no line breaks"""
def cleanLine(line):
    line = line.rstrip('\n')
    line = line.rstrip('\r\n')
    return line


"""Finds Duplicate entries and writes to output file"""
def findDuplicates():
        
    # Data file location
    data = DB_DATA_OUTPUT

    f = open(data,"r")

    dataNames = set() # This set maintains names of data that have been processed
    dataDict = {} # Maintains mappings from data name to list of frameworks
                # ex: 'Bikepath' => ['GIS', 'FW']

    for line in f:
        # Clear any potential line breaks from the strings
        line = cleanLine(line)

        dataElems = line.split('.') # should result in list =>
                                    # ex: ['GIS', 'Bikepath']
        framework = dataElems[0]
        data = dataElems[1]
        data = data.replace('_', '') ## Need to do this because one dataName between frameworks is the same
                                      # but has an underscore as the difference between them 
                                      # ie: FW.DOTFacilities and GIS.DOT_Facilities
        
        if data in dataNames:
            dataDict[data].append(framework)
        else:
            dataNames.add(data)
            dataDict[data] = [framework]

    # Write to Output
    headerLine = "DataName;Frameworks\n"
    dupOutput.write(headerLine) # header line
    for key, val in dataDict.items():
        if len(val) > 1:
            seq = (key, str(val))
            dupOutput.write(';'.join(seq) + '\n')

    return dataDict


"""Finds mxds the duplicates are used in and writes them to the output"""
def findMxdsWithDups(dupDict):
    mxdData = MXD_OUTPUT

    mxds = open(mxdData, "r")

    firstLine = mxds.readline() # get special 1st csv line
    firstLine = cleanLine(firstLine)
    headers = firstLine.split(';')
    dataNameIndex = headers.index("Data Name")
    mxdNameIndex = headers.index('Map Document')

    # dict for maintaining FrameWork.DataName => mxds Used in
    resDict = {}

    # init resDict
    for key, val in dupDict.items():
        if len(val)>1:
            for framework in val:
                fullData = framework + '.' + key
                resDict[fullData] = ''


    for line in mxds:
        line = cleanLine(line)
        lineParts = line.split(';')
        dataName = lineParts[dataNameIndex].replace('_', '')
        try:
            resDict[dataName] += lineParts[mxdNameIndex] + '-'
        except:
            pass


    # Write to Output
    headerLine = "FullDataName;MxdsUsedIn\n"
    dupOutput.write(headerLine) # header line
    for key, val in resDict.items():
        if val == '':
            val = 'None'
        seq = (key, val)
        dupOutput.write(';'.join(seq)+'\n')


def run():
    # Run Processes
    dupDict = findDuplicates()
    findMxdsWithDups(dupDict)

    # Close output file
    dupOutput.close()
    

##run()