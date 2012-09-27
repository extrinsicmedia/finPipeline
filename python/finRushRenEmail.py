#!/usr/bin/env python
## Modified by Miles Lauridsen 2011-07-27
## Update information in lines 59 and 60 before use

import os
import sys
import csv
import subprocess

## Get info about RUSH job for email
jobid = os.environ.get('RUSH_JOBID', None)
user = sys.argv[1]
jobInfo = subprocess.Popen(['rush', '-lf', jobid], stdout=subprocess.PIPE).communicate()[0]
jobInfo = str(jobInfo)

## {{{ http://code.activestate.com/recipes/473810/ (r1)
# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Define these once; use them twice!
strFrom = os.environ.get('RENDER_EMAIL_NAME', None) + '@' + os.environ.get('SHOP_EMAIL', None) + '.' + os.environ.get('EXT_EMAIL', None)
strTo = user + '@' + os.environ.get('SHOP_EMAIL', None) + '.' + os.environ.get('EXT_EMAIL', None)

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = jobid + ' is finished rendering'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<img src="cid:image1"><br><p>' + str('Your render: ' + jobid + ' is finished. <br />Thanks for using RUSH.<br /><br />' + jobInfo), 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open(os.path.join(os.environ.get('SYSTEMS_SERVER', None), 'icons'), 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP()
smtp.connect('<email connection>')
smtp.login('<user@email.com>', '<password>')
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
## end of http://code.activestate.com/recipes/473810/ }}}