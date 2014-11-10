### List any changes to the the installs here

# XCode for OS version
# https://developer.apple.com

# XCode Command Line for OS version
# https://developer.apple.com

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
brew install -v glib, gdk-pixbuf, pixman, harfbuzz, fontconfig, pango
brew install -v libyaml

# For TuttleOFX in the future
brew install -v libraw libcaca libxml2 nasm xz jpeg-turbo, ctl
brew install -v openjpeg tinyxml freeglut swig boost libpng
brew install -v opencolorio cfitsio hdf5 field3d glew

# Sys-Admin tools
brew install -v wireshark --with-qt --with-x --with-lua --devel
brew install duplicity

# Additional libraries
brew tap homebrew/science
brew install -v hdf5
brew install -v alembic
brew install -v opencv

# New way to install all ffmpeg options
brew install -v ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-frei0r --with-libass --with-libaca --with-libvo-aacenc --with-libvorbis --with-libvpx --with-openjpeg --with-openssl --with-schroedinger --with-speex --with-theora --with-tools 

# New way to install imagemagick with all options except: --with-x11
brew install -v imagemagick --with-fontconfig --with-jasper --with-quantum-depth-32 --with-liblqr --with-librsvg --with-libtiff --with-libwmf --with-little-cms --with-openexr --with-webp

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
sudo pip install dagobah
sudo pip install pysqlite
sudo pip install sqlalchemy
sudo pip install alembic
sudo pip install pyyaml

### Manual installs
mkdir ~/installs && cd ~/installs

# Komodo Edit
wget http://downloads.activestate.com/Komodo/releases/8.5.3/Komodo-Edit-8.5.3-14067-macosx-x86_64.dmg

# VLC
wget http://get.videolan.org/vlc/2.1.2/macosx/vlc-2.1.2.dmg

# Handbrake
wget http://handbrake.fr/rotation.php?file=HandBrake-0.9.9-MacOSX.6_GUI_x86_64.dmg

# True Crypt - manual download
# http://www.truecrypt.org/downloads

# Firefox
wget http://download-installer.cdn.mozilla.net/pub/firefox/releases/26.0/mac/en-US/Firefox%2026.0.dmg

# Celtx - manual download
# https://www.celtx.com/desktop.html

# Meshlab
wget http://sourceforge.net/projects/meshlab/files/meshlab/MeshLab%20v1.3.2/MeshLabMac_v132.dmg

# Adobe CC - manual download
# http://www.adobe.com/products/creativecloud.html

# Maya
# 2014
wget http://download.autodesk.com/us/maya/service_packs/Autodesk_Maya_2014_SP1_English_Japanese_SimplifiedChinese_MAC_OSX.dmg

# Nuke 7 - Requires Login and manual download
# http://www.thefoundry.co.uk/products/nuke-product-family/nuke/downloads/

# Nuke 8 - Requires Login and manual download
# http://www.thefoundry.co.uk/products/nuke-product-family/nuke/downloads/

# 3Delight - manual download
# http://www.3delight.com/en/index.php?page=3DSP_download

# DJViewer
wget http://sourceforge.net/projects/djv/files/djv-stable/0.9.0/djv-0.9.0_osx-x64.dmg

# Blender
wget http://mirror.cs.umn.edu/blender.org/release/Blender2.69/blender-2.69-OSX_10.6-x86_64.zip

# OpenOffice
wget http://sourceforge.net/projects/openofficeorg.mirror/files/4.0.1/binaries/en-US/Apache_OpenOffice_4.0.1_MacOS_x86_install_en-US.dmg

# Virtualbox
wget http://download.virtualbox.org/virtualbox/4.3.6/VirtualBox-4.3.6-91406-OSX.dmg
wget http://download.virtualbox.org/virtualbox/4.3.6/Oracle_VM_VirtualBox_Extension_Pack-4.3.6-91406.vbox-extpack

# Cuda
# osx 10.7 or 10.8
wget http://developer.download.nvidia.com/compute/cuda/5_5/rel/installers/cuda_5.5.20_mac_64.pkg
# osx 10.9
wget http://developer.download.nvidia.com/compute/cuda/5_5/rel/installers/cuda-mac-5.5.28_10.9_64.pkg

# Cyberduck
wget https://update.cyberduck.io/Cyberduck-4.4.3.zip

# XQuartz
http://xquartz.macosforge.org/downloads/SL/XQuartz-2.7.5.dmg

### finPipeline Maya files setup
cp $SYSTEMS_SERVER/maya/STARTUP/userSetup.py ~/Library/Preferences/Autodesk/maya/2014-x64/scripts/
cp $SYSTEMS_SERVER/maya/STARTUP/_user_files/Maya_mac.env ~/Library/Preferences/Autodesk/maya/2014-x64/

### OPTIONAL INSTALLS
# GoProStudio
# Wacom Utility
# Arduino
# Transmission
# Drobbox
# Audacity
