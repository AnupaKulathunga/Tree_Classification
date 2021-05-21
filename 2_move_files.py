import os
import shutil

srcpath = "samples"
destpath = "samples/Categories"

for root, subFolders, files in os.walk(srcpath):
    for file in files:
        subFolder = os.path.join(destpath,file[:2])
        if not os.path.isdir(subFolder):
            os.makedirs(subFolder)
        shutil.move(os.path.join(root, file), subFolder)

for n in range(1,10):
    os.chdir(
        r"D:\Machine learning\RS model\Git model\Tree_Classification\samples\Categories")
    try:
        os.rename(f"{n}_",f"{n}")
    except:
        continue