#!/usr/bin/env python

'''
fin_ffmpeg.py - A module to turn a QT into a file sequence or a file sequence into a QT
Copyright (C) 2012  Miles Lauridsen

Based on BSD 2-Clause License  http://opensource.org/licenses/BSD-2-Clause

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
'''

import os
import sys
import subprocess

### DEFINITIONS

## MP4 files

def imgToMP4(file_in, file_out, fps='24', audioRate='192000', size='1280x720'):
    cmd = ['ffmpeg', '-f', 'image2', '-i', file_in, '-r', fps, '-b:v', '2500000', \
           '-refs', '5', '-weightp', '1', '-subq', '5', '-trellis', '0', '-s', \
           size, '-aq-strength', '2.0', '-8x8dct', '0', '-rc-lookahead', '10', \
           '-acodec', 'libfaac', '-b:a', audioRate, '-ar', '48000', file_out]
    return cmd

def onePassMp4(file_in, file_out, fps='24', audioRate='192000', scale='1280:720'):
    cmd = ['ffmpeg', '-f', 'image2', 'i', file_in, '-vf', 'scale='+ scale, \
           '-sws_flags', 'lanczos', '-vcodec', 'libx264', 'r', fps, '-preset', 'slow', \
           '-tune', 'film', '-y', '-an', '-crf', '22', \
           '-f', 'mp4', file_out]
    return cmd

def movToMP4(file_in, file_out, audioRate='192000', size='1280x720'):
    cmd = ['ffmpeg', '-i', file_in, '-b:v', '2500000', '-s', size, '-pix_fmt', 'yuv420p', \
           '-sws_flags', 'bicubic', '-refs', '5', '-weightp', '1', '-subq', '5', \
            '-trellis', '0', '-aq-strength', '2.0', '-8x8dct', '0', '-rc-lookahead', \
            '10', '-acodec', 'libfaac', '-b:a', audioRate, '-ar', '48000', file_out ]
    return cmd

def movToImg(file_in, file_out):
    cmd = ['ffmpeg', '-i', file_in, '-q:v', '2', file_out]
    return cmd
    
def movInfo(file_in):
    cmd = ['ffmpeg', 'i', file_in]
    return cmd

def files(path):
    files = os.listdir(path)
    return path, files

def fileOut(file, pad=None, ext=None):
    split = file.split('.')
    if pad == None:
        return split[0] + '.' + ext
    else:
        return split[0] + '.%0' + str(pad) + 'd.' + ext
    



### Image Magick convert sRGB tiff to DPX
# This gets close but slightly brighter and more saturated than converted to jpg
# Need to test color bars
#convert $image -gamma 0.47 -colorspace Log  ~/Desktop/fin_imagemagick_Log_v03.dpx

# ffmpeg -r 23.976 -i /Volumes/ARCHIVE_02/TRON/PRODUCTION/castleLogo/RENDERS/COMPS/TL_castleTron_outlinesStylize_v001c/TL_castleTron_outlinesStylize_v001c.%04d.tif -vcodec mjpeg -qscale 1 -s 480x270 ~/Desktop/test1800_23976_02.mov

### MOV to PNG
# ffmpeg -i /Volumes/PRODUCTION_01/ASSETS/footage/ACTION_MOVIE_ESSENTIALS_II/Action_Essentials_2K_D1-A/01_Atmospheres/Atmosphere_07.mov -q:v 2 /Volumes/PRODUCTION_01/ASSETS/footage/ACTION_MOVIE_ESSENTIALS_II/Action_Essentials_2K_D1-A/01_Atmospheres/Atmosphere_07/Atmosphere_07.%04d.png



### PRORES
# Profile 0 - apco, Profile 1 - apcs, Profile 2 - apcn, Profile 3 - apch
# ffmpeg -r 23.976 -i /Volumes/ARCHIVE_02/TRON/PRODUCTION/castleLogo/RENDERS/COMPS/TL_castleTron_outlinesStylize_v001c/TL_castleTron_outlinesStylize_v001c.%04d.tif -vcodec prores -profile 4 -s 1920x1080 -pix_fmt yuv422p10le ~/Desktop/fin_test_ffmpeg_prores_profile-4_1920x1080_23976_v01.mov


### MJPEG - Photo-JPEG

# ffmpeg -r 23.976 -i /Volumes/ARCHIVE_02/TRON/PRODUCTION/castleLogo/RENDERS/COMPS/TL_castleTron_outlinesStylize_v001c/TL_castleTron_outlinesStylize_v001c.%04d.tif -vcodec mjpeg -q:v 1 -s 960x540 -sws_flags bicubic -pix_fmt yuvj420p ~/Desktop/fin_test_ffmpeg_mjpeg_q-1_s-bicubic_960x540_23976_v01.mov

### mp4
# this one has good file size and decent image:
# ffmpeg -f image2 -i ~/Movies/TL_castleTron_outlinesStylize_v001c/TL_castleTron_outlinesStylize_v001c.%04d.tif -r 24 -acodec aac -b:a 192 -ar 22050 -b:v 2000000 -s 1280x720 -pix_fmt yuv420p -sws_flags bicubic -refs 5 -weightp 1 -subq 5 -trellis 0 -aq-strength 2.0 -8x8dct 0 -rc-lookahead 10 ~/Desktop/test16.mp4

#ffmpeg -i /Volumes/PRODUCTION_01/ASSETS/footage/ACTION_MOVIE_ESSENTIALS_II/Action_Essentials_2K_D1-A/01_Atmospheres/Atmosphere_07.mov -b:v 2500000 -s 1280x720 -pix_fmt yuv420p -sws_flags bicubic -refs 5 -weightp 1 -subq 5 -trellis 0 -aq-strength 2.0 -8x8dct 0 -rc-lookahead 10 -acodec aac -b:a 192 -ar 22050 /Volumes/PRODUCTION_01/ASSETS/footage/ACTION_MOVIE_ESSENTIALS_II/Action_Essentials_2K_D1-A/01_Atmospheres/Atmosphere_07.mp4

'''
Vimeo
ffmpeg -i /Volumes/PRODUCTION_01/PROJECTS/barefootGirl/editorial/publish/output/BH_Teaser_WhoByFire_v04_CC_001_v002_noDialog_pr422HQ.mov -i /Users/mileslauridsen/Dropbox/BG_Final_Audio/BarefootGirl_AudioBPFinesse_021913.aif -c copy -map 0:0 -map 1:0 -vcodec libx264 -b:v 20000k -s 1920x1080 -sws_flags bicubic -refs 5 -weightp 1 -subq 5 -trellis 0 -aq-strength 2.0 -8x8dct 0 -rc-lookahead 10 -acodec libfaac -b:a 320000 -ar 48000 ~/Desktop/BH_Teaser_WhoByFire_v04_CC_002_v003_dialog_1080_h264.mp4
'''