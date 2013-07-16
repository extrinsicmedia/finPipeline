### Start FFMBC dependencies
# Helpful instructions here: http://www.movieeditor.com/2012/01/26/building-ffmbcffmpeg-on-mac-os-x-lion/

# New way to install all ffmpeg options
brew install ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-frei0r --with-libass --with-libaca --with-libvo-aacenc --with-libvorbis --with-libvpx --with-openjpeg --with-openssl --with-schroedinger --with-speex --with-theora --with-tools 

# New way to install imagemagick with all options
brew install imagemagick --with-fontconfig --with-jasper --with-liblqr --with-librsvg --with-libtiff --with-libwmf --with-little-cms --with-openexr --with-quantum-depth-32 --with-webp --with-x11

## FFMBC dependencies - Some of these may be covered by new ffmpeg install
brew install frei0r libdc1394 dirac

wget https://ffmbc.googlecode.com/files/FFmbc-0.7-rc8.tar.bz2
tar -xvjf FFmbc-0.7-rc8.tar.bz2
cd FFmbc-0.7-rc8/
./configure --enable-gpl --enable-nonfree --enable-shared --enable-postproc --enable-runtime-cpudetect --enable-frei0r --enable-libdc1394 --enable-libdirac --enable-libfaac --enable-libmp3lame --enable-libopenjpeg --enable-libschroedinger --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-pthreads --enable-libxvid --enable-zlib



