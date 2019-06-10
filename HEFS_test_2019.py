#from suds.client import Client
from traceback import format_exc
import sys
#import FEWSConnect
import logging
from paramiko import Transport
from paramiko import SFTPClient

#import gzip

if (__name__ == '__main__'):
    host = "data7.erh.noaa.gov"
    port = 22 #after much testing....port 22 is the place to be
    usr = "cschultz"
    pw = "Shenandoah22"
    path = "/hefs_icprb/"#r"/Distribution/RHA-Data/rhapub5/hefs_icprb"
    lookback = 5


    importDir = r"C:\\Users\\icprbadmin\\Documents\\Python_Scripts\\HEFS\\data\\"#"C:/Users/Public/Documents/Python Scripts/HEFS/data/"
    #file_name ="/SFTP_TEST"
    extension = ".xml" #.gz?

    #1
    try:
        transport = Transport((host, port))
        transport.connect(username = usr, password = pw)
        sftp = SFTPClient.from_transport(transport)
        print("1 it's alive...sftp object up and running")
    except:
        print("1 failed to connect")

    #2
    try:
        # Retrieve list of files from sftp site
        s=sftp.listdir(path)
        print("2 These are the files in " + host + path + ": ")
        print("currently not showing")
        #print(s)
    except:
        print("2 no good retrieving file list")

   
    #3
    try:
        hrsback = int(lookback)*24
        # List of files in directory variable s
        allfiles=[filename for filename in s if filename.endswith('.xml.gz')][-hrsback:]
        #print('3' + allfiles)
        print("3 found files")
    except:
        print("3 no good finding file")

    #4
    try:   
        for file in allfiles:
            reader = sftp.open(path+file,'rb').read()
            #with gzip.open(file, 'rb') as f:
                #reader = f.read()
            #print(pdf)
        print("4 read successful")
    except:
        print("4 no good on read from file")

    # for file in allfiles:
    #         #reader = sftp.open(path+file,'rb').read()
    #         with gzip.open(file, 'rb') as f:
    #             reader = f.read()
    
    #5
    try:
        for file in allfiles:
    #        Store file in FEWS import Directory
            with open(importDir +file, 'wb') as f:
                f.write(reader)
        print("5 files saved to " + importDir)# +file)
    except:
        print("5 no good on file save attempt 1")
        #print(pdf)

    # for file in allfiles:
    #     reader = sftp.open(path+file,'rb').read()

    # for file in allfiles:
    # #        Store file in FEWS import Directory
    #     with open(importDir+file, 'wb') as f:
    #         f.write(reader)
    
    

    #unzip files
    #6
    # try:
    #     import zipfile
    #     import gunzip


    #     for file in allfiles:
    #         with gunzip(file)
    #     print("files unzipped")
    # except:
    #     print("no good on unzip")

        #7
    try:
        sftp.close()
        print("6 closed sftp object")
    except:
        print("6 sftp did not close")
    # 8
    try:
        f.close()#importDir.close()
        print("7 closed importDir object")
    except:
        print("7 importDir did not close")