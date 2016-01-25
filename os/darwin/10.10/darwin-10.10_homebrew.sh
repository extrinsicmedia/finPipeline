### Homebrew installs

# Compilers and Core requirements
brew install -v cmake
brew install -v gcc
brew install -v tbb
brew install -v glib
brew install -v bash

# Security
brew install -v gnupg --8192
brew install -v pass
brew install -v keychain
brew install -v openssl
brew install -v gpg-agent

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
brew install -v watch

# Database
brew install -v postgresql
brew install -v mongodb

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
# oiio expects libhdf5.9.dylib. This appears to fix the issue
if [ ! -f /usr/local/lib/libhdf5.9.dylib ];
then
    ln -s /usr/local/lib/libhdf5.10.dylib /usr/local/lib/libhdf5.9.dylib
fi
brew install -v alembic

# Imaging
brew install -v ilmbase
brew install -v openexr
brew install -v opencolorio --with-docs --with-python
brew install -v openimageio # --with-qt and --with-tests currently fail
brew install -v openvdb

# FFmpeg
brew install -v ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-frei0r --with-libass --with-libaca --with-libvo-aacenc --with-libvorbis --with-libvpx --with-openjpeg --with-openssl --with-speex --with-theora --with-tools

# Imagemagick
brew install -v imagemagick --enable-hdri --with-fftw --with-fontconfig --with-jp2 --with-libtiff --with-little-cms --with-liblqr --with-librsvg --with-little-cms2 --with-openexr --with-webp --with-perl --with-quantum-depth-32 --with-x11

# Image processing
brew install -v opencv --with-cuda --with-eigen --with-ffmpeg --with-java --with-openexr --with-openni --with-qt --with-tests
brew install -v pixie
brew install -v open-scene-graph --docs --with-collada-dom --with-ffmpeg --with-gnuplot --with-openexr

# Link apps such as Python and QT Designer
sudo brew linkapps
