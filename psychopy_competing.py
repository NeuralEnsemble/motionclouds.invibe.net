#!/usr/bin/env python
"""

Using psychopy to perform an experiment on competing clouds

(c) Laurent Perrinet - INT/CNRS

 See http://invibe.net/LaurentPerrinet/SciBlog/2012-12-12 for a small tutorial
 
"""
# width and height of your screen
w, h = 1920, 1200

print('launching experiment')
from psychopy import visual, core, event, logging, gui, misc
logging.console.setLevel(logging.DEBUG)

try:
    #try to load previous info
    info = misc.fromFile('data/competing.pickle')
except:
    #if no file use some defaults
    info = {}
    info['observer'] = ''
    info['screen_width'] = w
    info['screen_height'] = h
    info['nTrials'] = 50
    info['N_X'] = 256 # size of image
    info['N_Y'] = 256 # size of image
    info['N_frame_total'] = 128 # a full period. in time frames
    info['N_frame'] = 64 # length of the presented period. in time frames
try:
    dlg = gui.DlgFromDict(info)
except:
    print('Could not load gui... running with defaut parameters')
    print(info)
#save to a file for future use (ie storing as defaults)
if dlg.OK:
    misc.toFile('data/competing.pickle', info)
else:
    print('Could not load gui... running with defaut parameters')
    #core.quit() #user cancelled. quit

import time
info['timeStr'] = time.strftime("%b_%d_%H%M", time.localtime())


print('generating data')

import os, numpy
import MotionClouds as mc

fx, fy, ft = mc.get_grids(info['N_X'], info['N_Y'], info['N_frame_total'])
color = mc.envelope_color(fx, fy, ft)
up = 2*mc.rectif(mc.random_cloud(color * mc.envelope_gabor(fx, fy, ft, V_X=+.5))) - 1
down = 2*mc.rectif(mc.random_cloud(color * mc.envelope_gabor(fx, fy, ft, V_X=-.5))) - 1

print('go!      ')
win = visual.Window([info['screen_width'], info['screen_height']], fullscr=True)

stim = visual.GratingStim(win, 
        size=(info['screen_height'], info['screen_height']), units='pix',
        interpolate=False,
        autoLog=False)#this stim changes too much for autologging to be useful

wait_for_response = visual.TextStim(win, 
                        text = u"?", units='norm', height=0.15, color='DarkSlateBlue',
                        pos=[0., -0.], alignHoriz='center',alignVert='center' ) 
wait_for_next = visual.TextStim(win, 
                        text = u"x", units='norm', height=0.15, color='BlanchedAlmond',
                        pos=[0., -0.], alignHoriz='center',alignVert='center' ) 
                        
def getResponse():
    event.clearEvents()#clear the event buffer to start with
    resp = None#initially
    while 1:#forever until we returns
        for key in event.getKeys():
            #quit
            if key in ['escape', 'q']:
                    win.close()
                    #myWin.bits.reset()
                    core.quit()
                    return None
            #valid response - check to see if correct
            elif key in ['down', 'up']:
                    if key in ['down'] :return -1
                    else: return 1
            else:
                    print "hit DOWN or UP (or Esc) (You hit %s)" %key

def presentStimulus(C_A, C_B):
    """Present stimulus
    """
    phase_up = numpy.floor(numpy.random.rand() *(info['N_frame_total']-info['N_frame']))
    phase_down = numpy.floor(numpy.random.rand() *(info['N_frame_total']-info['N_frame']))
    for i_frame in range(info['N_frame']): # length of the stimulus
        stim.setTex(C_A * up[:, :, i_frame+phase_up]+C_B * down[:, :, i_frame+phase_down])
        stim.draw()
        win.flip()

results = numpy.zeros((2, info['nTrials']))
for i_trial in range(info['nTrials']):
    wait_for_next.draw()
    win.flip()
    core.wait(0.5)
    C_A = numpy.random.rand() # a random number between 0 and 1
    presentStimulus(C_A, 1. - C_A)
    wait_for_response.draw()
    win.flip()
    ans = getResponse()
    results[0, i_trial] = ans
    results[1, i_trial] = C_A

win.update()
core.wait(0.5)

win.close()

#save data
fileName = 'data/' + info['observer'] + '_' + info['timeStr']
numpy.save(fileName,results)

print('analyzing results')
# TODO: loop over all data + make a fit for each
import pylab
pylab.scatter(results[1, :], results[0, :])
pylab.axis([0., 1., -1.1, 1.1])
pylab.xlabel('contrast')
pylab.savefig('competing_psychopy.png')
