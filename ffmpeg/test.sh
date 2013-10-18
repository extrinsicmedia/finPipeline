#!/bin/sh

if [ $1 ];
then
    if [ -f $1 ];
    then
        if [ $2 ];
        then
            # mp4 1 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
            ffmpeg -i $1 -vcodec libx264 -preset slow -tune film -q:v 9 -y -an -crf 22 $2_1pass.m4v

            # mp4 2 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
            ffmpeg -i $1 -pass 1 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -q:v 9 -y -an -b:v 1000k -bufsize 2000k -f rawvideo /dev/null && ffmpeg -i $1 -pass 2 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -q:v 9 -y -an -b:v 1000k -bufsize 2000k -f mp4 $2_2pass.m4v

            # prores 0, 4:2:2
            ffmpeg -i $1 -vcodec prores_kostya -profile:v 0 -q:v 9 -y -an -crf 22 $2_prores0.mov
        
            # prores 1
            ffmpeg -i $1 -vcodec prores_kostya -profile:v 1 -q:v 9 -y -an -crf 22 $2_prores1.mov

            # prores 2
            ffmpeg -i $1 -vcodec prores_kostya -profile:v 2 -q:v 9 -y -an -crf 22 $2_prores2.mov

            # prores 3
            ffmpeg -i $1 -vcodec prores_kostya -profile:v 3 -q:v 9 -y -an -crf 22 $2_prores3.mov

            # Motion jpeg
            ffmpeg -i $1 -vf scale=1920:1080 -vcodec mjpeg -qscale 1 -tune film -q:v 9 -y -an -crf 22 $2_mjpeg.mov

            # DNXHD 36M
            ffmpeg -i $1 -vf scale=1920:1080 -vcodec dnxhd -b 36M -tune film -q:v 9 -y -an -crf 22 $2_dnxhd36M.mov

            # DNXHD 115M
            ffmpeg -i $1 -vf scale=1920:1080 -vcodec dnxhd -b 115M -tune film -q:v 9 -y -an -crf 22 $2_dnxhd115M.mov
        fi
    fi
fi
