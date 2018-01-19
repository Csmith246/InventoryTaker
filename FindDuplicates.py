import copy

# Data file location
data = r"C:\WorkSpace\ReportDataSources\testMxds\DatabaseFeatureClasses.txt"

f = open(data,"r")

dataNames = set() # This set maintains names of data that have been processed
dataDict = {} # Maintains mappings from data name to list of frameworks
              # ex: 'Bikepath' => ['GIS', 'FW']

for line in f:
    line = line.rstrip('\n')
    line = line.rstrip('\r\n')
    dataElems = line.split('.') # should result in list like =>
                                # ex: ['GIS', 'Bikepath']
    framework = dataElems[0]
    data = dataElems[1]

    data = data.replace('_', '')
    
    if data in dataNames:
        tempList = copy.copy(dataDict[data]) # best way to do, but it works...
        tempList.append(framework)
        dataDict[data] = tempList
    else:
        dataNames.add(data)
        dataDict[data] = [framework]


# Print out interesting stuff
for key, val in dataDict.items():
    if len(val) > 1: # 2 or more elems in list
        print(key + ': ' + str(val))
