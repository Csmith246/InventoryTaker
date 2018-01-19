# This script needs to be run from the Python terminal in ArcMap. Couldn't get it
# running properly in a stand-alone script.
# This script makes a .txt file that lists the names of all the data
# in the specified database.

import os


arcpy.env.workspace = r"Database Connections\agsdev01_osd4.sde"#gis_osd4.sde"

output = r"C:\WorkSpace\ReportDataSources\testMxds\DatabaseFeatureClasses.txt"

# Accepts a list, file and counter. Writes all elements of list to file
def writeAll(listToWrite, f, cnt):
    for elem in listToWrite:
        # Write messages to a Text File
        f.write(elem + '\n')
        # Increment counter
        cnt[0] += 1

# Initialize counter and File
count = [0] # This is a list because pass by value
txtFile = open(output,"w")

# Get data then send to writeAll
featureClasses = arcpy.ListFeatureClasses() #SDE Feature Class
writeAll(featureClasses, txtFile, count)

dataSets = arcpy.ListDatasets() #SDE Raster Dataset and Catalog
writeAll(dataSets, txtFile, count)

tableList = arcpy.ListTables() # SDE Table
writeAll(tableList, txtFile, count)

# Note: SDE Relationship Class not listed


#close text file
txtFile.close()

print("Process Complete")
print(str(count[0]) + " items processed.")
