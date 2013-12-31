### List any changes to the the installs here

yum install http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
yum -y update
yum groupinstall -y development
yum install -y coreutils
yum install -y nano
yum install -v cmake libtool
yum install -y zlib-devel openssl-devel sqlite-devel bzip2-devel
yum install -y nasm libXp
yum install -y expat-devel gdbm-devel readline-devel screen
yum install -v xz-libs wget
yum install -v gnupg openssl
yum install -v ilmbase openexr openexr-devel openjpeg opencv opencv-devel
yum install -v qt qt-devel
yum install -v ffmpeg vlc
yum install -v gimp libreoffice
yum install -v kdebase-workspace kdeutils kdegraphics htop
yum install -y atlas atlas-devel blas blas-devel lapack lapack-devel
yum install -v numpy scipy python-matplotlib
yum install -v boost tbb scons
yum install -v ImageMagick

## Python 2.7.6 & 3.3.3
cd ~/Downloads
wget http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz
xz -d Python-2.7.6.tar.xz
tar -xvf Python-2.7.6.tar
cd Python-2.7.6
./configure --prefix=/usr/local
make
make altinstall

cd ~/Downloads
wget http://www.python.org/ftp/python/3.3.3/Python-3.3.3.tar.xz
xz -d Python-3.3.3.tar.xz
tar -xvf Python-3.3.3.tar
cd Python-3.3.3
./configure --prefix=/usr/local
make
make altinstall

echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc

## Setuptools
cd ~/Downloads
wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-2.0.1.tar.gz
tar -xvf setuptools-2.0.1.tar.gz
cd setuptools-2.0.1
python2.7 setup.py install

## PIP
cd ~/Downloads
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python2.7 get-pip.py

pip install virtualenv
pip install virtualenvwrapper
pip install numpy
pip install scipy
pip install scikit-learn
pip install ipython
pip install pyp
pip install cython
pip install scikit-image
pip install psutil

### Downloads

# 3Delight - manual download
# http://www.3delight.com/en/index.php?page=3DSP_download

# DJViewer - 0.9.0 seems to be missing files
rpm -ivh http://sourceforge.net/projects/djv/files/djv-stable/0.8.3%20Pre2/djv-0.8.3-pre2_linux-x64.rpm

# Nuke 7 - Requires Login and manual download
# http://www.thefoundry.co.uk/products/nuke-product-family/nuke/downloads/

# Nuke 8 - Requires Login and manual download
# http://www.thefoundry.co.uk/products/nuke-product-family/nuke/downloads/

# Maya
mkdir ~/installs/maya2014 && cd ~/installs/maya2014
wget http://download.autodesk.com/us/maya/service_packs/Autodesk_Maya_2014_SP1_English_Linux_64bit.tgz
tar xvzf Autodesk_Maya_2014_SP1_English_Linux_64bit.tgz
./setup

# Komodo Edit
cd ~/installs
wget http://downloads.activestate.com/Komodo/releases/8.5.3/Komodo-Edit-8.5.3-14067-linux-x86_64.tar.gz
tar xvzf Komodo-Edit-8.5.3-14067-linux-x86_64.tar.gz
cd Komodo-Edit-8.5.3-14067-linux-x86_64
./install.sh # change install directory to /usr/Komodo-Edit-8

### OPTIONAL

## Newest FFmpeg
# http://linuxsysconfig.com/2013/04/compile-latest-ffmpeg-and-vlc-on-centos-6/

yum install dbus-devel lua-devel zvbi
yum install libdvdread-devel libdc1394-devel libxcb-devel
yum install xcb-util-devel libxml2-devel mesa-libGLU-devel
yum install pulseaudio-libs-devel alsa-lib-devel libgcrypt-devel
yum install yasm libva-devel libass-devel libkate-devel
yum install libdvdnav-devel libcddb-devel libmodplug-devel
yum install a52dec-devel libmpeg2-devel

 
# Create the folder structure
# All source compilation will be performed in /opt/source.
# vlc will be install in /opt/vlc.
# The following command creates all required folders.

mkdir -p /opt/source/{ffmpeg,vlc} /opt/vlc

# x264
cd /opt/source/ffmpeg/
git clone git://git.videolan.org/x264
cd x264
./configure --enable-shared
make
make install

# libfdk_aac
cd /opt/source/ffmpeg/
git clone --depth 1 git://github.com/mstorsjo/fdk-aac.git
cd fdk-aac
autoreconf -fiv
./configure --enable-shared
make
make install

# lame
cd /opt/source/ffmpeg/
wget http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz
tar xzvf lame-3.99.5.tar.gz
cd lame-3.99.5
./configure --enable-shared --enable-nasm
make
make install

# libogg
cd /opt/source/ffmpeg/
wget http://downloads.xiph.org/releases/ogg/libogg-1.3.0.tar.gz
tar xzvf libogg-1.3.0.tar.gz
cd libogg-1.3.0
./configure --enable-shared
make
make install

# libtheora
cd /opt/source/ffmpeg/
wget http://downloads.xiph.org/releases/theora/libtheora-1.1.1.tar.gz
tar xzvf libtheora-1.1.1.tar.gz
cd libtheora-1.1.1
./configure --enable-shared
make
make install

# libvorbis
cd /opt/source/ffmpeg/
wget http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.3.tar.gz
tar xzvf libvorbis-1.3.3.tar.gz
cd libvorbis-1.3.3
./configure --enable-shared
make
make install

# libvpx
cd /opt/source/ffmpeg/
git clone http://git.chromium.org/webm/libvpx.git
cd libvpx
./configure --enable-shared
make
make install

# ffmpeg
cd /opt/source/ffmpeg/
git clone git://source.ffmpeg.org/ffmpeg
cd ffmpeg
./configure --enable-gpl --enable-libfdk_aac --enable-libmp3lame --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-nonfree --disable-static --enable-shared
make
make install