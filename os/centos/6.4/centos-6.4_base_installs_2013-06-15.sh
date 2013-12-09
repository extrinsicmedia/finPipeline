Fedora installs:

yum update
yum install apt gcc gcc-c++ boost boost-devel boost-jam python-devel wget python-setuptools automake make man
yum install opencv opencv-devel pango pango-devel cairo cairo-devel qt git perl perl-devel
yum install lcms lcms-devel fontconfig-devel fftw-devel libxml libxml2 libxml2-devel
yum install openexr openexr-devel libpng libpng-devel libjpeg libjpeg-devel libtiff openjpeg
yum install libtiff-devel openjpeg ghostscript freetype dcraw tkinter

## FFMBC and FFMPEG Dependencies
yum install build-essential yasm libgpac-dev libdirac-dev libgsm1-dev libschroedinger-dev
yum install libspeex-dev libvorbis-dev libopenjpeg-dev libdc1394-22-dev libsdl1.2-dev
yum install zlib1g-dev texi2html libfaac-dev libmp3lame-dev libtheora-dev libxvidcore4-dev
yum install libopencore-amrnb-dev libopencore-amrwb-dev frei0r-plugins-dev libcv-dev
yuym install libvpx-dev libgavl1 libx264-dev

easy_install pip
pip install virtualenv
pip install PIL
pip install psutil

wget ftp://ftp.imagemagick.org/pub/ImageMagick/ImageMagick.tar.gz
tar -xzvf ImageMagick.tar.gz
cd ImageMagick/
./configure --prefix=/usr/local --enable-hdri
make
make install

## add to .bash_profile
#PYTHONPATH=$PYTHONPATH:/usr/local/lib64/python2.7/site-packages
#export PYTHONPATH

## May not need this anymore?
#yum localinstall --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm
#yum install ffmpeg

### GUI only
yum install argyllcms gimp firefox pidgin glut glut-devel