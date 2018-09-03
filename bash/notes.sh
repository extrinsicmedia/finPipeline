# http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/
# list the keys in your public key ring:
gpg --list-keys

# list the keys in your secret key ring:
gpg --list-secret-keys

# Change files open limit
ulimit -n 1024

# list all connected drives OSX
diskutil list

# mount drive OSX - replace '/dev/disk1s2' with drive identifier
diskutil mount /dev/disk1s2

# unmount drive OSX - replace '/dev/disk1s2' with drive identifier
diskutil unmount /dev/disk1s2

# start ssh agent and add keys
eval `ssh-agent -s`
ssh-add

# encrypt a backup tar of the users Home dir
# http://blog.sanctum.geek.nz/linux-crypto-backups/
tar -cf docsbackup-"$(date +%Y-%m-%d)".tar $HOME/Documents
gpg --encrypt docsbackup-2013-07-27.tar