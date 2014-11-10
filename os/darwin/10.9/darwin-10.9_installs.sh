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
brew install -v nmap
brew install -v ncdu
brew install -v youtube-dl

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
brew install -v sphinx

# Languages
brew install -v python --universal --with-brewed-openssl
brew install -v pyqt
brew install -v pyside

# Sys-Admin and Security tools
brew install -v wireshark --with-qt --with-x --with-lua --devel
brew install -v duplicity
brew install -v collectd --debug --java
brew install -v osxfuse
brew install -v boot2docker
brew install -v clamav

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
sudo pip install virtualenv
sudo pip install matplotlib
sudo pip install scipy

# Image processing
brew install -v opencv --with-cuda --with-eigen --with-ffmpeg --with-java --with-openexr --with-openni --with-qt --with-tests
brew install -v opencolorio --with-docs --with-python
brew install -v pixie
brew install -v open-scene-graph --docs --with-collada-dom --with-ffmpeg --with-gnuplot --with-openexr

# For TuttleOFX in the future
brew install -v libraw libcaca libxml2 nasm xz jpeg-turbo, ctl
brew install -v openjpeg tinyxml freeglut swig libpng
brew install -v cfitsio field3d glew

# Landsat util
brew install https://raw.githubusercontent.com/developmentseed/landsat-util/master/Formula/landsat-util.rb

# Link apps such as Python and QT
sudo brew linkapps


### Pip installs 2
sudo pip install dagobah # cronjob type program with web interface
sudo pip install shyaml # terminal yaml reader
sudo pip install pysqlite
sudo pip install sqlalchemy
sudo pip install alembic
sudo pip install pyseq # compressed sequence string module for Python and Shell


### Lib Linking

# DJV install
sudo ln -s /Applications/djv-0.9.0.app/Contents/Resources/lib/libdjv_* /usr/local/lib
