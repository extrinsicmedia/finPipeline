#!/bin/sh

### $1 is input file sequence NOT FILE, $2 is output directory
if [ $1 ];
then
    # Check for output path
    if [ $2 ];
    then
        # mp4 1 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vcodec libx264 -preset slow -tune film -q:v 9 -y -an -crf 22 -s 1920x1080 -r 23.976 $2/test_1pass_$(date +%Y-%m-%d_%H%M%S).m4v
        
        # mp4 2 pass encoding from http://transcoding.wordpress.com/2012/06/17/optimal-h-264-encoding-for-flash-and-html5/
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -pass 1 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -q:v 9 -y -an -b:v 1000k -bufsize 2000k -r 23.976 -s 1920x1080 -f rawvideo /dev/null && ffmpeg -i $1 -pass 2 -sws_flags lanczos -vcodec libx264 -preset slow -tune film -q:v 9 -y -an -b:v 1000k -bufsize 2000k -r 23.976 -s 1920x1080 -f mp4 $2/test_2pass_$(date +%Y-%m-%d_%H%M%S).m4v
        
        # mp4 v2
        #
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -c:v libx264 -profile:v main -g 1 -tune stillimage -crf 9 -bf 0 -vendor ap10 -pix_fmt yuv420p -s 1920x1080 -r 23.976 $2/test_1pass_v2_$(date +%Y-%m-%d_%H%M%S).m4v
        
        # prores 0, 4:2:2
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vcodec prores_kostya -profile:v 0 -q:v 9 -y -an -crf 22 -r 23.976 -s 1920x1080 $2/test_prores0_$(date +%Y-%m-%d_%H%M%S).mov
        
        # prores 0 v2, 4:2:2
        # file sequence input: -f image2
        # example from: https://trac.ffmpeg.org/wiki/vfxEncodingGuide
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -c:v prores_kostya -profile:v 0 -qscale:v 11 -vendor ap10 -pix_fmt yuv422p10le -s 1920x1080 -r 23.976 $2/test_prores0_v2_$(date +%Y-%m-%d_%H%M%S).mov
        
        # prores 1
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vcodec prores_kostya -profile:v 1 -q:v 9 -y -an -crf 22 -r 23.976 -s 1920x1080 $2/test_prores1_$(date +%Y-%m-%d_%H%M%S).mov
        
        # prores 1 v2
        # file sequence input: -f image2
        # example from: https://trac.ffmpeg.org/wiki/vfxEncodingGuide
        ffmpeg -y -probesize 5000000 -r 23.976 -force_fps -i $1 -c:v prores_kostya -profile:v 1 -qscale:v 11 -vendor ap10 -pix_fmt yuv422p10le -s 1920x1080 -r 23.976 $2/test_prores1_v2_$(date +%Y-%m-%d_%H%M%S).mov
        
        # prores 2
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vcodec prores_kostya -profile:v 2 -q:v 9 -y -an -crf 22 -r 23.976 -s 1920x1080 $2/test_prores2_$(date +%Y-%m-%d_%H%M%S).mov
        
        # prores 2 v2
        # file sequence input: -f image2
        # example from: https://trac.ffmpeg.org/wiki/vfxEncodingGuide
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -c:v prores_kostya -profile:v 2 -qscale:v 11 -vendor ap10 -pix_fmt yuv422p10le -s 1920x1080 -r 23.976 $2/test_prores2_v2_$(date +%Y-%m-%d_%H%M%S).mov
        
        # prores 3
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vcodec prores_kostya -profile:v 3 -q:v 9 -y -an -crf 22 -r 23.976 -s 1920x1080 $2/test_prores3_$(date +%Y-%m-%d_%H%M%S).mov
        
        # prores 3 v2
        # file sequence input: -f image2
        # example from: https://trac.ffmpeg.org/wiki/vfxEncodingGuide
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -c:v prores_kostya -profile:v 3 -qscale:v 11 -vendor ap10 -pix_fmt yuv422p10le -s 1920x1080 -r 23.976 $2/test_prores3_v2_$(date +%Y-%m-%d_%H%M%S).mov
        
        # Photo jpeg
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vf scale=1920:1080 -vcodec mjpeg -qscale:v 1 -tune film -q:v 9 -y -an -crf 22 -r 23.976 -s 1920x1080 $2/test_mjpeg_$(date +%Y-%m-%d_%H%M%S).mov
        
        # Photo jpeg v2
        # example from: https://trac.ffmpeg.org/wiki/vfxEncodingGuide
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -c:v mjpeg -qscale:v 1 -vendor ap10 -pix_fmt yuvj422p -s 1920x1080 -r 23.976 $2/test_mjpeg_v2_$(date +%Y-%m-%d_%H%M%S).mov

        # DNXHD 36M
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vcodec dnxhd -b:v 36M -vendor ap10 -pix_fmt yuv422p -s 1920x1080 -r 23.976 -tune film -q:v 9 -y -an -crf 22 $2/test_dnxhd36M_$(date +%Y-%m-%d_%H%M%S).mov
        
        # DNXHD 115M
        ffmpeg -y -probesize 5000000 -f image2 -r 23.976 -force_fps -i $1 -vcodec dnxhd -b:v 115M -vendor ap10 -pix_fmt yuv422p -s 1920x1080 -r 23.976 -tune film -q:v 9 -y -an -crf 22 $2/test_dnxhd115M_$(date +%Y-%m-%d_%H%M%S).mov
    fi
fi