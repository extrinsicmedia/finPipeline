## Useful expressions and tcl for Nuke

# On/Off in GUI mode
$gui
$gui ? 1 : 0
$gui ? 1 : 16 #scanline render

# Use python wrapped in tcl
[python nuke.tcl("value gain")]

# check node directly above this one and return some values for a knob:
[value [value input[value 0].name].distortion2] + [value [value input[value 0].name].distortion1]  > 0 ? 1:0

# Nuke Random Range between max and min values
(1.1 - .9) * random(t) + .9

# random curve expression
random(1,frame*1)*1)+0
# or just simplified: 
random(1,frame)
# this creates a curve containing random values between 0 and 1.
# the breakdown controls:
(random(seed,frame*frequency)*amplitude)+valueOffset

# simple html for label knobs
<font color="red">Some red text</font> # change font color
<font color="blue">Some blue text</font> # a different font color
<b>Bold text</b> # bold text
