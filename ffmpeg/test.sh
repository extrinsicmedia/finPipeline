#!/bin/sh

if [ $1 ];
then
    if [ -f $1 ];
    then
        if [ $2 ];
        then
            # mp4 1 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
            #ffmpeg -i $1 -vf scale=768:432 -vcodec libx264 -preset slow -tune film -y -an -crf 22 test01.m4v

            # mp4 2 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
            ffmpeg -i $1 -vf scale=768:432 -pass 1 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -y -an -b:v 1000k -bufsize 2000k -f rawvideo /dev/null && ffmpeg -i $1 -vf scale=768:432 -pass 2 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -y -an -b:v 1000k -bufsize 2000k -f mp4 $2
        else
            echo "Please enter an output name with *.m4v"
    fi
    else
        echo "Please enter a movie file path"
fi
