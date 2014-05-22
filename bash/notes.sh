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