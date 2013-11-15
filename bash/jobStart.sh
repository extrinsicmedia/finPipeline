#!/bin/sh

if [ $1 ];
then
    if [ -d $JOB_SERVER/$1 ];
    then
        echo export JOB="$1";
        START_PATH="$JOB_SERVER/$1";
        if [ -f $JOB_SERVER/$1/$CONFIG_DIR_NAME/$CONFIG_FILE_NAME ];
        then
            eval $JOB_SERVER/$1/$CONFIG_DIR_NAME/$CONFIG_FILE_NAME;
        fi
        
        if [ $2 ];
        then
            if [ -d $JOB_SERVER/$1/$PROD_DIR/$2 ];
            then
                if [ -z $3 ]; then
                    echo export SHOT="$2";
                else
                    echo export SEQUENCE="$2";
                fi
                START_PATH="$JOB_SERVER/$1/$PROD_DIR/$2";
                if [ -f $JOB_SERVER/$1/$PROD_DIR/$2/$CONFIG_DIR_NAME/$CONFIG_FILE_NAME ];
                then
                    eval $JOB_SERVER/$1/$PROD_DIR/$2/$CONFIG_DIR_NAME/$CONFIG_FILE_NAME;
                fi
                
                if [ $3 ];
                then
                    if [ -d $JOB_SERVER/$1/$PROD_DIR/$2/$3 ];
                    then
                        echo export SHOT="$3";
                        START_PATH="$JOB_SERVER/$1/$PROD_DIR/$2/$3";
                        if [ -f $JOB_SERVER/$1/$PROD_DIR/$2/$3/$CONFIG_DIR_NAME/$CONFIG_FILE_NAME ];
                        then
                            eval $JOB_SERVER/$1/$PROD_DIR/$2/$3/$CONFIG_DIR_NAME/$CONFIG_FILE_NAME;
                        fi
                    fi
                fi
            fi
        fi
    else
        echo $JOB_SERVER/$1 "is not a path";
    fi
fi

echo cd $START_PATH
