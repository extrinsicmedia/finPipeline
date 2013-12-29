### List any changes to the the installs here

## Manual installs
# Komodo Edit
# VLC
# Handbrake
# True Crypt
# Backblaze
# XCode
# XCode Command Line
# Firefox
# Celtx
# Meshlab
# Adobe CC
# Maya
# Nuke
# 3Delight
# Celtx
# djv
# GoProStudio
# Meshlab
# Wacom Utility
# Blender
# Arduino
# OpenOffice
# Virtualbox
# Cuda
# Cyberduck
# Transmission
# Drobbox
# Audacity
# XQuartz


# Install Homebrew and then install these
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

brew install -v cmake
brew install -v gnupg --8192
brew install -v pass
brew install -v keychain
brew install -v openssl
brew install -v python --universal --with-brewed-openssl
brew install -v ilmbase
brew install -v openexr
brew install -v git
brew install -v wget
brew install -v qt --universal --with-docs --with-mysql
brew install -v pyqt
brew install -v pyside --with-python3
brew install -v htop
brew install -v opencolorio --with-docs --with-java --with-python --with-tests
brew install -v boost --universal 
brew install -v python3 --quicktest --with-brewed-openssl
brew install -v doxygen
brew install -v vim
brew install -v colordiff
brew install -v gfortran
brew install -v tbb
brew install -v scons
brew install -v fltk
brew install -v pixie
brew install -v open-scene-graph --docs --with-collada-dom --with-ffmpeg --with-gnuplot --with-openexr
brew install -v unrar
brew install -v coreutils

brew tap homebrew/science
brew install -v hdf5
brew install -v alembic

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

# Update python3 setuptools and pip
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade pip

sudo pip install virtualenv
sudo pip install virtualenvwrapper
sudo pip install numpy
sudo pip install scipy
sudo pip install scikit-learn
sudo pip install pyp
sudo pip install cython
sudo pip install scikit-image
sudo pip install OpenEXR
sudo pip install psutil

# Maya files setup
cp $SYSTEMS_SERVER/maya/STARTUP/userSetup.py ~/Library/Preferences/Autodesk/maya/2014-x64/scripts/
cp $SYSTEMS_SERVER/maya/STARTUP/_user_files/Maya_mac.env ~/Library/Preferences/Autodesk/maya/2014-x64/


# Possibly need to delete these:
cp lib/libopenctm.dylib /usr/local/opt/
cp lib/openctm.h /usr/local/include/
cp lib/openctmpp.h /usr/local/include/
cp tools/ctmconv /usr/local/bin/
cp tools/ctmviewer /usr/local/bin/
mkdir -p /usr/local/share/man/man1/
cp doc/ctmconv.1 /usr/local/share/man/man1/
cp doc/ctmviewer.1 /usr/local/share/man/man1/
