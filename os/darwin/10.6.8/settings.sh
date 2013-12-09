#!/bin/sh

# Examples for OSX System 10.6.8 setup, commands, and settings here

## TO DO
## Rewrite workflow starting from fresh install of 10.6.8

# To select the 64-bit kernel for the current startup disk, use the following command in Terminal:
sudo systemsetup -setkernelbootarchitecture x86_64

# To select the 32-bit kernel for the current startup disk, use the following command in Terminal:
sudo systemsetup -setkernelbootarchitecture i386