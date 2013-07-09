#!/bin/sh

# mp4 1 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
ffmpeg -i “input.mov” -vf scale=768:432 -vcodec libx264 -preset slow -tune film -y -an -crf 22 temp.m4v

# mp4 2 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
ffmpeg -i some_file_in.mp4 -vf scale=768:432 -pass 1 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -y -an -b:v 1000k -bufsize 2000k -f rawvideo NUL && ffmpeg -i some_file_in.mp4 -vf scale=768:432 -pass 2 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -y -an -b:v 1000k -bufsize 2000k -f mp4 some_file_out.m4v