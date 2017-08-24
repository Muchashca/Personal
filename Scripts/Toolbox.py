from pymel.core import *
import pymel.core as pm
from functools import partial

#Start program > Make or have selection > check and save selection > show UI > Apply selection to control creation > if fork, offer
#selection, if not, follow to next joint, or end

def selectionCheck():   
    selectedObject = ls(sl=True, tr=True)
    objectNum = len(selectedObject)
    localNameList = ['winText', 'selName', 'grpName', 'offName', False, 'pieceName']
    localNameList[4] = False
    if objectNum == 0:
        localNameList[0] = "Nothing Selected"
        localNameList[4] = False
    elif objectNum == 1:
        localNameList[1] = selectedObject[0]
        localNameList[0] = selectedObject
        if 'Jnt' in localNameList[1]:
            localNameList[2] = localNameList[1].replace("Jnt", "Ctrl")
            localNameList[3] = localNameList[1].replace("Jnt", "Off")
        else:
            localNameList[2] = localNameList[1] + '_Ctrl'
            localNameList[3] = localNameList[1] + '_Off'
        localNameList[5] = localNameList[1] + '_Piece_01'
        localNameList[4] = True
    elif objectNum > 1:
        localNameList[0] = "Too many things selected"
        localNameList[4] = False
    return localNameList

def mainUi(nameList):
    #localNameList = ['winText', 'selName', 'grpName', 'offName', False, 'pieceName']
        
    selText = nameList[0]
    objectName = nameList[1]
    selOk = nameList[4]
    
    if pm.window('toolbox', exists=True):
        pm.deleteUI('toolbox')
    
    window = pm.window('toolbox', title = 'Toolbox', iconName='FK', widthHeight=(400, 500))
    
    if pm.columnLayout('winLayout', exists=True):
        pm.deleteUI('winLayout')
    
    winLayout = pm.columnLayout('winLayout', adjustableColumn=True )
    pm.separator('sep1', height=10, style='double' )     
    windowText = pm.text(selText, p = winLayout, al = 'center')    
    pm.separator( height=20, style='double' )
    pm.button( label='Make Control', command=partial(ctrlUi, nameList))
    pm.button( label='Delete History', command = delHist)
    pm.button( label='Delete Non-Deformer History', command = delNonDefHist)
    pm.button( label='Freeze Transformations', command = freezeTrans)
    pm.button( label='Group All', command = groupSel)
    pm.button( label='Sequential Renamer', command = seqRename, en = False)
    pm.button( label='Done', command=('pm.deleteUI(\"' + window + '\", window=True)') )
    pm.setParent( '..' )
    pm.showWindow( window )
    winJob = pm.scriptJob(kws = True, p = window, e = ("SelectionChanged", main))
      

def shapeUi(nameList):
    #localNameList = ['winText', 'selName', 'grpName', 'offName', False, 'pieceName']

    selText = nameList[0]
    objectName = nameList[1]
    selOk = nameList[4]
    
    if pm.window('fkCtrlMaker', exists=True):
        pm.deleteUI('fkCtrlMaker')
    
    window = pm.window('fkCtrlMaker', title = 'Fk Ctrl Maker', iconName='FK', widthHeight=(400, 300))
    
    if pm.columnLayout('winLayout', exists=True):
        pm.deleteUI('winLayout')
    
    winLayout = pm.columnLayout('winLayout', adjustableColumn=True )
    pm.separator('sep1', height=10, style='double' )     
    windowText = pm.text(selText, p = winLayout, al = 'center')    
    pm.separator( height=20, style='double' )
    pm.button( label='Basic Circle', command=partial(BCircle, nameList), en = selOk)
    pm.button( label='Detailed Circle', command=partial(DCircle, nameList), en = selOk)
    pm.button( label='Basic Square', command=partial(BSquare, nameList), en = selOk)
    pm.button( label='Done', command=('pm.deleteUI(\"' + window + '\", window=True)') )
    pm.setParent( '..' )
    pm.showWindow( window )
    winJob = pm.scriptJob(kws = True, p = window, e = ("SelectionChanged", shapeMain))
  
def delHist(*args):
    sel = ls(sl=True, tr=True)
    if len(sel) >= 1:
        for s in sel:
            delete(ch = True)
    else:
        print("No Selection")
        
def delNonDefHist(*args):
    sel = ls(sl=True, tr=True)
    if len(sel) >= 1:
        for s in sel:
            bakePartialHistory(ppt = True)
    else:
        print("No Selection")        

def freezeTrans(*args):
    sel = ls(sl=True, tr=True)
    if len(sel) >= 1:
        for s in sel:
            makeIdentity(t = True, r = True, s = True, jo = True)
    else:
        print("No Selection")
        
def groupSel(*args):
    sel = ls(sl=True, tr=True)
    if len(sel) >= 1:
        for s in sel:
            select(s)
            tempName = s + '_Grp'
            group(r = True, name = tempName)
    else:
        print("No Selection")
        
def printTest(*args):
    print(args)
        
