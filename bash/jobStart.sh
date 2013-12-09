#!/bin/sh

#jobStart.sh - a job vfx workflow script that sets environment variables for the
#job, sequence, and shot that an artist inputs.
#Copyright (C) 2012  Miles Lauridsen
#
#Based on BSD 2-Clause License  http://opensource.org/licenses/BSD-2-Clause
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#Redistributions of source code must retain the above copyright notice,
#this list of conditions and the following disclaimer.
#Redistributions in binary form must reproduce the above copyright notice,
#this list of conditions and the following disclaimer in the documentation
#and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
#BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#POSSIBILITY OF SUCH DAMAGE.

if [ $1 ];
then
    if [ -d $JOB_SERVER/$1 ];
    then
        echo export JOB="$1";
        START_PATH="$JOB_SERVER/$1";
        
        # Run this no matter what
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
                    START_PATH="$JOB_SERVER/$1/$PROD_DIR/$2";
                else
                    echo export SEQUENCE="$2";
                fi
                
                # Run this no matter what
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