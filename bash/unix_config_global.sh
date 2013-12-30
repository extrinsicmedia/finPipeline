#!/bin/bash

### Shared Server and multiple use items. Change this based on FIN location
### local server
if [ `uname` == "Darwin" ]; then
    if [[ -d "/Users/mileslauridsen/Dropbox/PRODUCTION/" ]];
    then
            export LOCAL_SERVER="/Users/mileslauridsen/Dropbox/PRODUCTION"
            export LOCAL_SYSTEMS_SERVER="$LOCAL_SERVER/SYSTEMS"
            export LOCAL_JOB_SERVER="$LOCAL_SERVER/PROJECTS"
            export LOCAL_PYTHON_SERVER="$LOCAL_SYSTEMS_SERVER/python"
    fi
    
    ### production or shared server
    if [[ -d "/Volumes/PRODUCTION_01" ]];
        then
            export PROD_SERVER="/Volumes/PRODUCTION_01"
            export PROD_JOB_SERVER="$PROD_SERVER/PROJECTS"
            export PROD_SYSTEMS_SERVER="$PROD_SERVER/SYSTEMS"
            export PROD_PYTHON_SERVER="$PROD_SYSTEMS_SERVER/python"
    fi
fi

if [ `uname` == "Linux" ]; then
    if [[ -d "/Users/mileslauridsen/Dropbox/PRODUCTION/" ]];
    then
            export LOCAL_SERVER="/Users/mileslauridsen/Dropbox/PRODUCTION"
            export LOCAL_SYSTEMS_SERVER="$LOCAL_SERVER/SYSTEMS"
            export LOCAL_JOB_SERVER="$LOCAL_SERVER/PROJECTS"
            export LOCAL_PYTHON_SERVER="$LOCAL_SYSTEMS_SERVER/python"
    fi
    
    ### production or shared server
    if [[ -d "/Volumes/PRODUCTION_01" ]];
        then
            export PROD_SERVER="/Volumes/PRODUCTION_01"
            export PROD_JOB_SERVER="$PROD_SERVER/PROJECTS"
            export PROD_SYSTEMS_SERVER="$PROD_SERVER/SYSTEMS"
            export PROD_PYTHON_SERVER="$PROD_SYSTEMS_SERVER/python"
    fi
fi

if [ `uname` == "CYGWIN_NT-6.1" ]; then
    if [[ -d "/cygdrive/c/PRODUCTION" ]];
    then
            export LOCAL_SERVER="/cygdrive/c/PRODUCTION"
            export LOCAL_SYSTEMS_SERVER="$LOCAL_SERVER/SYSTEMS"
            export LOCAL_JOB_SERVER="$LOCAL_SERVER/PROJECTS"
            export LOCAL_PYTHON_SERVER="$LOCAL_SYSTEMS_SERVER/python"
    fi
    
    ### production or shared server
    if [[ -d "/Volumes/PRODUCTION_01" ]];
        then
            export PROD_SERVER="/Volumes/PRODUCTION_01"
            export PROD_JOB_SERVER="$PROD_SERVER/PROJECTS"
            export PROD_SYSTEMS_SERVER="$PROD_SERVER/SYSTEMS"
            export PROD_PYTHON_SERVER="$PROD_SYSTEMS_SERVER/python"
    fi
fi

#######################################################################
##### OSX USERS SHOULDN'T NEED TO ADJUST ANYTHING BELOW THIS LINE #####
#######################################################################

### set server to use, if only one server is used, set $LOCAL_SERVER above
if [[ $LOCAL_SERVER ]];
    then
        export SERVER="$LOCAL_SERVER"
    else
        export SERVER="$PROD_SERVER"
fi
        
### set default servers
export LOCAL_SYSTEMS_SERVER="$LOCAL_SERVER/SYSTEMS"
export PROD_SYSTEMS_SERVER="$PROD_SERVER/SYSTEMS"
export SYSTEMS_SERVER="$SERVER/SYSTEMS"

export LOCAL_JOB_SERVER="$LOCAL_SERVER/PROJECTS"
export PROD_JOB_SERVER="$PROD_SERVER/PROJECTS"
export JOB_SERVER="$SERVER/PROJECTS"

export LOCAL_DB_SERVER="$LOCAL_SYSTEMS_SERVER/database"
export PROD_DB_SERVER="$PROD_SYSTEMS_SERVER/database"
export DB_SERVER="$SYSTEMS_SERVER/database"

export CONFIG_DIR_NAME="config"
export CONFIG_FILE_NAME="config.sh"
export PROD_DIR="production"
export SEQ_NAME="sequences"

