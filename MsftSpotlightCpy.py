from os import listdir, mkdir, rename, getenv
from os.path import isfile, join, exists, getsize
from shutil import copy2

def main():
# Create a new folder in Win Picture Folder
    homepth = getenv('USERPROFILE')
    #print(homepth)
    spotlightdir = homepth+r'\Pictures\MsftSpotlightWallppr'
    if not exists(spotlightdir):
        mkdir(spotlightdir)
        print("Home directory %s was created." %spotlightdir)

# Get MSFT Spotlight Wallpaper files
# %USERPROFILE%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
    mypath = homepth+r'\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #print(onlyfiles)

# Check file size which is bigger than 100kb
    copyf = []
    for x in onlyfiles:
        #print(getsize(join(mypath, x)))
        if (int(getsize(join(mypath, x)) > 99999)):
            copyf.append(join(mypath, x))

# Copy them to Picture folder
    for j in copyf:
        #print(j)
        copy2(j, spotlightdir)

# Rename file to *.jpg
    for filename in listdir(spotlightdir):
       rename(join(spotlightdir,filename), join(spotlightdir, filename+'.jpg'))

if __name__ == '__main__':
    main()
