### This script organizes info about the UserName used to get data from the DB
from Constants import *

def getUserNameData():
    # Open file with .mxds data
    mxdsDataPath = MXD_OUTPUT
    mxdsData = open(mxdsDataPath, 'r')

    firstLine = mxdsData.readline() # get special 1st csv line
    firstLine = firstLine.replace('\n','')
    headers = firstLine.split(';')
    userNameIndex = headers.index("DB User")

    collector = {}

    for line in mxdsData:
        line = line.replace('\n','')
        splitLine = line.split(';')
        userName = splitLine[userNameIndex]

        try:
            collector[userName] += 1
        except:
            collector[userName] = 1

    #print(collector)

    # Close mxdsData
    mxdsData.close()

    userNameDataPath = DB_USERNAME_OUTPUTS
    userData = open(userNameDataPath, 'w+')

    userData.write("UserName;TimesUsed\n")

    for key, value in collector.items():
        data = (key, str(value))
        userData.write(";".join(data)+'\n')

    userData.close()


def run():
    getUserNameData()