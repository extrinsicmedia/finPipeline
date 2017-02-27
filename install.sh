cd $HOME

# Make Production directories
mkdir -p $HOME/PRODUCTION/PROJECTS
mkdir -p $HOME/PRODUCTION/SYSTEMS

# Clone finPipeline
git clone https://github.com/extrinsicmedia/finPipeline.git $HOME/PRODUCTION/SYSTEMS/fin
cd $HOME/PRODUCTION/SYSTEMS/fin

# Update Nuke to celsiusa branch
git submodule init
git submodule update
cd $HOME/PRODUCTION/SYSTEMS/fin/nuke
git checkout celsiusa

# Clone finPy


# Clone OCIO configs and checkout celsiusa branch
cd ../ocio
git clone https://github.com/extrinsicmedia/OpenColorIO-Configs.git
cd OpenColorIO-Configs
git checkout celsiusa