#!/bin/bash
clear
echo "******************************START**********************************"
date
echo "******************************START**********************************"


##Path of the Dropbox folder where new blogs are uploaded
DROPBOXPATH="/home/kitab-admin/Dropbox/website/blogs/"
#cd $DROPBOXPATH
#pwd

## do not run the ocr pipeline if there are no new files in the dropbox:
#dropbox_ls=$(ls)
#if [[ -z "$dropbox_ls" ]]; then
#    echo "no new files in Dropbox. Exiting."
#    echo "*****************************END***********************************"
#    date
#    echo "*****************************END***********************************"
#    echo " "
#    exit 1
#fi

## Path of the Dropbox folder where new header data is uploaded
DROPBOXPATHHEAD="/home/kitab-admin/Dropbox/website/headers/" 


# Path of the folder where python script is located
ROOTPATH="/mnt/RAID/website/kitab-project-org.github.io/conversion_script"
cd $ROOTPATH
pwd

# Activate the virtual environment for converter !!Need to set up venv!!:
echo 'ACTIVATING CONDA' 
pwd

CONDA_PATH=$(conda info | grep -i 'base environment' | awk '{print $4}')
#source $CONDA_PATH/etc/profile.d/conda.sh
#echo $CONDA_PATH
source /home/kitab-admin/.pyenv/versions/anaconda3-5.1.0/etc/profile.d/conda.sh
conda activate kraken
pwd

# Update fork with recent changes to repo (in case there are any) !!NEED TO SET UP ACCESS TOKEN!!
echo "UPDATING BRANCH FROM MAIN WEBSITE BEFORE UPLOAD OF NEW BLOGS"

GitHubPAT=$(<GitHub_personalAccessTokenReadOnly.txt)

git remote add upstream https://github.com/kitab-project-org/kitab-project-org.github.io.git
git fetch upstream
git checkout main
git merge upstream/main

echo "GETTING FILES FROM DROPBOX  ..."

# First copy across files from blogs folder

echo "CONTENTS OF DROPBOXPATH BlOGS BEFORE MOVING FILES:"
ls $DROPBOXPATH/

for f in ${DROPBOXPATH}*
do
    if [[ $f =~ " - " ]]; then
        echo "  RENAMING $f"
        echo "  >>>$DROPBOXPATH${f#$DROPBOXPATH* - }"

        mv "$f" "$DROPBOXPATH${f#$DROPBOXPATH* - }"

        f="$DROPBOXPATH${f#$DROPBOXPATH* - }"
    fi

    echo "  COPYING $DROPBOXPATH${f#/home/kitab-admin/Dropbox/website/blogs/}"
    echo "  >>>${ROOTPATH}/input/blogs"

    cp -r "$DROPBOXPATH${f#$DROPBOXPATH}" "${ROOTPATH}/input/blogs/"

    echo "  REMOVING file from Dropbox"
    echo "  $f"
    rm -rf $f



    echo "  -----"
done

echo "CONTENTS OF DROPBOXPATH AFTER MOVING FILES:"
ls $DROPBOXPATH/
echo ""

echo "CONTENTS OF ROOTPATH/INPUT_FILES AFTER MOVING FILES:"
ls $ROOTPATH/INPUT_FILES/
echo ""

# Second copy across files from headers folder

echo "CONTENTS OF DROPBOXPATH HEADERS BEFORE MOVING FILES:"
ls $DROPBOXPATHHEAD/

for f in ${DROPBOXPATHHEAD}*
do
    if [[ $f =~ " - " ]]; then
        echo "  RENAMING $f"
        echo "  >>>$DROPBOXPATHHEAD${f#$DROPBOXPATHHEAD* - }"

        mv "$f" "$DROPBOXPATHHEAD${f#$DROPBOXPATHHEAD* - }"

        f="$DROPBOXPATHHEAD${f#$DROPBOXPATHHEAD* - }"
    fi

    echo "  COPYING $DROPBOXPATHHEAD${f#/home/kitab-admin/Dropbox/website/headers/}"
    echo "  >>>${ROOTPATH}/input/headers"

    cp -r "$DROPBOXPATHHEAD${f#$DROPBOXPATHHEAD}" "${ROOTPATH}/input/headers/"

    echo "  REMOVING file from Dropbox"
    echo "  $f"
    rm -rf $f



    echo "  -----"
done

echo "CONTENTS OF DROPBOXPATH HEADERS AFTER MOVING FILES:"
ls $DROPBOXPATHHEAD/
echo ""

echo "CONTENTS OF ROOTPATH/INPUT_FILES AFTER MOVING FILES:"
ls $ROOTPATH/input/headers
echo ""

echo "----------------------------------------------------------------------------"

echo "START THE CONVERSION SCRIPT:"

## !!Change for necessary venv!!
CONDA_PATH=$(conda info | grep -i 'base environment' | awk '{print $4}')
#echo $CONDA_PATH
#source $CONDA_PATH/etc/profile.d/conda.sh
source /home/kitab-admin/.pyenv/versions/anaconda3-5.1.0/etc/profile.d/conda.sh
conda activate kraken

python3 docx_converter.py

echo "----------------------------------------------------------------------------"

# Commit changes to the branch

echo "Committing changes to repo ..."
git add .
git commit -m 'output generated' 
git push 
## CHANGE THIS TO FORK 
https://kitab-project:$GitHubPAT@github.com/OpenITI/ocr_with_kraken main


echo "*****************************END***********************************"
date
echo "*****************************END***********************************"
echo " "

