**RemoveBadImages.py** for cryosparc version 3.xx

**RemoveBadImages_v4.py** for cryosparc version 4.xx

#This code is for removing rejected/uncategorized exposures in motion correct jobs

#download and save RemoveBadImages.py anywhere you want

#go into your curate exposure folder

#run the code

#type 1 to remove rejected images; type 2 to remove uncategorized images. If you want to remove accepted images, type 96
#if you don't have rejected or uncatergorized images, it will show up errors, just ignore it.

#type the motion correct job name

#example

cd P4/J125  # your curate exposure folder

python3 path/RemoveBadImages.py   #the code path

1    #1, reject; 2, uncatergorized

J123   #motion correct job name

###############################################################################

**RemoveBadImages_v4_raw.py** for cryosparc version 4.xx to remove raw images (movies)

#example

cd P4/J125  # your curate exposure folder

python3 path/RemoveBadImages.py   #the code path

1    #1, reject; 2, manual rejected

24May16  #the initial common name of the images

/data/rawdata/24May16  #the path to the raw image folder

