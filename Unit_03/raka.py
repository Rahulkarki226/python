import os
path=os.path.dirname(__file__)
path=path+'/'
def getsize(fp):
    filesize= os.path.getsize(fp)
    print("Total size of file:",filesize)

fp=path+"abc.txt"
getsize(fp)

