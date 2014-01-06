jobStart.sh: run `jobstart somejobname somesequence someshot` and it will set the $JOB, $SEQUENCE, and $SHOT env vars and cd you into the shot.  
It also has some logic to read config files for each of those.  
Would also work with just a job and sequence or job and shot.
