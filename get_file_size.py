import os

print("# GET THE FILE SIZE FROM ANY FILE!")
files = os.listdir()
print(files)
question = input("Filename: ")

def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = (fileobject.tell(), "bytes")
    return size

file = open(question, 'rb')
print(getSize(file))