export LOCAL_TUTORIALS="$LOCAL_SERVER/ASSETS/tutorials"
export PROD_TUTORIALS="$PROD_SERVER/ASSETS/tutorials"

export RSYNC_EXCLUDE="$SYSTEMS_SERVER/database/txt/exclude_list.txt"

### misc stuff
export LOCAL_APP_LIBRARY="$LOCAL_SERVER/APPS"
export PROD_APP_LIBRARY="$PROD_SERVER/APPS"
export APP_LIBRARY="$SERVER/APPS"

export LOCAL_CHARTS="$LOCAL_SERVER/ASSETS/charts"
export PROD_CHARTS="$PROD_SERVER/ASSETS/charts"
export CHARTS="$SERVER/ASSETS/charts"

### RSYNC Setups
#alias
export RSYNC_TIMES_DRY="--recursive --times --verbose --ignore-existing --exclude-from=$SYSTEMS_SERVER/database/txt/exclude_list.txt --dry-run"
export RSYNC_TIMES="--recursive --times --verbose --ignore-existing --progress --exclude-from=$SYSTEMS_SERVER/database/txt/exclude_list.txt"
alias rsynctimesdry='rsync $RSYNC_TIMES_DRY'
alias rsynctimes='rsync $RSYNC_TIMES --log-file=$SYSTEMS_SERVER/database/logs/rsync/rsync-log-"$(date +%Y-%m-%d_%H%M%S)".log'

## Unix
PATH="$SYSTEMS_SERVER/bin/frametools:$MAYA_LOCATION/bin:$PATH"
alias makedate='mkdir $(date +%Y-%m-%d)'
alias makedatetime='mkdir $(date +%Y-%m-%d_%H%M%S)'

## Python - relying on a properly set PYTHONPATH in user's .bashrc
## Additonal libraries could be placed here, but THINK critically
## if that is the best idea
#export PYTHONPATH="$PYTHONPATH"

## Nuke
export NUKE_PATH="$SYSTEMS_SERVER/nuke"
export NUKE_STARTUP="$SYSTEMS_SERVER/nuke"

## Maya
export MAYA_SHARED_DIR="$SYSTEMS_SERVER/maya"
export MAYA_FIN_SCRIPT_PATH="$MAYA_SHARED_DIR/mel"
export MAYA_EXTERNAL_SCRIPT_PATH="$MAYA_SHARED_DIR/external/mel"
export MAYA_SCRIPT_PATH="$MAYA_FIN_SCRIPT_PATH:MAYA_EXTERNAL_SCRIPT_PATH"
export MAYA_FIN_PLUGIN_PATH="$MAYA_SHARED_DIR/plugins"
export MAYA_EXTERNAL_PLUGIN_PATH="$MAYA_SHARED_DIR/external/plugins"
export MAYA_PLUG_IN_PATH="$MAYA_FIN_PLUGIN_PATH:$MAYA_EXTERNAL_PLUGIN_PATH"
export MAYA_FIN_ICON_PATH="$MAYA_SHARED_DIR/icons"
export MAYA_EXTERNAL_ICON_PATH="$MAYA_SHARED_DIR/external/icons"
export XBMLANGPATH="$MAYA_FIN_ICON_PATH:$MAYA_EXTERNAL_ICON_PATH"
export MAYA_FIN_SHELF_PATH="$MAYA_SHARED_DIR/shelves"
export MAYA_EXTERNAL_SHELF_PATH="$MAYA_SHARED_DIR/external/shelves"
export MAYA_SHELF_PATH="$MAYA_FIN_SHELF_PATH:$MAYA_EXTERNAL_SHELF_PATH"
export MAYA_FIN_PYTHON_PATH="$MAYA_SHARED_DIR/python"
export MAYA_EXTERNAL_PYTHON_PATH="$MAYA_SHARED_DIR/external/python"
export MAYA_PYTHON_PATH="$MAYA_FIN_PYTHON_PATH:$MAYA_EXTERNAL_PYTHON_PATH"

# Dynamic shelf variables here so Maya.env doesn't need to be set
export MAYA_DYN_SHELF_NAME="finShelf"

## OCIO Default setup
export OCIO="$SYSTEMS_SERVER/ocio/spi-vfx/config.ocio"