def seqRename(*args):
    sel = pm.ls(sl = True)
    selNum = len(sel)
    
    if pm.window('seqRename', exists=True):
        pm.deleteUI('seqRename')
        
    window = pm.window('seqRename', title = 'Sequential Renamer', iconName='Rename', widthHeight=(400, 300))    
    pm.showWindow( window )
    layout = pm.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
    t1 = pm.text(label = 'Prefix:  ', p = layout)
    tf1 = pm.textField(p = layout)
    t2 = pm.text(label = 'Object Name:  ', p = layout)
    tf2 = pm.textField(p = layout)
    t3 = pm.text(label = 'Suffix:  ', p = layout)
    tf3 = pm.textField(p = layout)
    pm.button( label='Submit', command=partial(printTest, tf3), en = False)
    #pm.rename (sel[0], tf3)
    
def ctrlUi(nameList, holder):
    shapeUi(nameList)
        
def BCircle(nameList, holder):
    name = "BCircle"
    listed = nameList
    makeShape(listed, name)
    
def DCircle(nameList, holder):
    name = "DCircle"
    listed = nameList
    makeShape(listed, name)
    
def BSquare(nameList, holder):
    name = "BSquare"
    listed = nameList
    makeShape(listed, name)
    
def makeShape(namesList, shape):
    #localNameList = ['winText', 'selName', 'grpName', 'offName', False, 'pieceName']
    print(namesList)
    
    shapes = []
    
    select (cl = True)
    if shape == 'DCircle':
        group(n=namesList[2])
        shapes.append(circle( nr=(0, 1, 0), c=(0, 0, 0), n=(namesList[5])))
        move(0, .25, 0)
        shapes.append(circle( nr=(0, 1, 0), c=(0, 0, 0), n=(namesList[5])))
        move(0, -.25, 0)
        shapes.append(curve( p=[(1, -.25, 0), (1, .25, 0)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(-1, -.25, 0), (-1, .25, 0)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(0, -.25, 1), (0, .25, 1)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(0, -.25, -1), (0, .25, -1)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, 10)
        shapes.append(curve( p=[(1, -.25, 0), (1, .25, 0)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, -10)
        shapes.append(curve( p=[(-1, -.25, 0), (-1, .25, 0)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, -10)
        shapes.append(curve( p=[(0, -.25, 1), (0, .25, 1)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, -10)
        shapes.append(curve( p=[(0, -.25, -1), (0, .25, -1)], k=[0,1], d=1, n=(namesList[5])))
        rotate(0, 0, -10)
        
        for s in shapes:
            select (s, add=True)
                    
        makeIdentity( apply=True )
        delete( ch=True )
        pickWalk(d = 'down')

        shapesSel = pm.ls(sl=True, s=True)
        
        for s in shapesSel:
            parent(s, namesList[2], s = True, r = True)
        
    if shape == 'BCircle':
        shapes.append(circle( nr=(0, 1, 0), c=(0, 0, 0), n=(namesList[2])))
    
    if shape == 'BSquare':
        shapes.append(curve( p=[(1, 0, 1), (-1, 0, 1), (-1, 0, -1), (1, 0, -1), (1, 0, 1)], k=[0,1,2,3,4], d=1, n=(namesList[2])))
 
    select(cl = True)
    group(n = namesList[3])
    tempConstraint = pm.parentConstraint(namesList[1], namesList[3], mo = False)
    delete(tempConstraint)
    parent(namesList[2], namesList[3])
    tempAttr = namesList[2] + '.tx'
    setAttr (tempAttr, 0)
    tempAttr = namesList[2] + '.ty'
    setAttr (tempAttr, 0)
    tempAttr = namesList[2] + '.tz'
    setAttr (tempAttr, 0)
    tempAttr = namesList[2] + '.rx'
    setAttr (tempAttr, 0)
    tempAttr = namesList[2] + '.ry'
    setAttr (tempAttr, 0)
    tempAttr = namesList[2] + '.rz'
    setAttr (tempAttr, 90)
    
    select(namesList[2])
    makeIdentity(apply = True)
        
    select(namesList[1])
    ob = pm.selected()
    for n in ob:
        ro = n.getRotationOrder()
    
    select(namesList[2])
    ctrl = pm.selected()
    for n in ctrl:
        n.setRotationOrder(ro, True)
        
    pm.parentConstraint(namesList[2], namesList[1], mo = False)
    
    select(namesList[1])
    checkPar = listRelatives (p = True)
    hasPar = len(checkPar)
    
    if hasPar != 0:
        print(checkPar[0])
        checkConstraints = pm.parentConstraint(checkPar[0], q=True, tl=True)
        if checkConstraints != []:
            select(namesList[3])
            select(checkConstraints, add = True)
            parent()
    
    select(namesList[1])
    toDo = []
    check = listRelatives (c = True)
    checkPar = listRelatives (p = True)
    hasPar = len(checkPar)

    for c in check:
        select(c)
        childSel = ls(sl=True, tr=True)
        if len(childSel) > 0:    
            child = childSel[0].type()
            if child == 'joint':
                toDo.append(childSel[0])
        else:
            select(cl = True)
     
    leftToDo = len(toDo)
    
    if leftToDo != 0:
        select(toDo[0])
    
    
def checkChildren():
    toDo = []
    check = listRelatives (c = True)
    
def main():
    returnedList = selectionCheck()
    mainUi(returnedList)
    
def shapeMain():
    returnedList = selectionCheck()
    shapeUi(returnedList)
    
main()
