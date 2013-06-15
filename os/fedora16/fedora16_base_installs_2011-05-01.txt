Fedora installs:

yum update
yum install apt gcc gcc-c++ boost boost-devel boost-jam python-devel wget python-setuptools automake make man
yum install opencv opencv-devel pango pango-devel cairo cairo-devel qt
yum install lcms lcms-devel fontconfig-devel fftw-devel libxml libxml2 libxml2-devel
yum install openexr openexr-devel libpng libpng-devel libjpeg libjpeg-devel libtiff
yum install libtiff-devel openjpeg ghostscript freetype dcraw tkinter

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

#$PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
#
#cd
#wget http://www.imagemagick.org/download/python/PythonMagick-0.9.7.tar.gz
#tar -xvzf PythonMagick-0.9.7.tar.gz
#cd PythonMagick-0.9.7/
#./configure --prefix=/usr/local
#make
#make install


## add to .bash_profile
#PYTHONPATH=$PYTHONPATH:/usr/local/lib64/python2.7/site-packages
#export PYTHONPATH

yum localinstall --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm

yum install ffmpeg

### GUI only
yum install argyllcms gimp firefox pidgin glut glut-devel
#pip install pyglet

## fin_Fedora16_KDE_x86_64_fixed_2012-05-10
yum install git

### 2012-05-29
yum install perl perl-devel
yum install openjpeg