### OSX Application paths ###
if [ `uname` == "Darwin" ]; then
    ### Apps
    #export BOOST_ROOT="/usr/local/Cellar/boost/1.49.0"
    alias truecrypt='/Applications/TrueCrypt.app/Contents/MacOS/TrueCrypt'
    alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'

    ### Application alias and ENV vars ###

    ## Firefox
    alias firefox='/Applications/Firefox.app/Contents/MacOS/firefox'

    ## Setup Amazon EC2 Command-Line Tools
    if [ -d ~/.ec2 ];
    then
        export EC2_HOME=~/.ec2
        export PATH=$PATH:$EC2_HOME/bin
        export EC2_PRIVATE_KEY=`ls $EC2_HOME/pk-*.pem`
        export EC2_CERT=`ls $EC2_HOME/cert-*.pem`
        export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Home/
    fi

    ## Djview Alias
    alias djview='/Applications/djv-0.9.0.app/Contents/MacOS/djv-0.9.0'
    alias djview-0.9.0='/Applications/djv-0.9.0.app/Contents/MacOS/djv-0.9.0'
    alias djview-0.8.3='/Applications/djv-0.8.3-pre2.app/Contents/MacOS/djv-0.8.3-pre2'
    export DJV_PATH='/Applications/djv-0.9.0.app/Contents/MacOS/djv-0.9.0'

    ## RV
    alias rv='/Applications/RV64.app/Contents/MacOS/RV64'
    alias rvpkg='/Applications/RV64.app/Contents/MacOS/rvpkg'

    ## Nuke
    alias nukex='/Applications/Nuke7.0v8/NukeX7.0v8.app/NukeX7.0v8'
    alias nuke='/Applications/Nuke7.0v8/Nuke7.0v8.app/Nuke7.0v8'
    alias nuke70v8='/Applications/Nuke7.0v8/Nuke7.0v8.app/Nuke7.0v8'

    export NUKE_PATH="$SYSTEMS_SERVER/nuke"
    export NUKE_STARTUP="$SYSTEMS_SERVER/nuke"

    ## Adobe Photoshop
    alias photoshop='/Applications/Adobe\ Photoshop\ CC/Adobe\ Photoshop\ CC.app/Contents/MacOS/Adobe\ Photoshop\ CC'
    
    ## Adobe After Effects
    alias ae='/Applications/Adobe\ After\ Effects\ CC/Adobe\ After\ Effects\ CC.app/Contents/MacOS/After\ Effects'

    ## Adobe Reader
    alias reader='/Applications/Adobe\ Reader.app/Contents/MacOS/AdobeReader'
    
    ## Maya
    alias maya='/Applications/Autodesk/maya2014/Maya.app/Contents/bin/maya'
    alias maya2014='/Applications/Autodesk/maya2014/Maya.app/Contents/bin/maya'
    export MAYA_LOCATION="/Applications/Autodesk/maya2014/Maya.app/Contents"
    
    # Add Maya bin folder to $PATH
    export PATH="/Applications/Autodesk/maya2014/Maya.app/Contents/bin:${PATH}"

    # Change this based on facility license settings
    #MAYA_LICENSE=unlimited; export MAYA_LICENSE
    #MAYA_LICENSE_METHOD=Network; export MAYA_LICENSE_METHOD
    #MAYA_ALT_EN=/var/flexlm/maya.lic; export MAYA_ALT_EN

    ## Komodo
    alias komodo='/Applications/Komodo\ Edit\ 8.app/Contents/MacOS/komodo'
fi

### Linux Application paths - 'Linux' may need to be 'Linux2' ###
if [ `uname` == "Linux" ]; then
    
    ### Application alias and ENV vars ###
    ## Misc Apps
    alias truecrypt='echo "set TrueCrypt path"'
    alias vlc='echo "set VLC path"'

    ## Firefox
    alias firefox='echo "set Firefox path"'

    ## Setup Amazon EC2 Command-Line Tools
    if [ -d ~/.ec2 ];
    then
        export EC2_HOME=~/.ec2
        export PATH=$PATH:$EC2_HOME/bin
        export EC2_PRIVATE_KEY=`ls $EC2_HOME/pk-*.pem`
        export EC2_CERT=`ls $EC2_HOME/cert-*.pem`
        export JAVA_HOME='echo "set JAVA_HOME path"'
    fi

    ## Djview Alias
    alias djview='echo "set DJView path"'
    alias djview-0.9.0='echo "set DJView path"'
    alias djview-0.8.3='echo "set DJView path"'
    export DJV_PATH='echo "set DJView path"'

    ## RV
    alias rv='echo "set RV path"'
    alias rvpkg='echo "set RVPkg path"'

    ## Nuke
    alias nukex='echo "set NukeX path"'
    alias nuke='echo "set Nuke path"'
    alias nuke70v8='echo "set Nuke 7.0v8 path"'
    
    ## Maya
    alias maya='echo "set Maya path"'
    alias maya2014='echo "set Maya 2014 path"'
    export MAYA_LOCATION='echo "set Maya Locations path"'
    
    # Add Maya bin folder to $PATH
    export PATH='echo "add Maya bin to $PATH: /usr/<path-to>/bin:${PATH}"'

    # Change this based on facility license settings
    #MAYA_LICENSE=unlimited; export MAYA_LICENSE
    #MAYA_LICENSE_METHOD=Network; export MAYA_LICENSE_METHOD
    #MAYA_ALT_EN=/var/flexlm/maya.lic; export MAYA_ALT_EN

    ## Komodo
    alias komodo='echo "set Komodo path"'
