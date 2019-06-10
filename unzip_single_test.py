import gzip
import os

importDir = r"C:\\Users\\icprbadmin\\Documents\\Python_Scripts\\HEFS\\data\\"#"C:/Users/Public/Documents/Python Scripts/HEFS/data/"
tempDir = r"C:\\Users\\icprbadmin\\Documents\\Python_Scripts\\HEFS\\test\\"

files = []

for file in os.listdir(tempDir):
    files.append(file)
#print(files)        

my_file = files[5]

with gzip.open(tempDir+my_file, 'rb') as f:
    file_content = f.read()
    with open(importDir +my_file, 'wb') as g:
        #f.write(reader)
        g.write(file_content)

    #         import os
    # for file in os.listdir(tempDir):
    #     with gzip.open(tempDir+file, 'rb') as f:
    #         file_content = f.read()
    #         with open(importDir +file, 'wb') as g:
    #             g.write(file_content)