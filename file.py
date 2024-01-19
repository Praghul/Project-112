import os
import shutil

source = "C:/Users/96659/Downloads"
destination = "C:/Users/96659/Desktop/File Organisation 1"
allfiles = os.listdir(source)
#print(allfiles)

for filename in allfiles:
    name,extension = os.path.splitext(filename)
    #print(name)
    #print(extension)

    list1 = [".jpeg", ".gif", ".png", "jpg", "jfif"]

    if extension == " ":
       continue
    if extension in list1:
        path1 = source + "/" + filename
        path2 = destination + "/" + "imagefiles"
        path3 = destination + "/" + "imagefiles" + filename
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
          shutil.move(path1,path3)
          print("Moving",filename)  
        else:
          os.mkdir(path2)
          shutil.move(path1,path3)
          print("Moving", filename)
    

    
