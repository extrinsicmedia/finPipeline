#!/bin/bash

### Check OS and set paths accordingly based on that info ###

UNAME=`uname`

### Shared Server and multiple use items. Change this based on FIN location
## Make a linux version here

if [ "$UNAME" == "Darwin" ]; then
    ### mobile servers
    if [[ -d "/Users/mileslauridsen/FIN_Google_Drive/PRODUCTION/" ]];
    then
            # Stupid whitespace in Google Drive Path so using * to pass the "Google\ Drive" portion of the path
            export MOBILE_SERVER="/Users/mileslauridsen/FIN_Google_Drive/PRODUCTION";export MOBILE_SERVER
            export MOBILE_SYSTEMS_SERVER="$MOBILE_SERVER/SYSTEMS";export MOBILE_SYSTEMS_SERVER
            export MOBILE_JOB_SERVER="$MOBILE_SERVER/PROJECTS";export MOBILE_JOB_SERVER
            export MOBILE_PYTHON_SERVER="$MOBILE_SYSTEMS_SERVER/python";export MOBILE_PYTHON_SERVER
    fi
    
    ### home job servers
    if [[ -d "/Volumes/PRODUCTION_01" ]];
        then
            export HOME_SERVER="/Volumes/PRODUCTION_01";export HOME_SERVER
            export HOME_JOB_SERVER="$HOME_SERVER/PROJECTS";export HOME_JOB_SERVER
            export HOME_SYSTEMS_SERVER="$HOME_SERVER/SYSTEMS";export HOME_SYSTEMS_SERVER
            export HOME_PYTHON_SERVER="$HOME_SYSTEMS_SERVER/python";export HOME_PYTHON_SERVER
    fi
    
    ### set server to use
    if [[ $HOME_SERVER ]];
        then
            ### Taking this out for now for dev
            ###export SERVER="$HOME_SERVER";export SERVER
            export SERVER="$MOBILE_SERVER";export SERVER
        else
            export SERVER="$MOBILE_SERVER";export SERVER
    fi
            
    ### set default servers
    export SYSTEMS_SERVER="$SERVER/SYSTEMS";export SYSTEMS_SERVER
    export JOB_SERVER="$SERVER/PROJECTS";export JOB_SERVER
    export PYTHON_SERVER="$SYSTEMS_SERVER/python";export PYTHON_SERVER
    export DB_SERVER="$SYSTEMS_SERVER/db";export DB_SERVER
    export PROD_DIR="production";export PROD_DIR
    export SEQ_DIR="sequences";export SEQ_DIR
    export SHOTS_DIR="shots";export SHOTS_DIR
    
    ### misc stuff
    export APP_LIBRARY="$SERVER/APPS";export APP_LIBRARY
    export UNIX_LIBRARY="$APP_LIBRARY/unix";export UNIX_LIBRARY
    #export MYSQL_SERVER="10.0.1.8";export MYSQL_SERVER
    export CHARTS="$SERVER/CHARTS";export CHARTS
fi

## Unix
if [ "$UNAME" == "Darwin" ]; then
    PATH="$PATH:$SYSTEMS_SERVER/bin/frametools:$MAYA_LOCATION/bin"; export PATH
    export BOOST_ROOT="/usr/local/Cellar/boost/1.49.0";export BOOST_ROOT
fi

### Application alias and ENV vars ###

## Firefox
if [ "$UNAME" == "Darwin" ]; then
    alias firefox='/Applications/Firefox.app/Contents/MacOS/firefox'
fi

## Setup Amazon EC2 Command-Line Tools
export EC2_HOME=~/.ec2
export PATH=$PATH:$EC2_HOME/bin
export EC2_PRIVATE_KEY=`ls $EC2_HOME/pk-*.pem`
export EC2_CERT=`ls $EC2_HOME/cert-*.pem`
export JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Home/

## Djview Alias http://djv.sourceforge.net/
if [ "$UNAME" == "Darwin" ]; then
    alias djview='/Applications/djv-0.9.0.app/Contents/MacOS/djv-0.9.0'
    alias djview-0.9.0='/Applications/djv-0.9.0.app/Contents/MacOS/djv-0.9.0'
    alias djview-0.8.3='/Applications/djv-0.8.3-pre2.app/Contents/MacOS/djv-0.8.3-pre2'
    export DJV_PATH='/Applications/djv-0.9.0.app/Contents/MacOS/djv-0.9.0'
    
fi
# Need to add Linux directory to djview

## RV
if [ "$UNAME" == "Darwin" ]; then
    alias rv='/Applications/RV64.app/Contents/MacOS/RV64'
    alias rvpkg='/Applications/RV64.app/Contents/MacOS/rvpkg'
    export RVRC_CONFIG="1"
fi

