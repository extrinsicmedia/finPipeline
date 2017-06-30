# Helpful bash commands

List the keys in your public key ring
http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/
`gpg --list-keys`

List the keys in your secret key ring:
`gpg --list-secret-keys`

Change files open limit
`ulimit -n 1024`

List all connected drives OSX
`diskutil list`

Mount drive OSX - replace '/dev/disk1s2' with drive identifier
`diskutil mount /dev/disk1s2`

Unmount drive OSX - replace '/dev/disk1s2' with drive identifier
`diskutil unmount /dev/disk1s2`

Start ssh agent and add keys
```
eval `ssh-agent -s`
ssh-add
```

Encrypt a backup tar of the users Home dir
http://blog.sanctum.geek.nz/linux-crypto-backups/
`tar -cf docsbackup-"$(date +%Y-%m-%d)".tar $HOME/Documents`
`gpg --encrypt docsbackup-2013-07-27.tar`