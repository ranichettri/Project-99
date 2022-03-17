import shutil
import os 
path= input("Enter the folder to be sorted:-")
print("We will delet files/folder when they are older than ")
time= int(input("Enter the no. of day:-"))* 24 * 60 * 60
print(time)
#f:\WhiteHat\cl99.2\cl99

if os.path.exists(path):
    File = os.listdir(path)
    #print("this is it:-",File)
    for i in File:
        path2=os.path.join(path+'/'+i)
        #print(path2)
        ctime = os.stat(path2).st_ctime
        print(ctime)
        if ctime != time:
            os.remove(path2)
        else:
           continue
else:
    print("check the folder you gave and try again")
