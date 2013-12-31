### Installs

## Install Cygwin before continuing
# Cygwin :: http://cygwin.com/setup-x86.exe
# Here is a minimal list of packages for Cygwin setup
# autoconf automake binutils cmake gcc-g++ git libgfortran3
# make python python-imaging python-ming python-numpy
# python-openssl python-paramiko python-pyqt4 python-setuptools
# python-sip python-twisted scons curl
# fontconfig clamav gnupg hdf5 makepasswd wget openldap openldap-devel
# openssh openssl rsync whois exif gnuplot ImageMagick jasper jpeg lcms
# lcms2 python-lcms tiff libpng15 libpng-devel sqlite3 flac flac-devel
# libogg0 libkate1 libkate-devel libogg0 libogg-devel pulseaudio libpulse-devel
# libvorbis libvorbis-devel vorbis-tools speex

## Cygwin Ports
# Follow instructions here:
# https://sourceware.org/cygwinports/
# yasm libSDL-devel libfaac-devel libaacplus-devel libgsm-devel
# libmp3lame-devel libschroedinger1.0-devel speex-devel
# libtheora-devel libxvidcore-devel pkg-config
# ffmpeg vlc openexr ImageMagick

### The following downloads and installs should be run in a Cygwin shell
mkdir ~/installs && cd ~/installs

# VLC 32bit and 64bit
wget http://get.videolan.org/vlc/2.1.2/win32/vlc-2.1.2-win32.exe
wget http://download.videolan.org/pub/videolan/vlc/last/win64/vlc-2.1.2-win64.exe

# Meshlab 64bit
wget http://sourceforge.net/projects/meshlab/files/meshlab/MeshLab%20v1.3.2/MeshLab_v132_64bit.exe/download

# Komodo Edit
wget http://downloads.activestate.com/Komodo/releases/8.5.3/Komodo-Edit-8.5.3-14067.msi

# Nuke 7 - Requires Login and manual download
# http://www.thefoundry.co.uk/products/nuke-product-family/nuke/downloads/

# Nuke 8 - Requires Login and manual download
# http://www.thefoundry.co.uk/products/nuke-product-family/nuke/downloads/

# Python 2.7 32bit and 64bit
wget http://www.python.org/ftp/python/2.7/python-2.7.msi
wget http://www.python.org/ftp/python/2.7/python-2.7.amd64.msi

# Setuptools
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python

# PIP
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python ./get-pip.py

# Still having issues with gcc linking on pip installs
# Probably related to MinGW
pip install virtualenv
pip install virtualenvwrapper

# Virtualbox - Install virtualbox and extension pack
wget http://download.virtualbox.org/virtualbox/4.3.6/VirtualBox-4.3.6-91406-Win.exe
wget http://download.virtualbox.org/virtualbox/4.3.6/Oracle_VM_VirtualBox_Extension_Pack-4.3.6-91406.vbox-extpack

# Djviewer
wget http://sourceforge.net/projects/djv/files/djv-stable/0.8.3%20Pre2/djv-0.8.3-pre2_winxp-x64.exe

# OpenOffice
wget http://sourceforge.net/projects/openofficeorg.mirror/files/4.0.1/binaries/en-US/Apache_OpenOffice_4.0.1_Win_x86_install_en-US.exe

# Blender
wget http://mirror.cs.umn.edu/blender.org/release/Blender2.69/blender-2.69-windows64.exe

# Handbrake 64bit
wget http://downloads.sourceforge.net/project/handbrake/0.9.9/HandBrake-0.9.9-1_x86_64-Win_GUI.exe

# MinGW
wget http://downloads.sourceforge.net/project/mingw-w64/mingw-w64/mingw-w64-release/mingw-w64-v3.0.0.tar.bz2
wget http://downloads.sourceforge.net/project/mingw/Other/Cross-Hosted%20MinGW%20Build%20Tool/x86-mingw32-build-1.0/x86-mingw32-build-1.0-sh.tar.bz2

# Maya - http://www.autodesk.com/products/autodesk-maya
wget http://download.autodesk.com/us/maya/service_packs/Autodesk_Maya_2014_SP1_English_Japanese_SimplifiedChinese_Win_64bit.exe

# 3Delight - manual download
# http://www.3delight.com/en/index.php?page=3DSP_download