###    Flipbook current selected node with DJV View
###    DJV Imaging - http://djv.sourceforge.net/
###    ---------------------------------------------------------
###    djv_this.py v3.0
###    Created: 2012/05/29
###    Modified:
###    Modified by: Miles Lauridsen
###    miles@finvfx.com
###    Derived from the djv_this.py by Diogo Girondi
###    diogogirondi@gmail.com

import platform
import os.path
import subprocess
import re
import nuke
import nukescripts

### Path to the DJV executable #########################
djv_path = ''
########################################################

if djv_path == '':
    try:
        djv_path = os.environ[ 'DJVIEW' ]
    except:
        ## Windows
        if platform.system() in ( 'Windows', 'Microsoft' ):
            djv_path = 'C:\\Program Files (x86)\\djv 0.8.3\\bin]\djv_view.exe'
        ## OSX
        elif platform.system() in ( 'Darwin', 'Apple' ):
            djv_path = '/Application/DJV.app/Contents/MacOS/DJV'
        ## Linuxs
        else:
            djv_path = '/usr/local/djv/djv_view'
            

def djv_this( node, start, end, incr, view ):
    
    '''
    Plays the selected node sequence in DJV.
    You can get DJV at:
        http://djv.sourceforge.net/
        
    Use:
        djv_this( <node_object>, <start_frame>, <end_frame>, <frame_increment>, <view_name> )
    '''
    
    
    global djv_path

    if not os.access( djv_path, os.X_OK ):
        raise RuntimeError( 'DJV cannot be executed "%s".' % djv_path )
        
    if len( view ) > 1:
        raise RuntimeError( 'DJV currently does not support stereo sequences' )
        
    filename = nuke.filename( node )
    if filename is None or filename == '':
        raise RuntimeError( 'DJV cannot be executed on "%s", expected to find a file and there was none.' % node.fullName() )
        
    try:
        padding = re.findall( '%[0-9]*d', filename ).pop()
        range = ( padding % start )
        filename = re.sub( '%[0-9]*d', range, filename )
    except:
        raise RuntimeError( 'djv_this.py was unable to form the necessary string with: %s' % filename )
        
    cmd = []
    
    cmd.append( os.path.normpath( djv_path ) )

    ### DJV Options Start ################################################
    cmd.append( os.path.normpath( filename ) )
    # cmd.append( '-file_layer (value)' ) #layer name
    cmd.append( '-file_seq_auto True' )
    cmd.append( '-file_proxy 1/2' ) #Proxy scale: 1/2, 1/4, 1/8
    cmd.append( '-file_cache True' ) # Cache: True, False.
    # cmd.append( '-window_fullscreen' ) #Start in full screen
    # cmd.append("-window_toolbar False") # Toolbar controls: False, True.
    # cmd.append("-window_playbar False") # Window controls: False, True.
    # cmd.append("-view_grid None") # Grid overlay: None, 1x1, 10x10, 100x100.
    # cmd.append("-view_hud True") # Heads up display: True, False.
    cmd.append("-playback Forward") # Playback: Stop, Forward, Reverse.
    # cmd.append("-playback_frame (value)") # Frame.
    cmd.append("-playback_speed " + str( int( nuke.root().knob( 'fps' ).value() ) ) )
    # cmd.append("-playback_timer (value)") # Timer: Sleep, Timeout. Value: Sleep.
    # cmd.append("-playback_timer_resolution (value)") # Timer resolution (seconds): 0.001.
    cmd.append("-time_units Frames") # Time units: Timecode, Frames.
    ### DJV Options End ##################################################
    
    print ' '.join(cmd)
    subprocess.Popen( ' '.join( cmd ), shell=True )