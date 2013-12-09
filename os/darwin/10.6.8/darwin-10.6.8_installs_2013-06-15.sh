# New way to install all ffmpeg options
brew install -v ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-frei0r --with-libass --with-libaca --with-libvo-aacenc --with-libvorbis --with-libvpx --with-openjpeg --with-openssl --with-schroedinger --with-speex --with-theora --with-tools 

# New way to install imagemagick with all options
brew install -v imagemagick --with-fontconfig --with-jasper --with-liblqr --with-librsvg --with-libtiff --with-libwmf --with-little-cms --with-openexr --with-quantum-depth-32 --with-webp --with-x11

### Start FFMBC install
# Helpful instructions here: http://www.movieeditor.com/2012/01/26/building-ffmbcffmpeg-on-mac-os-x-lion/
# FFMBC dependencies - Some of these may be covered by new ffmpeg install
brew install -v frei0r libdc1394 dirac

wget https://ffmbc.googlecode.com/files/FFmbc-0.7-rc8.tar.bz2
tar -xvjf FFmbc-0.7-rc8.tar.bz2
cd FFmbc-0.7-rc8/
./configure --enable-gpl --enable-nonfree --enable-shared --enable-postproc --enable-runtime-cpudetect --enable-frei0r --enable-libdc1394 --enable-libdirac --enable-libfaac --enable-libmp3lame --enable-libopenjpeg --enable-libschroedinger --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-pthreads --enable-libxvid --enable-zlib


# Install qt, python, python3, pyqt, boost, cmake, hdf5, ilmbase, openexr, alembic, htop
brew install -v qt
brew install -v python
brew install -v python3
brew install -v pyqt
brew install -v boost
brew install -v cmake
brew install -v hdf5
brew install -v ilmbase
brew install -v openexr
brew install -v alembic
brew install -v htop

# Update python3 setuptools and pip
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade pip
