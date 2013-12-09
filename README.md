finPipeline is a VFX pipeline methodology that relies on environment variables to build out complex interoperability between various image manipulation and generation software packages.

Currently the project requires a bash environment and has been written as shell scripts and python code.

Instructions for installation of software requirements for the environment can be found in the /os directory.

Basic installation using Mac OSX 10.7.5 as example:

1. Clone finPipeline to your shared system server.  For example: 
    `/mnt/server/systems/finPipeline`

2. Change the appropriate paths in your os config file.  For the example os that would be:
    `/mnt/server/systems/finPipeline/bash/unix_config_global.sh`

3. Put the following line in your .bashrc file:
    `source /mnt/server/systems/finPipeline/bash/unix_config_global.sh`

4. Log any errors as Github issues or email for help.
