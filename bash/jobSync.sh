#!/bin/sh

#jobSync.sh - For use in syncing a local >> production server workflow
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

shopt -s expand_aliases


if [ -f ~/.bashrc ];
then
    source ~/.bashrc
fi

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