####This code is for removing rejected/uncategorized Raw images; images collected by EPU software
######if test on windowns, just double click the .py file
####cd curate exposure job
####python3 RemoveBadImages.py
####type 1 to remove rejected images; type 2 to remove uncategorized images. If you want to remove accepted images, type 96

import os, re, sys
def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))
            print(os.path.join(dir, f))
def find_and_delete_file(starting_directory, filename_to_delete):
    for root, dirs, files in os.walk(starting_directory):
        if filename_to_delete in files:
            file_path = os.path.join(root, filename_to_delete)
            print(f"Found file: {file_path}")
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting file: {e}")
            return True
    print(f"File '{filename_to_delete}' not found.")
    return False


print('Delete file type. 1:rejected. 2:manual_rejected. 96:accepted')
filetype = input() 
if filetype=='1':
    filename = './'+'0_exposures_rejected.cs'
elif filetype=='2':
    filename = './'+'0_exposures_manual_rejected.cs'
elif filetype=='96':
    filename = './'+'0_exposures_accepted.cs'
else:
    sys.exit(0)

file1 = open(filename, 'r', errors="ignore") #ignore weired text in the file
count = 0
DeleteFileCount = 0
print('Images Name Start: example, the date or FoilHole')
ImageNameStart = input() 
print('Images Name End: example, frames or fractions')
ImageNameEnd = input() 
print('Rawimage path: ')
ImagePath = input() 

while True:
    count += 1 
    # Get next line from file
    line = file1.readline()#read one line; if realines(), read all file
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    imageStartIndex = [i for i in range(len(line)) if line.startswith(ImageNameStart, i)]
    imageEndIndex = [i for i in range(len(line)) if line.startswith('.mrc', i)]
    #print("Line{}: {}".format(count, line.strip()))
    for i in range(len(imageStartIndex)):
        str = line[imageStartIndex[i]:imageEndIndex[i]]
        ennEnd = str.find(ImageNameEnd)+len(ImageNameEnd)
        ennStart = str.find(ImageNameStart)
        dirRemove = ImagePath
        removeName = str[ennStart:ennEnd]+'.tiff'
        find_and_delete_file(ImagePath, removeName)
        #os.remove(ImagePath+'/'+removeName)
        DeleteFileCount += 1
        #print(removeName) 
    #input()  #wait keyboard input, for debugging
 
file1.close()
print('Image Deleted:  ',DeleteFileCount)
#input()