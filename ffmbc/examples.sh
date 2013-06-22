#!/bin/sh

# Examples for ffmbc QT creation should go here.  Later we can wrap these into python calls for auto-generation.

### PRORES
ffmpeg -i input.mov -vcodec prores -profile NUMBER -an output.mov

# For different flavors of ProRes replace NUMBER with a number from zero to 3 where:
# 0 : ProRes422 (Proxy)
# 1 : ProRes422 (LT)
# 2 : ProRes422 (Normal)
# 3 : ProRes422 (HQ)
#
# OR use one of the following shorthands to select your profile:
#
# -profile NAME
# proxy
# lt
# std
# hq
#
# The following was taken from FFmbc’s wiki site:
#
# The encoder behave differently based on 3 options:
# -qscale < value > or -cqp < value >
# Specify a fixed quantizer that will be used for every frame. This is a VBR encoding method.
#
# If bitrate is not specified, the bitrate will be automatically chosen based on video resolution and will be similar to the reference encoder for the same profile.
# -b < bitrate >
# Specify a approximately constant bit rate to use during encoding.
# 444 encoding: add -pix_fmt yuv444p10 to your commandline options.
#
# Update: ProRes 444 doesn’t seem to work, but people are working on a patch as learned from this thread:
# http://ffmpeg.org/pipermail/ffmpeg-user/2012-September/009521.html
# I must admit I haven’t used the codec lately, but people write that Final Cut Pro
# often gives the warning that ProRes files made with FFmpeg, are not optimized
# for FCP. All that means is, that the file wasn’t compressed using FCP while as
# the file should work fine.