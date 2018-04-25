##### Constants ######
# NOTE: exempting GetDBDataNames.py from using this file because it needs to be run from ArcMap
# terminal. So any changes to this file that affect GetDBDataNames.py, need to be
# changed in that file itself, to keep consistency


### Inputs

#MXD_SOURCE_FOLDER = r"C:\Users\csmith1\LocalWorkSpace\ServerMxds"
MXD_SOURCE_FOLDER = r"\\wvmoap137\e$\temp\wvmoap_138_132"



### Outputs

# Change to the folder you want the output to be put in
outputFolder = "wvmoap_138_132_X_gis_gisp_OUTPUT"


MXD_OUTPUT = r"C:\WorkSpace\ReportDataSources\\" + outputFolder + "\\MxdSources.txt"

DB_DATA_OUTPUT = r"C:\WorkSpace\ReportDataSources\\" + outputFolder + "\\DatabaseFeatureClasses.txt"

DUPLICATES_OUTPUT = r"C:\WorkSpace\ReportDataSources\\" + outputFolder + "\\Duplicates.txt"

DB_USERNAME_OUTPUTS = r"C:\WorkSpace\ReportDataSources\\" + outputFolder + "\\DBUserNames.txt"

FINAL_OUTPUT_1 = r"C:\WorkSpace\ReportDataSources\\" + outputFolder + "\\finalOutput1.txt"

FINAL_OUTPUT_2 = r"C:\WorkSpace\ReportDataSources\\" + outputFolder + "\\finalOutput2.txt"

## Add outputs from comparison.py in here
