#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Chelsea Harmon 
#cmh2228@columbia.edu
#March 2018 

"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Mon Feb 19 14:40:12 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'sequenceLearningTask'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsGeneral = visual.TextStim(win=win, name='instructionsGeneral',
    text="\n\nGo as fast as you can to catch the minion before he escapes! \n\n\n\n\n\n(experimenter press spacebar)",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
image_paw1 = visual.ImageStim(
    win=win, name='image_paw1',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='Press 1 when a minion is here ',
    font='Arial',
    pos=(0, .8), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "practice2"
practice2Clock = core.Clock()
image_paw2 = visual.ImageStim(
    win=win, name='image_paw2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press 2 when a minion is here ',
    font='Arial',
    pos=(0, .8), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "practice3"
practice3Clock = core.Clock()
image_paw3 = visual.ImageStim(
    win=win, name='image_paw3',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press 3 when a minion is here ',
    font='Arial',
    pos=(0, .8), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "practice4"
practice4Clock = core.Clock()
image_paw4 = visual.ImageStim(
    win=win, name='image_paw4',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='Press 4 when a minion is here ',
    font='Arial',
    pos=(0, .8), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Get Ready...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='GO!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "randomStim"
randomStimClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stimBlank"
stimBlankClock = core.Clock()
blankImage = visual.ImageStim(
    win=win, name='blankImage',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Take a short break \n\n(Press spacebar when you are ready to continue) ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "stim1"
stim1Clock = core.Clock()
pos1 = visual.ImageStim(
    win=win, name='pos1',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(2,2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stim2"
stim2Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stim3"
stim3Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "stim4"
stim4Clock = core.Clock()
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
goodJob = visual.TextStim(win=win, name='goodJob',
    text='You did it!!!! \n\nYou caught 400 minions! \n\nGreat Job!!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(120.000000)
# update component parameters for each repeat
instructionsGeneral.setColor('white', colorSpace='rgb')
instructionsResponse = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instructionsGeneral, instructionsResponse]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionsGeneral* updates
    if t >= 0.0 and instructionsGeneral.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsGeneral.tStart = t
        instructionsGeneral.frameNStart = frameN  # exact frame index
        instructionsGeneral.setAutoDraw(True)
    frameRemains = 0.0 + 120.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instructionsGeneral.status == STARTED and t >= frameRemains:
        instructionsGeneral.setAutoDraw(False)
    
    # *instructionsResponse* updates
    if t >= 0.0 and instructionsResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsResponse.tStart = t
        instructionsResponse.frameNStart = frameN  # exact frame index
        instructionsResponse.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 120- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instructionsResponse.status == STARTED and t >= frameRemains:
        instructionsResponse.status = STOPPED
    if instructionsResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['space', 'enter', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pawStimuli.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_paw1.setImage(pawPatrol1)
    text.setColor('black', colorSpace='rgb')
    key_resp_1 = event.BuilderKeyResponse()
    # keep track of which components have finished
    practiceComponents = [image_paw1, text, key_resp_1]
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_paw1* updates
        if t >= 0.0 and image_paw1.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_paw1.tStart = t
            image_paw1.frameNStart = frameN  # exact frame index
            image_paw1.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_paw1.status == STARTED and t >= frameRemains:
            image_paw1.setAutoDraw(False)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # *key_resp_1* updates
        if t >= 0.0 and key_resp_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_1.tStart = t
            key_resp_1.frameNStart = frameN  # exact frame index
            key_resp_1.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space', 'return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # was this 'correct'?
                if (key_resp_1.keys == str('1')) or (key_resp_1.keys == '1'):
                    key_resp_1.corr = 1
                else:
                    key_resp_1.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice2"-------
    t = 0
    practice2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_paw2.setImage(pawPatrol2)
    text_2.setColor('black', colorSpace='rgb')
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    practice2Components = [image_paw2, text_2, key_resp_2]
    for thisComponent in practice2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice2"-------
    while continueRoutine:
        # get current time
        t = practice2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_paw2* updates
        if t >= 0.0 and image_paw2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_paw2.tStart = t
            image_paw2.frameNStart = frameN  # exact frame index
            image_paw2.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_paw2.status == STARTED and t >= frameRemains:
            image_paw2.setAutoDraw(False)
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space', 'return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # was this 'correct'?
                if (key_resp_2.keys == str('2')) or (key_resp_2.keys == '2'):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice2"-------
    for thisComponent in practice2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice3"-------
    t = 0
    practice3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_paw3.setImage(pawPatrol3)
    text_3.setColor('black', colorSpace='rgb')
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    practice3Components = [image_paw3, text_3, key_resp_3]
    for thisComponent in practice3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice3"-------
    while continueRoutine:
        # get current time
        t = practice3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_paw3* updates
        if t >= 0.0 and image_paw3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_paw3.tStart = t
            image_paw3.frameNStart = frameN  # exact frame index
            image_paw3.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_paw3.status == STARTED and t >= frameRemains:
            image_paw3.setAutoDraw(False)
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space', 'return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # was this 'correct'?
                if (key_resp_3.keys == str('3')) or (key_resp_3.keys == '3'):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice3"-------
    for thisComponent in practice3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice4"-------
    t = 0
    practice4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_paw4.setImage(pawPatrol4)
    text_4.setColor('black', colorSpace='rgb')
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    practice4Components = [image_paw4, text_4, key_resp_4]
    for thisComponent in practice4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice4"-------
    while continueRoutine:
        # get current time
        t = practice4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_paw4* updates
        if t >= 0.0 and image_paw4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_paw4.tStart = t
            image_paw4.frameNStart = frameN  # exact frame index
            image_paw4.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_paw4.status == STARTED and t >= frameRemains:
            image_paw4.setAutoDraw(False)
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_4.status == STARTED and t >= frameRemains:
            text_4.setAutoDraw(False)
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space', 'return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # was this 'correct'?
                if (key_resp_4.keys == str('4')) or (key_resp_4.keys == '4'):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice4"-------
    for thisComponent in practice4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "practice4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "instructions2"-------
t = 0
instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructions2Components = [text_5, text_6]
for thisComponent in instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_5.status == STARTED and t >= frameRemains:
        text_5.setAutoDraw(False)
    
    # *text_6* updates
    if t >= 1 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#
#
# set up handler to look after randomisation of conditions etc
#trials_1 = data.TrialHandler(nReps=25, method='random', 
#    extraInfo=expInfo, originPath=-1,
#    trialList=data.importConditions(u'random.xlsx'),
#    seed=None, name='trials_1')
#thisExp.addLoop(trials_1)  # add the loop to the experiment
#thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
#if thisTrial_1 != None:
#    for paramName in thisTrial_1.keys():
#        exec(paramName + '= thisTrial_1.' + paramName)
#
#for thisTrial_1 in trials_1:
#    currentLoop = trials_1
#    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
#    if thisTrial_1 != None:
#        for paramName in thisTrial_1.keys():
#            exec(paramName + '= thisTrial_1.' + paramName)
#            
#    # ------Prepare to start Routine "randomStim"-------
#    t = 0
#    randomStimClock.reset()  # clock
#    frameN = -1
#    continueRoutine = True
#    # update component parameters for each repeat
#    image.setImage(randomPaw)
#    key_resp_9 = event.BuilderKeyResponse()
#    # keep track of which components have finished
#    randomStimComponents = [image, key_resp_9]
#    for thisComponent in randomStimComponents:
#        if hasattr(thisComponent, 'status'):
#            thisComponent.status = NOT_STARTED
#    
#    # -------Start Routine "randomStim"-------
#    while continueRoutine:
#        # get current time
#        t = randomStimClock.getTime()
#        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#        # update/draw components on each frame
#        
#        # *image* updates
#        if t >= 0.0 and image.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            image.tStart = t
#            image.frameNStart = frameN  # exact frame index
#            image.setAutoDraw(True)
#        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
#        if image.status == STARTED and t >= frameRemains:
#            image.setAutoDraw(False)
#        
#        # *key_resp_9* updates
#        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            key_resp_9.tStart = t
#            key_resp_9.frameNStart = frameN  # exact frame index
#            key_resp_9.status = STARTED
#            # AllowedKeys looks like a variable named `allowableKey`
#            if not type(allowableKey) in [list, tuple, np.ndarray]:
#                if not isinstance(allowableKey, basestring):
#                    logging.error('AllowedKeys variable `allowableKey` is not string- or list-like.')
#                    core.quit()
#                elif not ',' in allowableKey: allowableKey = (allowableKey,)
#                else:  allowableKey = eval(allowableKey)
#            # keyboard checking is just starting
#            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
#        if key_resp_9.status == STARTED:
#            theseKeys = event.getKeys(keyList=list(allowableKey))
#            
#            # check for quit:
#            if "escape" in theseKeys:
#                endExpNow = True
#            if len(theseKeys) > 0:  # at least one key was pressed
#                key_resp_9.keys.extend(theseKeys)  # storing all keys
#                key_resp_9.rt.append(key_resp_9.clock.getTime())
#                print('you pressed: ')
#                print(theseKeys)
#                print('correct key was ')
#                print(correctKey)
#                # was this 'correct'?
#                #if (theseKeys) == (correctKey):
#                if ((theseKeys) == (correctKey)): 
#                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
#                    print('you got it right!!!')
#                    print('length of response key:')
#                    if len(key_resp_9.keys) == 1:
#                        key_resp_9_corr = 1
#                        #print('key resp 9 corr should be 1:')
#                        #print(key_resp_9_corr)
#                        trialCorrect = 1
#                        trials_1.addData('trialCorrect',trialCorrect)
#                    else: 
#                        key_resp_9_corr = 0
#                        #print('the first element was not right: should be 0')
#                        #print(key_resp_9_corr)
#                        trialCorrect = 0
#                        trials_1.addData('trialCorrect',trialCorrect)
#                    #key_resp_9.corr = 1
#                    continueRoutine = False
#                else:
#                    #key_resp_9.corr = 0
#                    continueRoutine = True
#                # a response ends the routine
#                #continueRoutine = True
#        
#        # check if all components have finished
#        if not continueRoutine:  # a component has requested a forced-end of Routine
#            break
#        continueRoutine = False  # will revert to True if at least one component still running
#        for thisComponent in randomStimComponents:
#            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                continueRoutine = True
#                break  # at least one component has not yet finished
#        
#        # check for quit (the Esc key)
#        if endExpNow or event.getKeys(keyList=["escape"]):
#            core.quit()
#        
#        # refresh the screen
#        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#            win.flip()
#    
#    # -------Ending Routine "randomStim"-------
#    for thisComponent in randomStimComponents:
#        if hasattr(thisComponent, "setAutoDraw"):
#            thisComponent.setAutoDraw(False)
#    # check responses
#    if key_resp_9.keys in ['', [], None]:  # No response was made
#        key_resp_9.keys=None
#        # was no response the correct answer?!
#        if str(u'correctKey').lower() == 'none':
#           key_resp_9.corr = 1  # correct non-response
#        else:
#           key_resp_9.corr = 0  # failed to respond (incorrectly)
#    # store data for trials_2 (TrialHandler)
#    trials_1.addData('key_resp_9.keys',key_resp_9.keys)
#    trials_1.addData('key_resp_9.corr', key_resp_9.corr)
#    if key_resp_9.keys != None:  # we had a response
#        trials_1.addData('key_resp_9.rt', key_resp_9.rt)
#    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
#    routineTimer.reset()
#    
#    # ------Prepare to start Routine "stimBlank"-------
#    t = 0
#    stimBlankClock.reset()  # clock
#    frameN = -1
#    continueRoutine = True
#    routineTimer.add(0.500000)
#    # update component parameters for each repeat
#    blankImage.setImage(blank)
#    # keep track of which components have finished
#    stimBlankComponents = [blankImage]
#    for thisComponent in stimBlankComponents:
#        if hasattr(thisComponent, 'status'):
#            thisComponent.status = NOT_STARTED
#    
#    # -------Start Routine "stimBlank"-------
#    while continueRoutine and routineTimer.getTime() > 0:
#        # get current time
#        t = stimBlankClock.getTime()
#        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#        # update/draw components on each frame
#        
#        # *blankImage* updates
#        if t >= 0.0 and blankImage.status == NOT_STARTED:
#            # keep track of start time/frame for later
#            blankImage.tStart = t
#            blankImage.frameNStart = frameN  # exact frame index
#            blankImage.setAutoDraw(True)
#        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
#        if blankImage.status == STARTED and t >= frameRemains:
#            blankImage.setAutoDraw(False)
#        
#        # check if all components have finished
#        if not continueRoutine:  # a component has requested a forced-end of Routine
#            break
#        continueRoutine = False  # will revert to True if at least one component still running
#        for thisComponent in stimBlankComponents:
#            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#                continueRoutine = True
#                break  # at least one component has not yet finished
#        
#        # check for quit (the Esc key)
#        if endExpNow or event.getKeys(keyList=["escape"]):
#            core.quit()
#        
#        # refresh the screen
#        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#            win.flip()
#    
#    # -------Ending Routine "stimBlank"-------
#    for thisComponent in stimBlankComponents:
#        if hasattr(thisComponent, "setAutoDraw"):
#            thisComponent.setAutoDraw(False)
#    thisExp.nextEntry()
#    
# completed 25 repeats of 'trials_1'
#
#
# ------Prepare to start Routine "break_2"-------
#t = 0
#break_2Clock.reset()  # clock
#frameN = -1
#continueRoutine = True
#routineTimer.add(120.000000) #How long the screen will be up for 
# update component parameters for each repeat
#break_2Response = event.BuilderKeyResponse()
# keep track of which components have finished
#break_2Components = [text_7, break_2Response]
#for thisComponent in break_2Components:
#    if hasattr(thisComponent, 'status'):
#        thisComponent.status = NOT_STARTED
#
#-------Start Routine "break_2"-------
#while continueRoutine and routineTimer.getTime() > 0:
#    # get current time
#    t = break_2Clock.getTime()
#    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#    # update/draw components on each frame
#            
#    # *text_7* updates
#    if t >= 0.0 and text_7.status == NOT_STARTED:
#        #keep track of start time/frame for later 
#        text_7.tStart = t 
#        text_7.frameNStart = frameN #extract frame index
#        text_7.setAutoDraw(True)
#    frameRemains = 0.0 + 120.0- win.monitorFramePeriod * 0.75 #most of one frame period left
#    if text_7.status == STARTED and t >= frameRemains: 
#        text_7.setAutoDraw(False) 
#            
#     # *break_2Response* updates
#    if t >= 0.0 and break_2Response.status == NOT_STARTED:
#        # keep track of start time/frame for later
#        break_2Response.tStart = t
#        break_2Response.frameNStart = frameN  # exact frame index
#        break_2Response.status = STARTED 
#        # keyboard checking is just startgin
#    frameRemains = 0.0 + 120- win.monitorFramePeriod * 0.75  # most of one frame period left
#    if break_2Response.status == STARTED and t >= frameRemains:
#        break_2Response.status == STOPPED
#    if break_2Response.status == STARTED: 
#        theseKeys = event.getKeys(keyList=['space', 'enter', 'return'])
#        
#        # check for quit:
#        if "escape" in theseKeys:
#            endExpNow = True
#        if len(theseKeys) > 0:  # at least one key was pressed
#            # a response ends the routine
#            continueRoutine = False
#                
#    # check if all components have finished
#    if not continueRoutine:  # a component has requested a forced-end of Routine
#        break
#    continueRoutine = False  # will revert to True if at least one component still running
#    for thisComponent in break_2Components:
#        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#            continueRoutine = True
#            break  # at least one component has not yet finished
#    
#    # check for quit (the Esc key)
#    if endExpNow or event.getKeys(keyList=["escape"]):
#        core.quit()
#    
#    # refresh the screen
#    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#        win.flip()
#
# -------Ending Routine "break_2"-------
#for thisComponent in break_2Components:
#    if hasattr(thisComponent, "setAutoDraw"):
#        thisComponent.setAutoDraw(False)
#
# ------Prepare to start Routine "instructions2"-------
#t = 0
#instructions2Clock.reset()  # clock
#frameN = -1
#continueRoutine = True
#routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
#instructions2Components = [text_5, text_6]
#for thisComponent in instructions2Components:
#    if hasattr(thisComponent, 'status'):
#        thisComponent.status = NOT_STARTED
#
# -------Start Routine "instructions2"-------
#while continueRoutine and routineTimer.getTime() > 0:
#    # get current time
#    t = instructions2Clock.getTime()
#    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
#    # update/draw components on each frame
#    
#    # *text_5* updates
#    if t >= 0.0 and text_5.status == NOT_STARTED:
#        # keep track of start time/frame for later
#        text_5.tStart = t
#        text_5.frameNStart = frameN  # exact frame index
#        text_5.setAutoDraw(True)
#    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
#    if text_5.status == STARTED and t >= frameRemains:
#        text_5.setAutoDraw(False)
#    
#    # *text_6* updates
#    if t >= 1 and text_6.status == NOT_STARTED:
#        # keep track of start time/frame for later
#        text_6.tStart = t
#        text_6.frameNStart = frameN  # exact frame index
#        text_6.setAutoDraw(True)
#    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
#    if text_6.status == STARTED and t >= frameRemains:
#        text_6.setAutoDraw(False)
#    
#    # check if all components have finished
#    if not continueRoutine:  # a component has requested a forced-end of Routine
#        break
#    continueRoutine = False  # will revert to True if at least one component still running
#    for thisComponent in instructions2Components:
#        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
#            continueRoutine = True
#            break  # at least one component has not yet finished
#    
#    # check for quit (the Esc key)
#    if endExpNow or event.getKeys(keyList=["escape"]):
#        core.quit()
#    
#    # refresh the screen
#    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
#        win.flip()
#
# -------Ending Routine "instructions2"-------
#for thisComponent in instructions2Components:
#    if hasattr(thisComponent, "setAutoDraw"):
#        thisComponent.setAutoDraw(False)
#



# -------Setting Up Repition-------
# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pawStimuli.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
            
    # ------Prepare to start Routine "stim1"-------
    t = 0
    stim1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    pos1.setImage(pawPatrol1)
    key_resp_1 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim1Components = [pos1, key_resp_1]
    for thisComponent in stim1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim1"-------
    while continueRoutine:
        # get current time
        t = stim1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pos1* updates
        if t >= 0.0 and pos1.status == NOT_STARTED:
            # keep track of start time/frame for later
            pos1.tStart = t
            pos1.frameNStart = frameN  # exact frame index
            pos1.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if pos1.status == STARTED and t >= frameRemains:
            pos1.setAutoDraw(False)
        if pos1.status == STARTED:  # only update if drawing
            pos1.setPos((0, 0), log=False)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_1.tStart = t
            key_resp_1.frameNStart = frameN  # exact frame index
            key_resp_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        if key_resp_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_1.keys.extend(theseKeys)  # storing all keys
                key_resp_1.rt.append(key_resp_1.clock.getTime())
                # was this 'correct'?
                if ((theseKeys) == (['1'])): 
                    if len(key_resp_1.keys) == 1:
                        key_resp_1_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_1_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim1"-------
    for thisComponent in stim1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_1.keys',key_resp_1.keys)
    trials_2.addData('key_resp_1.corr', key_resp_1.corr)
    if key_resp_1.keys != None:  # we had a response
        trials_2.addData('key_resp_1.rt', key_resp_1.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim3"-------
    t = 0
    stim3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_4.setImage(pawPatrol3)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim3Components = [image_4, key_resp_2]
    for thisComponent in stim3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim3"-------
    while continueRoutine:
        # get current time
        t = stim3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_4.status == STARTED and t >= frameRemains:
            image_4.setAutoDraw(False)
        
        # *key_resp_7* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['3', '1', '2', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys.extend(theseKeys)  # storing all keys
                key_resp_2.rt.append(key_resp_2.clock.getTime())
                # was this 'correct'?
                if ((theseKeys) == (['3'])): 
                    if len(key_resp_2.keys) == 1:
                        key_resp_2_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_2_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim3"-------
    for thisComponent in stim3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    trials_2.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim2"-------
    t = 0
    stim2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(pawPatrol2)
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim2Components = [image_3, key_resp_3]
    for thisComponent in stim2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim2"-------
    while continueRoutine:
        # get current time
        t = stim2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '1', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys.extend(theseKeys)  # storing all keys
                key_resp_3.rt.append(key_resp_3.clock.getTime())
                # was this 'correct'?
                if ((theseKeys) == (['2'])): 
                    if len(key_resp_3.keys) == 1:
                        key_resp_3_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_3_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim2"-------
    for thisComponent in stim2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    trials_2.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_4]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys.extend(theseKeys)  # storing all keys
                key_resp_4.rt.append(key_resp_4.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['4'])): 
                    if len(key_resp_4.keys) == 1:
                        key_resp_4_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_4_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_4.keys',key_resp_4.keys)
    trials_2.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials_2.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_5]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys.extend(theseKeys)  # storing all keys
                key_resp_5.rt.append(key_resp_5.clock.getTime())
                # was this 'correct'?
                if ((theseKeys) == (['4'])): 
                    if len(key_resp_5.keys) == 1:
                        key_resp_5_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_5.keys',key_resp_5.keys)
    trials_2.addData('key_resp_5.corr', key_resp_5.corr)
    if key_resp_5.keys != None:  # we had a response
        trials_2.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim2"-------
    t = 0
    stim2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(pawPatrol2)
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim2Components = [image_3, key_resp_6]
    for thisComponent in stim2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim2"-------
    while continueRoutine:
        # get current time
        t = stim2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '1', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys.extend(theseKeys)  # storing all keys
                key_resp_6.rt.append(key_resp_6.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['2'])): 
                    if len(key_resp_6.keys) == 1:
                        key_resp_6_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_6_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim2"-------
    for thisComponent in stim2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_6.keys',key_resp_6.keys)
    trials_2.addData('key_resp_6.corr', key_resp_6.corr)
    if key_resp_6.keys != None:  # we had a response
        trials_2.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim3"-------
    t = 0
    stim3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_4.setImage(pawPatrol3)
    key_resp_7 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim3Components = [image_4, key_resp_7]
    for thisComponent in stim3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim3"-------
    while continueRoutine:
        # get current time
        t = stim3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_4.status == STARTED and t >= frameRemains:
            image_4.setAutoDraw(False)
        
        # *key_resp_7* updates
        if t >= 0.0 and key_resp_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_7.tStart = t
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        if key_resp_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['3', '1', '2', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_7.keys.extend(theseKeys)  # storing all keys
                key_resp_7.rt.append(key_resp_7.clock.getTime())
                # was this 'correct'?
                if ((theseKeys) == (['3'])): 
                    if len(key_resp_7.keys) == 1:
                        key_resp_7_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_7_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim3"-------
    for thisComponent in stim3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_7.keys',key_resp_7.keys)
    trials_2.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        trials_2.addData('key_resp_7.rt', key_resp_7.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_8 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_8]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_8.keys.extend(theseKeys)  # storing all keys
                key_resp_8.rt.append(key_resp_8.clock.getTime())
                # was this 'correct'?
                if ((theseKeys) == (['4'])): 
                    if len(key_resp_8.keys) == 1:
                        key_resp_8_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_8_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_8.keys',key_resp_8.keys)
    trials_2.addData('key_resp_8.corr', key_resp_8.corr)
    if key_resp_8.keys != None:  # we had a response
        trials_2.addData('key_resp_8.rt', key_resp_8.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim2"-------
    t = 0
    stim2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(pawPatrol2)
    key_resp_10 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim2Components = [image_3, key_resp_10]
    for thisComponent in stim2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim2"-------
    while continueRoutine:
        # get current time
        t = stim2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_10* updates
        if t >= 0.0 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '1', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys.extend(theseKeys)  # storing all keys
                key_resp_10.rt.append(key_resp_10.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['2'])): 
                    if len(key_resp_10.keys) == 1:
                        key_resp_10_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_10_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim2"-------
    for thisComponent in stim2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_10.keys',key_resp_10.keys)
    trials_2.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        trials_2.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_11 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_11]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_11* updates
        if t >= 0.0 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        if key_resp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_11.keys.extend(theseKeys)  # storing all keys
                key_resp_11.rt.append(key_resp_11.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['4'])): 
                    if len(key_resp_11.keys) == 1:
                        key_resp_11_corr = 1
                        trialCorrect = 1
                        trials_2.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_11_corr = 0
                        trialCorrect = 0
                        trials_2.addData('trialCorrect',trialCorrect)
                    continueRoutine = False
                else:
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_11.keys',key_resp_11.keys)
    trials_2.addData('key_resp_11.corr', key_resp_11.corr)
    if key_resp_11.keys != None:  # we had a response
        trials_2.addData('key_resp_11.rt', key_resp_11.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 10 repeats of 'trials_3'



# ------Prepare to start Routine "break_2"-------
t = 0
break_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(120.000000) #How long the screen will be up for 
# update component parameters for each repeat
break_2Response = event.BuilderKeyResponse()
# keep track of which components have finished
break_2Components = [text_7, break_2Response]
for thisComponent in break_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "break_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
            
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        #keep track of start time/frame for later 
        text_7.tStart = t 
        text_7.frameNStart = frameN #extract frame index
        text_7.setAutoDraw(True)
    frameRemains = 0.0 + 120.0- win.monitorFramePeriod * 0.75 #most of one frame period left
    if text_7.status == STARTED and t >= frameRemains: 
        text_7.setAutoDraw(False) 
            
     # *break_2Response* updates
    if t >= 0.0 and break_2Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        break_2Response.tStart = t
        break_2Response.frameNStart = frameN  # exact frame index
        break_2Response.status = STARTED 
        # keyboard checking is just startgin
    frameRemains = 0.0 + 120- win.monitorFramePeriod * 0.75  # most of one frame period left
    if break_2Response.status == STARTED and t >= frameRemains:
        break_2Response.status == STOPPED
    if break_2Response.status == STARTED: 
        theseKeys = event.getKeys(keyList=['space', 'enter', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
                
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "instructions2"-------
t = 0
instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructions2Components = [text_5, text_6]
for thisComponent in instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_5.status == STARTED and t >= frameRemains:
        text_5.setAutoDraw(False)
    
    # *text_6* updates
    if t >= 1 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# -------Setting Up Repition-------
# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pawStimuli.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
            
    # ------Prepare to start Routine "stim1"-------
    t = 0
    stim1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    pos1.setImage(pawPatrol1)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim1Components = [pos1, key_resp_9]
    for thisComponent in stim1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim1"-------
    while continueRoutine:
        # get current time
        t = stim1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pos1* updates
        if t >= 0.0 and pos1.status == NOT_STARTED:
            # keep track of start time/frame for later
            pos1.tStart = t
            pos1.frameNStart = frameN  # exact frame index
            pos1.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if pos1.status == STARTED and t >= frameRemains:
            pos1.setAutoDraw(False)
        if pos1.status == STARTED:  # only update if drawing
            pos1.setPos((0, 0), log=False)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['1'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim1"-------
    for thisComponent in stim1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim3"-------
    t = 0
    stim3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_4.setImage(pawPatrol3)
    key_resp_7 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim3Components = [image_4, key_resp_9]
    for thisComponent in stim3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim3"-------
    while continueRoutine:
        # get current time
        t = stim3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_4.status == STARTED and t >= frameRemains:
            image_4.setAutoDraw(False)
        
        # *key_resp_7* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['3', '1', '2', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['3'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim3"-------
    for thisComponent in stim3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim2"-------
    t = 0
    stim2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(pawPatrol2)
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim2Components = [image_3, key_resp_9]
    for thisComponent in stim2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim2"-------
    while continueRoutine:
        # get current time
        t = stim2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '1', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['2'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim2"-------
    for thisComponent in stim2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_9]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['4'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_9]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['4'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim2"-------
    t = 0
    stim2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(pawPatrol2)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim2Components = [image_3, key_resp_9]
    for thisComponent in stim2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim2"-------
    while continueRoutine:
        # get current time
        t = stim2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '1', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['2'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_9_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim2"-------
    for thisComponent in stim2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim3"-------
    t = 0
    stim3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_4.setImage(pawPatrol3)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim3Components = [image_4, key_resp_9]
    for thisComponent in stim3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim3"-------
    while continueRoutine:
        # get current time
        t = stim3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_4.status == STARTED and t >= frameRemains:
            image_4.setAutoDraw(False)
        
        # *key_resp_7* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['3', '1', '2', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['3'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim3"-------
    for thisComponent in stim3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_9]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['4'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim2"-------
    t = 0
    stim2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_3.setImage(pawPatrol2)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim2Components = [image_3, key_resp_9]
    for thisComponent in stim2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim2"-------
    while continueRoutine:
        # get current time
        t = stim2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', '1', '3', '4'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['2'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim2"-------
    for thisComponent in stim2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "stim4"-------
    t = 0
    stim4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image_5.setImage(pawPatrol4)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    stim4Components = [image_5, key_resp_9]
    for thisComponent in stim4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stim4"-------
    while continueRoutine:
        # get current time
        t = stim4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (['4'])): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        trialCorrect = 1
                        trials_3.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_5_corr = 0
                        trialCorrect = 0
                        trials_3.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stim4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stim4"-------
    for thisComponent in stim4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_3.addData('key_resp_9.keys',key_resp_9.keys)
    trials_3.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_3.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 10 repeats of 'trials_3'





# ------Prepare to start Routine "break_2"-------
t = 0
break_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(120.000000) #How long the screen will be up for 
# update component parameters for each repeat
break_2Response = event.BuilderKeyResponse()
# keep track of which components have finished
break_2Components = [text_7, break_2Response]
for thisComponent in break_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "break_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
            
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        #keep track of start time/frame for later 
        text_7.tStart = t 
        text_7.frameNStart = frameN #extract frame index
        text_7.setAutoDraw(True)
    frameRemains = 0.0 + 120.0- win.monitorFramePeriod * 0.75 #most of one frame period left
    if text_7.status == STARTED and t >= frameRemains: 
        text_7.setAutoDraw(False) 
            
     # *break_2Response* updates
    if t >= 0.0 and break_2Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        break_2Response.tStart = t
        break_2Response.frameNStart = frameN  # exact frame index
        break_2Response.status = STARTED 
        # keyboard checking is just startgin
    frameRemains = 0.0 + 120- win.monitorFramePeriod * 0.75  # most of one frame period left
    if break_2Response.status == STARTED and t >= frameRemains:
        break_2Response.status == STOPPED
    if break_2Response.status == STARTED: 
        theseKeys = event.getKeys(keyList=['space', 'enter', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
                
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# ------Prepare to start Routine "instructions2"-------
t = 0
instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructions2Components = [text_5, text_6]
for thisComponent in instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_5.status == STARTED and t >= frameRemains:
        text_5.setAutoDraw(False)
    
    # *text_6* updates
    if t >= 1 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=25, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'random.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    # ------Prepare to start Routine "randomStim"-------
    t = 0
    randomStimClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(randomPaw)
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    randomStimComponents = [image, key_resp_9]
    for thisComponent in randomStimComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "randomStim"-------
    while continueRoutine:
        # get current time
        t = randomStimClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + 50.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *key_resp_9* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # AllowedKeys looks like a variable named `allowableKey`
            if not type(allowableKey) in [list, tuple, np.ndarray]:
                if not isinstance(allowableKey, basestring):
                    logging.error('AllowedKeys variable `allowableKey` is not string- or list-like.')
                    core.quit()
                elif not ',' in allowableKey: allowableKey = (allowableKey,)
                else:  allowableKey = eval(allowableKey)
            # keyboard checking is just starting
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=list(allowableKey))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys.extend(theseKeys)  # storing all keys
                key_resp_9.rt.append(key_resp_9.clock.getTime())
                print('you pressed: ')
                print(theseKeys)
                print('correct key was ')
                print(correctKey)
                # was this 'correct'?
                #if (theseKeys) == (correctKey):
                if ((theseKeys) == (correctKey)): 
                #if (key_resp_9.keys == str(u'correctKey')) or (key_resp_9.keys == u'correctKey'):
                    print('you got it right!!!')
                    print('length of response key:')
                    if len(key_resp_9.keys) == 1:
                        key_resp_9_corr = 1
                        print('key resp 9 corr should be 1:')
                        print(key_resp_9_corr)
                        trialCorrect = 1
                        trials_4.addData('trialCorrect',trialCorrect)
                    else: 
                        key_resp_9_corr = 0
                        print('the first element was not right: should be 0')
                        print(key_resp_9_corr)
                        trialCorrect = 0
                        trials_4.addData('trialCorrect',trialCorrect)
                    #key_resp_9.corr = 1
                    continueRoutine = False
                else:
                    #key_resp_9.corr = 0
                    continueRoutine = True
                # a response ends the routine
                #continueRoutine = True
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in randomStimComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "randomStim"-------
    for thisComponent in randomStimComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys=None
        # was no response the correct answer?!
        if str(u'correctKey').lower() == 'none':
           key_resp_9.corr = 1  # correct non-response
        else:
           key_resp_9.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_4.addData('key_resp_9.keys',key_resp_9.keys)
    trials_4.addData('key_resp_9.corr', key_resp_9.corr)
    if key_resp_9.keys != None:  # we had a response
        trials_4.addData('key_resp_9.rt', key_resp_9.rt)
    # the Routine "randomStim" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stimBlank"-------
    t = 0
    stimBlankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    blankImage.setImage(blank)
    # keep track of which components have finished
    stimBlankComponents = [blankImage]
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "stimBlank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = stimBlankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blankImage* updates
        if t >= 0.0 and blankImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            blankImage.tStart = t
            blankImage.frameNStart = frameN  # exact frame index
            blankImage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blankImage.status == STARTED and t >= frameRemains:
            blankImage.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stimBlankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stimBlank"-------
    for thisComponent in stimBlankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 25 repeats of 'trials_2'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [goodJob, key_resp_10]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodJob* updates
    if t >= 0.0 and goodJob.status == NOT_STARTED:
        # keep track of start time/frame for later
        goodJob.tStart = t
        goodJob.frameNStart = frameN  # exact frame index
        goodJob.setAutoDraw(True)
    frameRemains = 0.0 + 10.- win.monitorFramePeriod * 0.75  # most of one frame period left
    if goodJob.status == STARTED and t >= frameRemains:
        goodJob.setAutoDraw(False)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['enter', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
