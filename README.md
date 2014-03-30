finPipeline is a VFX pipeline methodology that relies on environment variables to build out complex interoperability between various image manipulation and generation software packages.

Currently the project requires a bash environment and has been written as shell scripts and python code.

Instructions for installation of software requirements for the environment can be found in the /finPipeline/os directory.

Basic installation using Mac OSX 10.7.5 as example:

1. Clone finPipeline to your shared system server.  For example: 
    `cd /mnt/server/systems/ && git clone https://github.com/extrinsicmedia/finPipeline.git`

2. Change the appropriate paths in your os config file.  For the example os that would be:
    `finPipeline/bash/unix_config_global.sh`

3. Put the following line in your .bashrc file:
    `echo "source /mnt/server/systems/finPipeline/bash/unix_config_global.sh" >> ~/.bashrc`

4. Use /finPipeline/python/fin/fin/fileOps/dirOps.py to create your job folders.

5. Log any errors as Github issues or email for help.


If you find this code useful, feel free to tip: https://www.gittip.com/extrinsicmedia


