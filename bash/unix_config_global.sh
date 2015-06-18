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
        
        ## Set backup server path
        BACKUP_SERVER_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value backup_server_path)"
        if [[ -d $BACKUP_SERVER_PATH ]];
            then
                export BACKUP_SERVER=$BACKUP_SERVER_PATH
        fi
        
        ## Set project directory template path
        PROJECT_DIR_TEMPLATE="$(cat $HOME/finpipeline.yaml | shyaml get-value project_dir_template)"
        if [[ -d $PROJECT_DIR_TEMPLATE ]];
            then
                export PROJECT_DIR_TEMPLATE=$PROJECT_DIR_TEMPLATE
        fi

        ## Set reference/img path
        REF_IMG_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value reference_img_path)"
        if [[ -d $REF_IMG_PATH ]];
            then
                export REF_IMG_PATH=$REF_IMG_PATH
        fi

        ## Set reference/vid path
        REF_VID_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value reference_vid_path)"
        if [[ -d $REF_VID_PATH ]];
            then
                export REF_VID_PATH=$REF_VID_PATH
        fi
        
        ## Set verarypt app path
        VERACRYPT_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value veracrypt_app)"
        if [[ -f $VERACRYPT_APP ]];
            then
                alias veracrypt=$VERACRYPT_APP
                unset VERACRYPT_APP
        fi
        
        ## Set vlc app path
        VLC_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value vlc_app)"
        if [[ -f $VLC_APP ]];
            then
                alias vlc=$VLC_APP
                unset VLC_APP
        fi
        
        ## Set firefox app path
        FIREFOX_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value firefox_app)"
        if [[ -f $FIREFOX_APP ]];
            then
                alias firefox=$FIREFOX_APP
                unset FIREFOX_APP
        fi
        
        ## Set djview app path
        DJVIEW_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value djview_app)"
        if [[ -f $DJVIEW_APP ]];
            then
                alias djview=$DJVIEW_APP
                export DJV_PATH=$DJVIEW_APP
                alias djvload='djview $(djv_ls -xi)'
                unset DJVIEW_APP
        fi
        
        ## Set djview bin path
        DJV_BIN_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value djv_bin_path)"
        if [[ -d $DJV_BIN_PATH ]];
            then
                export PATH="$PATH:$DJV_BIN_PATH"
                unset DJV_BIN_PATH
        fi
        
        ## Set bview app path
        BVIEW_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value bview_app)"
        if [[ -f $BVIEW_APP ]];
            then
                alias bview=$BVIEW_APP
                export BVIEW_PATH=$BVIEW_APP
                unset BVIEW_APP
        fi
        
        ## Set batch_bview app path
        BATCH_BVIEW_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value batch_bview_app)"
        if [[ -f $BATCH_BVIEW_APP ]];
            then
                alias batch_bview=$BATCH_BVIEW_APP
                export BATCH_BVIEW_PATH=$BATCH_BVIEW_APP
                unset BATCH_BVIEW_APP
        fi
        
        ## Set rv app path
        RV_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value rv_app)"
        if [[ -f $RV_APP ]];
            then
                alias rv=$RV_APP
                unset RV_APP
        fi
        
        ## Set rvpkg app path
        RVPKG_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value rvpkg_app)"
        if [[ -f $RVPKG_APP ]];
            then
                alias rvpkg=$RVPKG_APP
                unset RVPKG_APP
        fi
        
        ## Set nuke app path
        NUKE_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value nuke_app)"
        if [[ -f $NUKE_APP ]];
            then
                alias nuke=$NUKE_APP
                unset NUKE_APP
        fi
        
        ## Set nukex app path
        NUKEX_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value nukex_app)"
        if [[ -f $NUKEX_APP ]];
            then
                alias nukex=$NUKEX_APP
                unset NUKEX_APP
        fi
        
        ## Set nukestudio app path
        NUKESTUDIO_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value nukestudio_app)"
        if [[ -f $NUKESTUDIO_APP ]];
            then
                alias nukestudio=$NUKESTUDIO_APP
                unset NUKESTUDIO_APP
        fi
        
        ## Set photoshop app path
        PHOTOSHOP_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value photoshop_app)"
        if [[ -f $PHOTOSHOP_APP ]];
            then
                alias photoshop=$PHOTOSHOP_APP
                unset PHOTOSHOP_APP
        fi
        
        ## Set aftereffects app path
        AFTEREFFECTS_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value aftereffects_app)"
        if [[ -f $AFTEREFFECTS_APP ]];
            then
                alias aftereffects=$AFTEREFFECTS_APP
                unset AFTEREFFECTS_APP
        fi
        
        ## Set maya app path
        MAYA_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value maya_app)"
        if [[ -f $MAYA_APP ]];
            then
                alias maya=$MAYA_APP
                unset MAYA_APP
        fi
        
        ## Set maya bin path
        MAYA_BIN_PATH="$(cat $HOME/finpipeline.yaml | shyaml get-value maya_bin_path)"
        if [[ -f $MAYA_BIN_PATH ]];
            then
                export PATH="$PATH:$MAYA_BIN_PATH"
                unset MAYA_BIN_PATH
        fi
        
        ## Set meshlab app path
        MESHLAB_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value meshlab_app)"
        if [[ -f $MESHLAB_APP ]];
            then
                alias meshlab=$MESHLAB_APP
                unset MESHLAB_APP
        fi
        
        ## Set komodo app path
        KOMODO_APP="$(cat $HOME/finpipeline.yaml | shyaml get-value komodo_app)"
        if [[ -f $KOMODO_APP ]];
            then
                alias komodo="\"$KOMODO_APP"\"
                unset KOMODO_APP
        fi
fi

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
