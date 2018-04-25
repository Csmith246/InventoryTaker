import arcpy, datetime, os
from Constants import *


def listMapData():
    arcpy.env.overwriteOutput = True
    #r'P:\Temporary Data Exchange\HK\toCSmith'#
    #Read input parameters from GP dialog
    folderPath = MXD_SOURCE_FOLDER #\\wvmoap134\Projects"#r"C:\WorkSpace\ReportDataSources\testMxds"#arcpy.GetParameterAsText(0)
    output = MXD_OUTPUT #arcpy.GetParameterAsText(1)

    #Create an output file
    outFile = open(output, "w+")
    #Moved to before loop so you only write the headers once, note linebreak '\n' character
    outFile.write("Map Document;MXD Path;DataFrame Name;DataFrame Description;Data Name;Layer name;Layer Datasource;DB User\n")


    # List of mxds suspected to be corrupted - when any are included, python.exe crashes
    blackList = ["MilepointLocations.mxd","NYSDOTQuadrangles.mxd","R7Data.mxd","r1_Contracts.mxd"]
    # tried converting them to 10.3, but still no luck

    #Loop through each MXD file
    for root, dirs, files in os.walk(folderPath):
    ##    print(files)
        for file in files: # files is a list of files in the current directory
            if file.lower().endswith(".mxd") and file not in blackList: #############<======================= Black List
                #print(file)
                fullpath = os.path.join(root, file) # root is the current directory
                #Reference MXD
    ##            print("B4 MapDoc")
                mxd = arcpy.mapping.MapDocument(fullpath)
    ##            print("Aft MapDoc")
                #Write MXD data to file
                MapDoc = os.path.basename(mxd.filePath)
                MapDocPath = mxd.filePath

                #Reference each data frame and report data
                #print("B4 ListDF")
                try:
                    DFList = arcpy.mapping.ListDataFrames(mxd)
                except:
                    pass
                   # print('IN EXCEPT')
                # print("Aft ListDF")
                for df in DFList:
                    #Format output values
                    if df.description == "": descValue = "None"
                    else: descValue = df.description
                    #==== Note the new descName variable
                    descName=df.name

                    #Reference each layer in a data frame
                    lyrList = arcpy.mapping.ListLayers(mxd, "", df)
                    for lyr in lyrList:
                        lyrName = lyr.name
                        if lyr.supports("datasetName"):
                            dataName = lyr.datasetName #HK
                        else: dataName ="N/A2"
                        if lyr.supports("dataSource"):
                            lyrDatasource = lyr.dataSource
                            
                            lastIndex = lyrDatasource.rfind("\\") # last backslash
                            userTemp = lyrDatasource[:lastIndex]
                            secondToLast = userTemp.rfind("\\") # 2nd to last backslash
                            dbUser = userTemp[secondToLast+1:]
                            #print(dbUser)
                            
                            dotSplit = dbUser.split('.')
                            fileType = dotSplit[-1]
                            #print(fileType)
                            if fileType != 'sde': # deal with non .sde files
                                dbUser = 'N/A'
                            
                        else:
                            lyrDatasource = "N/A"
                            dbUser = "N/A"
                        #==== Got rid of DFList and inserted descName instead
                        seq = (MapDoc, MapDocPath, descName, descValue, dataName, lyrName, lyrDatasource, dbUser);
                        #==== Got rid of "str" variable and just used a string literal - ','
                        outFile.write(';'.join(seq)+'\n')
                del mxd

    outFile.close()

def run():
    listMapData()