## Nuke
if [ "$UNAME" == "Darwin" ]; then
    alias nukex='/Applications/Nuke7.0v8/NukeX7.0v8.app/NukeX7.0v8'
    alias nuke='/Applications/Nuke7.0v8/Nuke7.0v8.app/Nuke7.0v8'
    alias nuke70v8='/Applications/Nuke7.0v8/Nuke7.0v8.app/Nuke7.0v8'
    alias nuke63v8='/Applications/Nuke6.3v8/Nuke6.3v8.app/Nuke6.3v8'
    alias nukex63v8='/Applications/Nuke6.3v8/NukeX6.3v8.app/NukeX6.3v8'
    alias nukex62v2='/Applications/Nuke6.2v2/NukeX6.2v2.app/NukeX6.2v2'
    alias nuke62v2='/Applications/Nuke6.2v2/Nuke6.2v2.app/Nuke6.2v2'
    alias nukex61v3='/Applications/Nuke6.1v3/NukeX6.1v3.app/NukeX6.1v3'
    alias nuke61v3='/Applications/Nuke6.1v3/Nuke6.1v3.app/Nuke6.1v3'
fi

export NUKE_PATH="$SYSTEMS_SERVER/nuke/STARTUP";export NUKE_PATH


## After Effects
if [ "$UNAME" == "Darwin" ]; then
    alias aecs3='/Applications/Adobe\ After\ Effects\ CS3/Adobe\ After\ Effects\ CS3.app/Contents/MacOS/After\ Effects'
    alias aecs4='/Applications/Adobe\ After\ Effects\ CS4/Adobe\ After\ Effects\ CS4.app/Contents/MacOS/After\ Effects'
    alias aecs5='/Applications/Adobe\ After\ Effects\ CS5/Adobe\ After\ Effects\ CS5.app/Contents/MacOS/After\ Effects'
    alias aecs6='/Applications/Adobe\ After\ Effects\ CS6/Adobe\ After\ Effects\ CS6.app/Contents/MacOS/After\ Effects'
    alias ae='/Applications/Adobe\ After\ Effects\ CS6/Adobe\ After\ Effects\ CS6.app/Contents/MacOS/After\ Effects'
fi


## Maya
if [ "$UNAME" == "Darwin" ]; then
    alias maya='/Applications/Autodesk/maya2013.5/Maya.app/Contents/bin/maya'
    alias maya2013='/Applications/Autodesk/maya2013.5/Maya.app/Contents/bin/maya'
    alias maya2012='/Applications/Autodesk/maya2012/Maya.app/Contents/bin/maya'
    alias maya2011='/Applications/Autodesk/maya2011/Maya.app/Contents/MacOS/Maya'
    alias maya2010='/Applications/Autodesk/maya2010/Maya.app/Contents/MacOS/Maya'
    alias mayapy='/Applications/Autodesk/maya2013.5/Maya.app/Contents/bin/mayapy'
    alias mayapy2013='/Applications/Autodesk/maya2013.5/Maya.app/Contents/bin/mayapy'
    alias mayapy2012='/Applications/Autodesk/maya2012/Maya.app/Contents/bin/mayapy'
    export MAYA_LOCATION='/Applications/Autodesk/maya2013.5/Maya.app/Contents';export MAYA_LOCATION
    #export MAYA_SHARED_DIR='$SYSTEMS_SERVER/maya';export MAYA_SHARED_DIR
    
fi

# Change this based on facility license settings
#MAYA_LICENSE=unlimited; export MAYA_LICENSE
#MAYA_LICENSE_METHOD=Network; export MAYA_LICENSE_METHOD
#MAYA_ALT_EN=/var/flexlm/maya.lic; export MAYA_ALT_EN

#export PYMEL_PATH="$MAYA_SHARED_DIR/python/pymel-1.0.3";export PYMEL_PATH
#export MAYA_SCRIPT_PATH="$MAYA_SHARED_DIR/SCRIPTS:$MAYA_SHARED_DIR/SCRIPTS/mel";export MAYA_SCRIPT_PATH
#export MAYA_PLUG_IN_PATH="$MAYA_SHARED_DIR/PLUGINS";export MAYA_PLUG_IN_PATH
#export XBMLANGPATH="$MAYA_SHARED_DIR/SCRIPTS/icons";export XBMLANGPATH
#export MAYA_ICON_PATH="$MAYA_SHARED_DIR/SCRIPTS/icons";export MAYA_ICON_PATH
#export MAYA_PYTHON_PATH="$MAYA_SHARED_DIR/SCRIPTS/python";export MAYA_PYTHON_PATH

## Houdini
if [ "$UNAME" == "Darwin" ]; then
    alias houdini11='/Applications/Houdini\ 11.0.581/Houdini.app/Contents/MacOS/houdini'
fi

## Komodo
if [ "$UNAME" == "Darwin" ]; then
    alias komodo='/Applications/Komodo\ Edit.app/Contents/MacOS/komodo'
fi

## Python
# Setting PATH for Python 2.7
PATH="/usr/local/bin/:${PATH}" export PATH

if [ "$UNAME" == "Darwin" ]; then
    PYTHONPATH="$PYTHON_SERVER:/usr/local/lib/python2.7/site-packages";export PYTHONPATH
    ## Took the following line out for now
    # $MAYA_SHARED_DIR/SCRIPTS/python:$MAYA_SHARED_DIR/SCRIPTS/python/pymel-1.0.3:
fi

### Default Alias Settings
alias ll="ls -l"
alias la="ls -a"