fi

if [ `uname` == "CYGWIN_NT-6.1" ]; then
    
    ### Application alias and ENV vars ###
    ## Misc Apps
    alias truecrypt='"/cygdrive/c/Program Files/TrueCrypt/TrueCrypt.exe"'
    alias vlc='"/cygdrive/c/Program Files (x86)/VideoLAN/VLC/vlc.exe"'

    ## Firefox
    alias firefox='"/cygdrive/c/Program Files (x86)/Mozilla Firefox/firefox.exe"'

    ## Setup Amazon EC2 Command-Line Tools
    if [ -d ~/.ec2 ];
    then
        export EC2_HOME=~/.ec2
        export PATH=$PATH:$EC2_HOME/bin
        export EC2_PRIVATE_KEY=`ls $EC2_HOME/pk-*.pem`
        export EC2_CERT=`ls $EC2_HOME/cert-*.pem`
        export JAVA_HOME='echo "set JAVA_HOME path"'
    fi

    ## Djview Alias
    alias djview='"/cygdrive/c/Program Files (x86)/djv 0.8.3/bin/djv_view.exe"'
    alias djview-0.8.3='"/cygdrive/c/Program Files (x86)/djv 0.8.3/bin/djv_view.exe"'
    export DJV_PATH='"/cygdrive/c/Program Files (x86)/djv 0.8.3/bin/djv_view.exe"'
    export PATH="$PATH:/cygdrive/c/Program Files (x86)/djv 0.8.3/bin"
    
    ## RV
    alias rv='echo "set RV path"'
    alias rvpkg='echo "set RVPkg path"'

    ## Nuke
    alias nukex='echo "set Nuke path"'
    alias nuke='"/cygdrive/c/Program Files/Nuke7.0v10/Nuke7.0.exe"'
    alias nuke70v10='"/cygdrive/c/Program Files/Nuke7.0v10/Nuke7.0.exe"'
    alias nuke80v1='"/cygdrive/c/Program Files/Nuke8.0v1/Nuke8.0.exe"'
    
    ## Blender
    alias blender='"/cygdrive/c/Program Files/Blender Foundation/Blender/blender.exe"'
    
    ## Maya
    alias maya='"/cygdrive/c/Program Files/Autodesk/Maya2014/bin/maya.exe"'
    alias maya2014='"/cygdrive/c/Program Files/Autodesk/Maya2014/bin/maya.exe"'
    export MAYA_LOCATION="/cygdrive/c/Program Files/Autodesk/Maya2014/bin"
    
    # Add Maya bin folder to $PATH
    export PATH="$MAYA_LOCATION:$PATH"

    # Change this based on facility license settings
    #MAYA_LICENSE=unlimited; export MAYA_LICENSE
    #MAYA_LICENSE_METHOD=Network; export MAYA_LICENSE_METHOD
    #MAYA_ALT_EN=/var/flexlm/maya.lic; export MAYA_ALT_EN
    
    ## Meshlab
    alias meshlab='"/cygdrive/c/Program Files/VCG/MeshLab/meshlab.exe"'
    alias meshlabserver='"/cygdrive/c/Program Files/VCG/MeshLab/meshlabserver.exe"'
    
    ## Komodo
    alias komodo='"/cygdrive/c/Program Files (x86)/ActiveState Komodo Edit 8/komodo.exe"'
fi

### jobStart tool function
jobStart () {
    if [ -n $3 ]; then
        eval "$($SYSTEMS_SERVER/bash/jobStart.sh $1 $2 $3)"
    elif [ -n $2 ]; then
        eval "$($SYSTEMS_SERVER/bash/jobStart.sh $1 $2)"
    elif [ -n $1 ]; then
        eval "$($SYSTEMS_SERVER/bash/jobStart.sh $1)"
    else
        echo "Please enter a job name"
    fi
}

# jobSync
alias jobsync='$SYSTEMS_SERVER/bash/jobSync.sh'
