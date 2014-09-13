#!/bin/bash

### If users are not working local/remote, only set the
### $PROD_SERVER settings.

## Check for config file and set servers
if [[ -f "$HOME/finpipeline.yaml" ]];
then
        # Set local server
        LOCAL_SERVER_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value local_server_path)"
        if [[ -d $LOCAL_SERVER_PATH ]];
            then
                export LOCAL_SERVER=$LOCAL_SERVER_PATH
                export LOCAL_SYSTEMS_SERVER="$LOCAL_SERVER/SYSTEMS"
                export LOCAL_JOB_SERVER="$LOCAL_SERVER/PROJECTS"
                export LOCAL_PYTHON_SERVER="$LOCAL_SYSTEMS_SERVER/python"
        fi
        
        ## Set production or shared server
        PROD_SERVER_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value prod_server_path)"
        if [[ -d $PROD_SERVER_PATH ]];
            then
                export PROD_SERVER=$PROD_SERVER_PATH
                export PROD_JOB_SERVER="$PROD_SERVER/PROJECTS"
                export PROD_SYSTEMS_SERVER="$PROD_SERVER/SYSTEMS"
                export PROD_PYTHON_SERVER="$PROD_SYSTEMS_SERVER/python"
        fi
        
        ## Set Dropbox path
        DROPBOX_SERVER_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value dropbox_path)"
        if [[ -d $DROPBOX_SERVER_PATH ]];
            then
                export DROPBOX_PATH=$DROPBOX_SERVER_PATH
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

## User Home directory backups
alias cpuserinfo='$SYSTEMS_SERVER/bash/cpUserInfo.sh'

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
if [[ `uname` == "Darwin" ]]; then
    
    ## Truecrypt
    alias truecrypt='/Applications/TrueCrypt.app/Contents/MacOS/TrueCrypt'
    
    ## VLC
    alias vlc='/Applications/VLC.app/Contents/MacOS/VLC'

    ## Firefox
    alias firefox='/Applications/Firefox.app/Contents/MacOS/firefox'

    ## Setup Amazon EC2 Command-Line Tools
    if [[ -d ~/.ec2 ]];
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
    export PATH="$PATH:/Applications/djv-0.9.0.app/Contents/Resources/bin"
    alias djvload='djview $(djv_ls -xi)'
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
    export PATH="/Applications/Autodesk/maya2014/Maya.app/Contents/bin:$PATH"

    # Change this based on facility license settings
    #MAYA_LICENSE=unlimited; export MAYA_LICENSE
    #MAYA_LICENSE_METHOD=Network; export MAYA_LICENSE_METHOD
    #MAYA_ALT_EN=/var/flexlm/maya.lic; export MAYA_ALT_EN
    
    ## Meshlab
    alias meshlab='/Applications/meshlab.app/Contents/MacOS/meshlab'
    alias meshlabserver='/Applications/meshlab.app/Contents/MacOS/meshlabserver'
    
    ## Komodo
    alias komodo='/Applications/Komodo\ Edit\ 8.app/Contents/MacOS/komodo'
fi

### Linux Application paths - 'Linux' may need to be 'Linux2' ###
if [[ `uname` == "Linux" ]]; then
    
    ### Application alias and ENV vars ###
    ## Misc Apps
    alias truecrypt='/usr/bin/truecrypt'
    alias vlc='/usr/bin/vlc'

    ## Firefox
    alias firefox='/usr/bin/firefox'

    ## Setup Amazon EC2 Command-Line Tools
    if [[ -d ~/.ec2 ]];
    then
        export EC2_HOME=~/.ec2
        export PATH=$PATH:$EC2_HOME/bin
        export EC2_PRIVATE_KEY=`ls $EC2_HOME/pk-*.pem`
        export EC2_CERT=`ls $EC2_HOME/cert-*.pem`
        export JAVA_HOME='echo "set JAVA_HOME path"'
    fi

    ## Djview Alias
    alias djview='/usr/local/djv/bin/djv_view'
    alias djview-0.8.3='/usr/local/djv/bin/djv_view'
    alias djvload='djview $(djv_ls -xi)'
    export DJV_PATH="/usr/local/djv/bin"
    export PATH="/usr/local/djv/bin:$PATH"

    ## RV
    alias rv='echo "set RV path"'
    alias rvpkg='echo "set RVPkg path"'

    ## Nuke
    alias nukex='/usr/local/Nuke7.0v10/Nuke7.0 --nukex -V'
    alias nuke='/usr/local/Nuke7.0v10/Nuke7.0 -V'
    alias nuke70v10='/usr/local/Nuke7.0v10/Nuke7.0 -V'
    export PATH="/usr/local/Nuke7.0v10:$PATH"
    
    ## Maya
    alias maya='/usr/autodesk/maya2014-x64/bin/maya2014'
    alias maya2014='/usr/autodesk/maya2014-x64/bin/maya2014'
    export MAYA_LOCATION='/usr/autodesk/maya2014-x64/bin'
    
    # Add Maya bin folder to $PATH
    export PATH="/usr/autodesk/maya2014-x64/bin:$PATH"

    # Change this based on facility license settings
    #MAYA_LICENSE=unlimited; export MAYA_LICENSE
    #MAYA_LICENSE_METHOD=Network; export MAYA_LICENSE_METHOD
    #MAYA_ALT_EN=/var/flexlm/maya.lic; export MAYA_ALT_EN

    ## Komodo
    alias komodo='/usr/Komodo-Edit-8/bin/komodo'
    export PATH="/usr/Komodo-Edit-8/bin:$PATH"
fi

if [[ `uname` == "CYGWIN_NT-6.1" ]]; then
    
    ### Application alias and ENV vars ###
    ## Misc Apps
    alias truecrypt='"/cygdrive/c/Program Files/TrueCrypt/TrueCrypt.exe"'
    alias vlc='"/cygdrive/c/Program Files (x86)/VideoLAN/VLC/vlc.exe"'

    ## Firefox
    alias firefox='"/cygdrive/c/Program Files (x86)/Mozilla Firefox/firefox.exe"'

    ## Setup Amazon EC2 Command-Line Tools
    if [[ -d ~/.ec2 ]];
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
    if [[ -n $3 ]]; then
        eval "$($SYSTEMS_SERVER/bash/jobStart.sh $1 $2 $3)"
    elif [[ -n $2 ]]; then
        eval "$($SYSTEMS_SERVER/bash/jobStart.sh $1 $2)"
    elif [[ -n $1 ]]; then
        eval "$($SYSTEMS_SERVER/bash/jobStart.sh $1)"
    else
        echo "Please enter a job name"
    fi
}

# jobSync
alias jobsync='$SYSTEMS_SERVER/bash/jobSync.sh'
