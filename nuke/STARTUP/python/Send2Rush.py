#Send2Rush v1.0

#Sends current Nuke Script to Rush Submit GUI with fields prefilled (frame range, job title etc)
#Written by John Cairns ( jc@misterjohn.net ) with thanks to Justin & Frank Reuter

#Modified by Miles Lauridsen 2012-09-26

import nuke
import os
import os.path
import time
import shutil
from datetime import date
import getpass

def Nuke2Rush():
    # save the project first
    nuke.scriptSave()
    rushFile = os.environ.get('RUSH_NUKE_FILE', None)
    nukeArchive = os.environ.get('NUKE_ARCHIVE', None)
    user = getpass.getuser()
    renderEmail = str('python ' + str(os.environ.get('PYTHON_SERVER', None)) + 'finRushRenEmail.py ' + user)
    
    # set current date and times
    curDate = time.localtime(time.time() )
    today = str(date.today())
    dateStamp = str(curDate[0]) + '-' + str(curDate[1]) + '-' + str(curDate[2]) + '_' + str(curDate[3]) + '_' + str(curDate[4]) + '_' + str(curDate[5])
    todaysArchive = os.path.join(nukeArchive, today)
    
    # get the script variables
    script_name=nuke.Root().name()
    start=nuke.Root().firstFrame()
    end=nuke.Root().lastFrame()
    job_path=os.path.basename(script_name)
    (job_title, extension)=os.path.splitext(job_path)
    cmd = "" + rushFile + " -field NukeScript " + script_name + " -field Frames " + str(start) + "-" + str(end) + " -field JobTitle " + job_title + '_' + user + " -field JobDoneCommand \"" + renderEmail + "\""
    
    # make a backup of the script to be rendered
    if not os.path.exists(os.path.abspath(todaysArchive)):
        os.makedirs(os.path.abspath(todaysArchive))
    shutil.copy(os.path.abspath(script_name),os.path.abspath(todaysArchive + '/' + job_title + '_' + dateStamp + '.nk'))
    os.system(cmd)
    
def saveScript():
    scriptSave(filename=None)