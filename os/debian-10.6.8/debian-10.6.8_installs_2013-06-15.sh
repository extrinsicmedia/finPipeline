### Start FFMBC dependencies
# Helpful instructions here: http://www.movieeditor.com/2012/01/26/building-ffmbcffmpeg-on-mac-os-x-lion/

brew install frei0r libdc1394 dirac schroedinger

wget https://ffmbc.googlecode.com/files/FFmbc-0.7-rc8.tar.bz2
tar -xvjf FFmbc-0.7-rc8.tar.bz2
cd FFmbc-0.7-rc8/
./configure --enable-gpl --enable-nonfree --enable-shared --enable-postproc --enable-runtime-cpudetect --enable-frei0r --enable-libdc1394 --enable-libdirac --enable-libfaac --enable-libmp3lame --enable-libopenjpeg --enable-libschroedinger --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-pthreads --enable-libxvid --enable-zlib
