#!/bin/sh

if [ $1 ];
then
    echo $1;
    if [ $2 ];
    then
        echo $2;
        cp -rv $1/.adobe $2
        cp -rv $1/.bash_history $2
        cp -rv $1/.bash_logout $2
        cp -rv $1/.bashrc $2
        cp -rv $1/.ec2 $2
        cp -rv $1/.flexlmrc $2
        cp -rv $1/.git-credentials $2
        cp -rv $1/.gitconfig $2
        cp -rv $1/.gnupg $2
        cp -rv $1/.ipython $2
        cp -rv $1/.keychain $2
        cp -rv $1/.mysql_history $2
        cp -rv $1/.nuke $2
        cp -rv $1/.password-store $2
        cp -rv $1/.pip $2
        cp -rv $1/.profile $2
        cp -rv $1/.ssh $2
        cp -rv $1/.viminfo $2
        cp -rv $1/.vimrc $2
        cp -rv $1/.crontab $2
        cp -rv $1/.dropbox $2
    else
        echo "Please enter an output directory"
    fi
else
    echo "Please enter a source directory"
fi
