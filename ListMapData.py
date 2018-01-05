import arcpy, datetime, os

arcpy.gp.overwriteOutput = True

#Read input parameters from GP dialog
folderPath = r"D:\GIS\python\ReportDataSources\testMxds"#arcpy.GetParameterAsText(0)
output = r"D:\GIS\python\ReportDataSources\testMxds\DataSourcestest.txt" #arcpy.GetParameterAsText(1)

#Create an output file
outFile = open(output, "w")
#==== Moved to before loop so you only write the headers once, note linebreak '\n' character
outFile.write("Map Document;MXD Path;DataFrame Name;DataFrame Description;Data Name;Layer name;Layer Datasource\n")

#Loop through each MXD file
for root, dirs, files in os.walk(folderPath):
    for file in files: # files is a list of files in the current directory
        if file.lower().endswith(".mxd"):
            fullpath = os.path.join(root, file) # root is the current directory
            #Reference MXD
            mxd = arcpy.mapping.MapDocument(fullpath)

            #Write MXD data to file
            MapDoc = os.path.basename(mxd.filePath)
            MapDocPath = mxd.filePath

            #Reference each data frame and report data
            DFList = arcpy.mapping.ListDataFrames(mxd)
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
                    else: lyrDatasource = "N/A"
                    #==== Got rid of DFList and inserted descName instead
                    seq = (MapDoc, MapDocPath, descName, descValue, dataName, lyrName, lyrDatasource);
                    #==== Got rid of "str" variable and just used a string literal - ','
                    outFile.write(';'.join(seq)+'\n')
            del mxd
outFile.close()
