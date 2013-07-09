#!/usr/bin/env python

'''
fin_rmvList.py - A module to remove filenames from a list
Copyright (C) 2012  Miles Lauridsen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl.html/>.
'''

import re

def rmvList(fileNames, removeList):
    newList = fileNames
    fileNames = sorted(fileNames)
    removeList = sorted(removeList)    
    
    a = 0
    b = -1
    c = 0
    for x in fileNames:

        b = b + 1
        a = 0
        for x in removeList:
            if fileNames[b] == removeList[a]:
                newList.remove(removeList[a])        
                a = a + 1
                c = c + 1
            else:
                a = a + 1
    if c == 0:
        print "No items were removed from list"
    
    newList = sorted(newList)
    del fileNames, removeList, a, b, c
    return newList

### Check to see if all files in a list match any single item in a second list
def matchList(fileNames, checkList):
    newList = fileNames
    fileNames = sorted(fileNames)
    fileNum = len(fileNames)
    checkList = sorted(checkList)
    
    a = 0
    b = -1
    c = 0
    matchNum = 0
    
    for x in fileNames:

        b = b + 1
        a = 0
        for x in checkList:
            if fileNames[b] == checkList[a]:                       
                a = a + 1
                c = c + 1
            else:
                a = a + 1
    if c != fileNum:
        print "Not all of these items match the proper criteria"
        print "There are " + str(c) + " items that match the criteria"
        matchUp = False
    else:
        matchUp = True
    del newList, fileNames, fileNum, checkList, a, b, c
    return matchUp