#!/bin/sh

# Examples of commonly used bash syntax goes here

# Create .tgz:
tar cvzfw fileName.tgz directory

# Extract:
tar xvzf fileName.tgz

# rsync examples
# dry run with exclusions
rsync -vrn --exclude=".dropbox" --exclude=".DS_Store" --ignore-existing ~/some_path/ ~/another_path/