####This code is for removing rejected/uncategorized exposures in motion correct jobs
####cd curate exposure job
####python3 RemoveBadImages.py
####type 1 to remove rejected images; type 2 to remove uncategorized images. If you want to remove accepted images, type 96

import os, re, sys
def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))
            print(os.path.join(dir, f))

print('Delete file type. 1:rejected. 2:uncategorized. 96:accepted')
filetype = input() 
if filetype=='1':
    filename = './'+'0_exposures_rejected.cs'
elif filetype=='2':
    filename = './'+'0_exposures_uncategorized.cs'
elif filetype=='96':
    filename = './'+'0_exposures_accepted.cs'
else:
    sys.exit(0)

file1 = open(filename, 'r', errors="ignore") #ignore weired text in the file
count = 0
print('Motion Correct JobName: example J123')
JobName = input() 
while True:
    count += 1 
    # Get next line from file
    line = file1.readline()#read one line; if realines(), read all file
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    imageStartIndex = [i for i in range(len(line)) if line.startswith(JobName, i)]
    imageEndIndex = [i for i in range(len(line)) if line.startswith('.mrc', i)]
    #print("Line{}: {}".format(count, line.strip()))
    for i in range(len(imageStartIndex)):
        str = line[imageStartIndex[i]:imageEndIndex[i]]
        ennEnd = str.find('enn')
        dirEnd = str.find('ted/')
        dirRemove = '../'+str[0:dirEnd+4]
        removeName = str[dirEnd+5:ennEnd+3]
        purge(dirRemove, removeName)
        #print(dirRemove)
        #print(removeName) 
    #input()  #wait keyboard input, for debugging
 
file1.close()