#!/usr/bin/env python

import pymel.core as pm
import os

jobServer = os.environ.get('JOB_SERVER', None)
project = os.path.join(jobServer, "celsiusa/production/build/prj/maya")
pm.mel.eval(' setProject  "' + project + '"')