from src import ListMapData
from src import FindDuplicates
from src import DBUserNames
from src import comparison



##### !!!!!IMPORTANT!!!! ######
# GetDBDataNames.py needs to be run in ArcMap Terminal before this file is run.



# List Map Data from Mxds
print("Listing Map Data")
ListMapData.run()
print("Complete")

# Finds Duplicates
print("Finding Duplicates") 
FindDuplicates.run()
print("Complete")

# Finds UserName data
print("Finding UserName Data") 
DBUserNames.run()
print("Complete")

# Does comparison
print("Comparing mxd data and DB data") 
comparison.run()
print("Complete")
