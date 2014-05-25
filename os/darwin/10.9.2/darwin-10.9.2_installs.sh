### Homebrew installs

# Compilers and Core requirements
brew install -v cmake
brew install -v gcc
brew install -v tbb
brew install -v glib

# Security
brew install -v gnupg --8192
brew install -v pass
brew install -v keychain
brew install -v openssl

# Utilities
brew install -v curl
brew install -v git
brew install -v wget
brew install -v vim
brew install -v colordiff
brew install -v coreutils
brew install -v unrar
brew install -v htop

# Database
brew install -v postgresql

# Development
brew install -v qt --universal --with-docs --with-mysql
brew install -v scons
brew install -v boost --with-mpi --with-python --without-single
brew install -v doxygen
brew install -v jsonpp
brew install -v libyaml
brew install -v fltk
brew install -v gdk-pixbuf
brew install -v pixman
brew install -v harfbuzz
brew install -v fontconfig
brew install -v pango

# Languages
brew install -v python --universal --with-brewed-openssl
brew install -v pyqt
brew install -v python3 --quicktest --with-brewed-openssl
brew install -v pyside --with-python3

# Sys-Admin tools
brew install -v wireshark --with-qt --with-x --with-lua --devel
brew install -v duplicity
brew install -v collectd --debug --java
brew install -v osxfuse
brew install -v boot2docker

# Homebrew science
brew tap homebrew/science
brew install -v hdf5
brew install -v alembic

# Imaging
brew install -v ilmbase
brew install -v openexr

# FFmpeg
brew install -v ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-frei0r --with-libass --with-libaca --with-libvo-aacenc --with-libvorbis --with-libvpx --with-openjpeg --with-openssl --with-speex --with-theora --with-tools 

# Imagemagick
brew install -v imagemagick --with-fontconfig --with-jasper --with-quantum-depth-32 --with-liblqr --with-librsvg --with-libtiff --with-libwmf --with-little-cms --with-openexr --with-webp


### Pip installs 1
sudo pip install numpy


# Image processing
brew install -v opencv --with-cuda --with-eigen --with-ffmpeg --with-java --with-openexr --with-openni --with-qt --with-tests
brew install -v opencolorio --with-docs --with-python --with-java --with-tests
brew install -v pixie
brew install -v open-scene-graph --docs --with-collada-dom --with-ffmpeg --with-gnuplot --with-openexr

# For TuttleOFX in the future
brew install -v libraw libcaca libxml2 nasm xz jpeg-turbo, ctl
brew install -v openjpeg tinyxml freeglut swig libpng
brew install -v cfitsio field3d glew

# Link apps such as Python and QT
sudo brew linkapps


### Pip installs 2
sudo pip install dagobah
sudo pip install shyaml
sudo pip install pysqlite
sudo pip install sqlalchemy
sudo pip install alembic


### Lib Linking

# DJV install
sudo ln -s /Applications/djv-0.9.0.app/Contents/Resources/lib/libdjv_* /usr/local/lib
