#!/bin/sh

shopt -s expand_aliases

### Server Paths
LOCAL_SERVER="/Users/mileslauridsen/Dropbox/PRODUCTION"
LOCAL_JOB_SERVER="$LOCAL_SERVER/PROJECTS"
PROD_SERVER="/Volumes/PRODUCTION_01"
PROD_JOB_SERVER="$PROD_SERVER/PROJECTS"
LOCAL_SYSTEMS_SERVER="$LOCAL_SERVER/SYSTEMS"
PROD_SYSTEMS_SERVER="$PROD_SERVER/SYSTEMS"

### RSYNC Setups
RSYNC_TIMES_DRY="--recursive --times --verbose --ignore-existing --exclude-from=$SYSTEMS_SERVER/database/txt/exclude_list.txt --dry-run"
RSYNC_TIMES="--recursive --times --verbose --ignore-existing --progress --exclude-from=$SYSTEMS_SERVER/database/txt/exclude_list.txt"
alias rsynctimesdry='rsync $RSYNC_TIMES_DRY'
alias rsynctimes='rsync $RSYNC_TIMES --log-file=$SYSTEMS_SERVER/database/logs/rsync/rsync-log-"$(date +%Y-%m-%d_%H%M%S)".log'

### The rsync script
if [ $1 ];
then
    if [ -d $LOCAL_JOB_SERVER/$1 ];
    then
        if [ -d $PROD_JOB_SERVER/$1 ];
        then
            echo "Beginning Job Sync"
            echo " "
            echo "Syncing Job: "$1;
            rsynctimes $LOCAL_JOB_SERVER/$1/ $PROD_JOB_SERVER/$1/;
        else
            echo "Production Job Server not found"
        fi
    else
        echo "Local Job Server not found"

    fi
else
    echo "Please enter a job to sync"
fi
