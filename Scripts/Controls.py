from pymel.core import *

import pymel.core as pm
from pymel import *

#Start program > Make or have selection > check and save selection > show UI > Apply selection to control creation > if fork, offer
#selection, if not, follow to next joint, or end

def selectionCheck():   
    selectedObject = ls(sl=True, tr=True)
    objectNum = len(selectedObject)
    objectName = 'A'
    groupName = 'B'
    offName = 'C'
    selName = 'D'
    selOK = False
    if objectNum == 0:
        winText = "Nothing Selected"
        selOk = False
    elif objectNum == 1:
        selName = selectedObject[0]
        print("selname " + selName)
        winText = selectedObject
        if 'Jnt' in selName:
            groupName = selName.replace("Jnt", "Ctrl")
            print("groupName " + groupName)
            offName = selName.replace("Jnt", "Off")
            print("offname " + offName)
        else:
            groupName = selName + '_Ctrl'
            offName = selName + '_Off'
        objectName = selName + '_Piece_01'
        selOk = True
    elif objectNum > 1:
        winText = "Too many things selected"
        selOk = False
    uiCreate(winText, objectName, selOk)

def uiCreate(selText, obName, selectionOk):
    objectName = obName
    selOk = selectionOk
    if pm.window('fkCtrlMaker', exists=True):
        pm.deleteUI('fkCtrlMaker')
    
    window = pm.window('fkCtrlMaker', title = 'Fk Ctrl Maker', iconName='FK', widthHeight=(400, 200))
    
    if pm.columnLayout('winLayout', exists=True):
        pm.deleteUI('winLayout')
    
    winLayout = pm.columnLayout('winLayout', adjustableColumn=True )
    pm.separator('sep1', height=10, style='double' )     
    windowText = pm.text(selText, p = winLayout, al = 'center')    
    pm.separator( height=20, style='double' )
    pm.button( label='Basic Circle', command='makeShape("BCircle", objectName, groupName, offName)', en = selOk)
    pm.button( label='Detailed Circle', command='makeShape("DCircle", objectName, groupName, offName)', en = selOk)
    pm.button( label='Basic Square', command='buttonPressed()', en = selOk)
    pm.button( label='Close', command=('pm.deleteUI(\"' + window + '\", window=True)') )
    pm.setParent( '..' )
    pm.showWindow( window )
    winJob = pm.scriptJob(kws = True, p = window, e = ("SelectionChanged", selectionCheck))
    
    #def buttonPressed():
    #makeShape('DCircle', objectName, groupName) ("DCircle", objectName, groupName, offName)


def makeShape(shape, object, transform, offsetName):
    select (cl = True)
    shapes = []
    shapeTr = []
    number = 0
    pieceName = object
    offName = offsetName
    group(n = offName)
    if shape == 'DCircle':
        group(n=transform)
        shapes.append(circle( nr=(0, 1, 0), c=(0, 0, 0), n=(pieceName)))
        move(0, .25, 0)
        shapes.append(circle( nr=(0, 1, 0), c=(0, 0, 0), n=(pieceName)))
        move(0, -.25, 0)
        shapes.append(curve( p=[(1, -.25, 0), (1, .25, 0)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(-1, -.25, 0), (-1, .25, 0)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(0, -.25, 1), (0, .25, 1)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(0, -.25, -1), (0, .25, -1)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(1, -.25, 0), (1, .25, 0)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, -10)
        shapes.append(curve( p=[(-1, -.25, 0), (-1, .25, 0)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, -10)
        shapes.append(curve( p=[(0, -.25, 1), (0, .25, 1)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, -10)
        shapes.append(curve( p=[(0, -.25, -1), (0, .25, -1)], k=[0,1], d=1, n=(pieceName)))
        rotate(0, 0, -10)
        
        for s in shapes:
            select (s, add=True)
                    
        makeIdentity( apply=True )
        delete( ch=True )
        pickWalk(d = 'down')

        shapesSel = pm.ls(sl=True, s=True)
        
        for s in shapesSel:
            parent(s, transform, s = True, r = True)
        
    if shape == 'BCircle':
        shapes.append(circle( nr=(0, 1, 0), c=(0, 0, 0), n=(groupName)))
        
        
        
        #for s in shapes:
         #   select (s, add=True)
'''
selectedObject = ls(sl=True, tr=True)
objectNum = len(selectedObject)
print(objectNum)
if objectNum == 1:
    print("it's true")
    objectName = selectedObject[0] + '_Piece_01'
    if 'Jnt' in selectedObject[0]:
        groupName = selectedObject[0].replace("Jnt", "Ctrl")
        offName = selectedObject[0].replace("Jnt", "Off")
    else:
        groupName = selectedObject[0] + '_Ctrl'
        offName = selectedObject[0] + '_Off'
else:
    print("it's false")
    objectName = 'A'
    groupName = 'B'
    offName = 'C'
'''

selectionCheck()