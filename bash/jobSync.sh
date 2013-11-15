#!/bin/sh

shopt -s expand_aliases

### RSYNC Setups
RSYNC_TIMES_DRY="--recursive --times --verbose --ignore-existing --exclude-from=$SYSTEMS_SERVER/database/txt/exclude_list.txt --dry-run"
RSYNC_TIMES="--recursive --times --verbose --ignore-existing --progress --exclude-from=$SYSTEMS_SERVER/database/txt/exclude_list.txt"
alias rsynctimesdry='rsync $RSYNC_TIMES_DRY'
alias rsynctimes='rsync $RSYNC_TIMES --log-file=$SYSTEMS_SERVER/database/logs/rsync/rsync-log-"$(date +%Y-%m-%d_%H%M%S)".log'


if [ $1 ];
then
    if [ -d $LOCAL_JOB_SERVER/$1 ];
    then
        echo "Beginning Job Sync"
        echo " "
        echo "Syncing Job: "$1;
        rsynctimes $LOCAL_JOB_SERVER/$1/ $PROD_JOB_SERVER/$1/;
    else
        echo "Local Job Server not found"

    fi
else
    echo "Please enter a job to sync"
fi

