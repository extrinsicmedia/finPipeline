#finPipeline

finPipeline is a VFX pipeline for small team and studio use on commercial and film produciton.  We believe a successful pipeline is based on providing a flexible structure that enables consistency of delivery in the face of changing creative and technical demands.  Our goal is to provide a framework of tools to help in this process.


###Dependencies
Here's the bare minimum of dependencies to get started:
* Bash Shell
* Python 2.7
* pip
* shyaml
* A package management program (Homebrew, Cygwin, apt-get, etc)


###Installation

Instructions for installation of software requirements for the environment can be found in the /finPipeline/os directory.

Basic installation using Mac OSX as example:

1. Fork or clone finPipeline to your shared system server.  For example:

    `cd /mnt/server/systems/ && git clone https://github.com/extrinsicmedia/finPipeline.git`
    
    `cd /mnt/server/systems/ && git clone https://github.com/<your-git-name>/finPipeline.git`

2. Copy the config file to your $HOME directory and change the paths for your server:
    `cp finPipeline/config/finpipeline.yaml $HOME`
    `vim $HOME/finpipeline.yaml`

3. Run the following to source the unix_config_global.sh in your .bashrc file:
    `echo "source /mnt/server/systems/finPipeline/bash/unix_config_global.sh" >> ~/.bashrc`

4. Log any errors as Github issues or email for help.
