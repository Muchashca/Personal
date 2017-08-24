import maya.cmds as cmds
import maya.mel as mel

def jntChainFromSelection(*args):
    sel = cmds.ls(sl = True)

    if sel != []:
        jnts = []
        for index, s in enumerate(sel):
            cmds.select(cl = True)
            selTran = cmds.xform(s, q = True, t = True, ws = True)
            jnts.append(cmds.joint())
            cmds.xform(jnts[index], t = selTran, ws = True)
            cmds.select(s)
            cmds.makeIdentity(jnts[index], a = True, s = True, r = True, t = True)
            if index != 0:
                cmds.parent(jnts[index], jnts[index -1])
            cmds.select(jnts[0])
            cmds.joint(e = True, oj = 'xyz', sao = 'yup', ch = True, zso = True)
    else:
        cmds.warning("A selection is needed for this tool.")

def jointOrientModeToggle(*args):
    sel = cmds.ls(sl = True)

    if sel != []:
        for s in sel:
            lraVis = cmds.getAttr(s + '.displayLocalAxis', k = True)
            lraOn = cmds.getAttr(s + '.displayLocalAxis')
            joX = cmds.getAttr(s + '.jointOrientX', k = True)
            joY = cmds.getAttr(s + '.jointOrientY', k = True)
            joZ = cmds.getAttr(s + '.jointOrientZ', k = True)
            
            if lraVis == True:
                cmds.setAttr(s + '.displayLocalAxis', k = False)
            else:
                cmds.setAttr(s + '.displayLocalAxis', k = True)
                
            if lraOn == True:
                cmds.setAttr(s + '.displayLocalAxis', False)
            else:
                cmds.setAttr(s + '.displayLocalAxis', True)
                
            if joX == True:
                cmds.setAttr(s + '.jointOrientX', k = False)
            else:
                cmds.setAttr(s + '.jointOrientX', k = True)    

            if joY == True:
                cmds.setAttr(s + '.jointOrientY', k = False)
            else:
                cmds.setAttr(s + '.jointOrientY', k = True)
                
            if joX == True:
                cmds.setAttr(s + '.jointOrientZ', k = False)
            else:
                cmds.setAttr(s + '.jointOrientZ', k = True)
    else:
        cmds.warning("A selection is needed for this tool.")
        
def jointOrientModeOn(*args):
    sel = cmds.ls(sl = True)

    if sel != []:
        for s in sel:
            lraVis = cmds.getAttr(s + '.displayLocalAxis', k = True)
            lraOn = cmds.getAttr(s + '.displayLocalAxis')
            joX = cmds.getAttr(s + '.jointOrientX', k = True)
            joY = cmds.getAttr(s + '.jointOrientY', k = True)
            joZ = cmds.getAttr(s + '.jointOrientZ', k = True)
            
            cmds.setAttr(s + '.displayLocalAxis', k = True)
            cmds.setAttr(s + '.displayLocalAxis', True)
            cmds.setAttr(s + '.jointOrientX', k = True)    
            cmds.setAttr(s + '.jointOrientY', k = True)
            cmds.setAttr(s + '.jointOrientZ', k = True)
    else:
        cmds.warning("A selection is needed for this tool.")

def jointOrientModeOff(*args):
    sel = cmds.ls(sl = True)

    if sel != []:
        for s in sel:
            lraVis = cmds.getAttr(s + '.displayLocalAxis', k = True)
            lraOn = cmds.getAttr(s + '.displayLocalAxis')
            joX = cmds.getAttr(s + '.jointOrientX', k = True)
            joY = cmds.getAttr(s + '.jointOrientY', k = True)
            joZ = cmds.getAttr(s + '.jointOrientZ', k = True)
            
            cmds.setAttr(s + '.displayLocalAxis', k = False)
            cmds.setAttr(s + '.displayLocalAxis', False)
            cmds.setAttr(s + '.jointOrientX', k = False)    
            cmds.setAttr(s + '.jointOrientY', k = False)
            cmds.setAttr(s + '.jointOrientZ', k = False)
    else:
        cmds.warning("A selection is needed for this tool.")

def selNextSkinJnt(*args):
    sel = cmds.ls(sl = True)
    try:
        print number
    except:
        number = 0
    if sel != []:
        for s in sel:
            skin = mel.eval('findRelatedSkinCluster '+ s)
            print skin
            if skin != '':
                print "Accessed"
                locked = []
                unlocked = []
                jntList = cmds.skinCluster(skin, q = True, inf = True)
                for jnt in jntList:
                    if cmds.getAttr(jnt + '.liw') == True:
                        locked.append(jnt)
                    if cmds.getAttr(jnt + '.liw') == False:
                        unlocked.append(jnt)
                print number
                
                if len(unlocked) == number:
                    print "First"
                    number = 0
                    mel.eval('selInfJnt("' + unlocked[0] + '");')
                    print unlocked[number]
                    number += 1
                else:
                    print "Second"
                    mel.eval('selInfJnt("' + unlocked[number] + '");')
                    print unlocked[number]
                    number += 1
    
def selectHi(*args):
    sel = cmds.ls(sl = True)
    if sel != []:
        cmds.select(sel[0], hi = True)

def clickOne(outliner, button, nodeList, *args):
    retrievedList = nodeList()
    fixed = []
    for r in retrievedList:
        name = str(r).replace("[u'", "").replace("']", "")
        fixed.append(name)
    retrievedList = fixed
    cmds.nodeOutliner(outliner, e = True, rma = True)
    for r in retrievedList:
        cmds.nodeOutliner(outliner, e = True, a = r)
    cmds.button(button, e = True, bgc = (.8, .8, .8), c = lambda x: clickTwo(outliner, button, nodeList))
    cmds.select(cl = True)

def clickTwo(outliner, button, nodeList, *args):
    retrievedList = nodeList()
    fixed = []
    for r in retrievedList:
        name = str(r).replace("[u'", "").replace("']", "")
        fixed.append(name)
    retrievedList = fixed
    cmds.nodeOutliner(outliner, e = True, rma = True)
    for r in retrievedList:
        cmds.nodeOutliner(outliner, e = True, a = r)
    cmds.button(button, e = True, bgc = (.4, .4, .4), c = lambda x: clickOne(outliner, button, nodeList))
    cmds.select(cl = True)
    for r in retrievedList:
        cmds.select(r, add = True)

def SASave(outliner, loadButton, *args):
    list = cmds.nodeOutliner(outliner, q = True, nd = True)
    print list
    cmds.button(loadButton, e = True, en = True)
    SASave.saved = list

def SALoad(outliner, *args):
    print SASave.saved
    cmds.nodeOutliner(outliner, e = True, rma = True)
    for s in SASave.saved:
        cmds.nodeOutliner(outliner, e = True, a = s)
    
def SAAdd(outliner, *args):
    sel = cmds.ls(sl = True)
    for s in sel:
        cmds.nodeOutliner(outliner, e = True, a = s)   
   
def SARemove(outliner, *args):
    sel = cmds.ls(sl = True)
    for s in sel:
        cmds.nodeOutliner(outliner, e = True, rm = s)   
        
def SAClear(outliner, *args):
    cmds.nodeOutliner(outliner, e = True, rma = True)   
            
def populateGeoList():
    geoList = cmds.ls(typ = 'mesh')
    parList = []
    for g in geoList:
        par = cmds.listRelatives(g, p = True)
        parList.append(par)
    return parList
    
def populateGeoShapeList():
    geoShapeList = cmds.ls(typ = 'mesh')
    return geoShapeList
    
def populateCurveList():
    curveList = cmds.ls(typ = 'curveShape')
    parList = []
    for c in curveList:
        par = cmds.listRelatives(c, p = True)
        parList.append(par)
    return parList

def populateCurveShapeList():
    curveShapeList = cmds.ls(typ = 'curveShape')
    return curveShapeList

def populateGroupList():
    sel = cmds.ls()
    groups = []
    for s in sel:
        isGroup = True
        transform = cmds.ls(s, typ = 'transform')
        if not transform:
            isGroup = False
        ik = cmds.ls(s, typ = 'ikHandle')
        if ik:
            isGroup = False
        fl = cmds.ls(s, typ = 'fluidEmitter')
        if fl:
            isGroup = False
        ikEff = cmds.ls(s, typ = 'ikEffector')
        if ikEff:
            isGroup = False
        shape = cmds.listRelatives(s, s = True)
        if shape:
            isGroup = False
        isJoint = cmds.ls(s, typ = 'joint')
        if isJoint:
            isGroup = False
        isConstraint = cmds.ls(s, showType = True)
        if len(isConstraint) > 1:
            if 'Constraint' in isConstraint[1]:
                isGroup = False
        if isGroup == True:
            groups.append(s)
    return groups

def populateJointList():
    jointList = cmds.ls(typ = 'joint')
    return jointList

def populateConstraintList():
    parents = cmds.ls(typ = 'parentConstraint')
    points = cmds.ls(typ = 'pointConstraint')
    orients = cmds.ls(typ = 'orientConstraint')
    scales = cmds.ls(typ = 'scaleConstraint')
    aims = cmds.ls(typ = 'aimConstraint')
    pvs = cmds.ls(typ = 'poleVectorConstraint')
    constraintList = []
    constraintList.extend(parents)
    constraintList.extend(points)
    constraintList.extend(orients)
    constraintList.extend(scales)
    constraintList.extend(aims)
    constraintList.extend(pvs)
    return constraintList
    
def populateLightList():
    lightList = cmds.ls(typ = 'light')
    return lightList
    
def populateMaterialList():
    materialList = cmds.ls(mat = True)
    return materialList

def sceneAnalyzerCreate(*args):
    geoList = populateGeoList
    geoShapeList = populateGeoShapeList
    curveList = populateCurveList
    curveShapeList = populateCurveShapeList
    groupList = populateGroupList
    jointList = populateJointList
    constraintList = populateConstraintList
    lightList = populateLightList
    materialList = populateMaterialList

    if cmds.window('SceneOutliner', ex = True):
        cmds.deleteUI('SceneOutliner')

    SAWindow = cmds.window('SceneOutliner', title = 'Scene Analyzer', wh = (300, 450))
    SAForm = cmds.formLayout(numberOfDivisions=100)

    sceneAnalyzer = cmds.nodeOutliner(showInputs=True, addCommand='print("%node \\n")', ms = True, si = False)

    butGeo = cmds.button(l = 'Geometry', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butGeo, geoList))
    butGeoShape = cmds.button(l = 'Geo Shapes', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butGeoShape, geoShapeList))
    butCurve = cmds.button(l = 'Curves', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butCurve,curveList))
    butCurveShape = cmds.button(l = 'Curve Shapes', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butCurveShape, curveShapeList))
    butGroup = cmds.button(l = 'Groups', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butGroup, groupList))
    butJoint = cmds.button(l = 'Joints', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butJoint, jointList))
    butConstraint = cmds.button(l = 'Constraints', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butConstraint, constraintList))
    butLight = cmds.button(l = 'Lights', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butLight, lightList))
    butMaterial = cmds.button(l = 'Materials', bgc = (.4, .4, .4), c = lambda x: clickOne(sceneAnalyzer, butMaterial, materialList))

    butSave = cmds.button(l = 'Save', bgc = (.4, .4, .4), c = lambda x: SASave(sceneAnalyzer, butLoad))
    butLoad = cmds.button(l = 'Load', bgc = (.4, .4, .4), c = lambda x: SALoad(sceneAnalyzer), en = False)

    butAdd = cmds.button(l = 'Add', bgc = (.4, .4, .4), c = lambda x: SAAdd(sceneAnalyzer))
    butRemove = cmds.button(l = 'Remove', bgc = (.4, .4, .4), c = lambda x: SARemove(sceneAnalyzer))
    butClear = cmds.button(l = 'Clear', bgc = (.4, .4, .4), c = lambda x: SAClear(sceneAnalyzer))

    cmds.nodeOutliner(sceneAnalyzer, e = True, sc = 'selectionSynchronize("' + sceneAnalyzer + '")')
    sceneControl = cmds.nodeOutliner(showInputs=True, addCommand='print("%node \\n")', ms = True, si = False)
    cmds.formLayout(SAForm, e = True, attachForm = [(sceneAnalyzer, 'top', 5), (sceneAnalyzer, 'right', 5), (sceneAnalyzer, 'bottom', 5)], attachPosition = (sceneAnalyzer, 'left', 5, 40))
    cmds.formLayout(SAForm, e = True, attachForm = [(butGeo, 'left', 5),  (butGeo, 'top', 5)], attachPosition = (butGeo, 'right', 5, 40), attachControl = (butGeo, 'bottom', 5, butGeoShape))
    cmds.formLayout(SAForm, e = True, attachForm = (butGeoShape, 'left', 5), attachPosition = [(butGeoShape, 'right', 5, 40), (butGeoShape, 'top', 5, 9)], attachControl = (butGeoShape, 'bottom', 5, butCurve))
    cmds.formLayout(SAForm, e = True, attachForm = (butCurve, 'left', 5), attachPosition = [(butCurve, 'right', 5, 40), (butCurve, 'top', 5, 18)], attachControl = (butCurve, 'bottom', 5, butCurveShape))
    cmds.formLayout(SAForm, e = True, attachForm = (butCurveShape, 'left', 5), attachPosition = [(butCurveShape, 'right', 5, 40), (butCurveShape, 'top', 5, 27)], attachControl = (butCurveShape, 'bottom', 5, butGroup))
    cmds.formLayout(SAForm, e = True, attachForm = (butGroup, 'left', 5), attachPosition = [(butGroup, 'right', 5, 40), (butGroup, 'top', 5, 36)], attachControl = (butGroup, 'bottom', 5, butJoint))
    cmds.formLayout(SAForm, e = True, attachForm = (butJoint, 'left', 5), attachPosition = [(butJoint, 'right', 5, 40), (butJoint, 'top', 5, 45)], attachControl = (butJoint, 'bottom', 5, butConstraint))
    cmds.formLayout(SAForm, e = True, attachForm = (butConstraint, 'left', 5), attachPosition = [(butConstraint, 'right', 5, 40), (butConstraint, 'top', 5, 54)], attachControl = (butConstraint, 'bottom', 5, butLight))
    cmds.formLayout(SAForm, e = True, attachForm = (butLight, 'left', 5), attachPosition = [(butLight, 'right', 5, 40), (butLight, 'top', 5, 63)], attachControl = (butLight, 'bottom', 5, butMaterial))
    cmds.formLayout(SAForm, e = True, attachForm = (butMaterial, 'left', 5), attachPosition = [(butMaterial, 'right', 5, 40), (butMaterial, 'top', 5, 72), (butMaterial, 'bottom', 5, 81)])

    cmds.formLayout(SAForm, e = True, attachForm = (butSave, 'left', 5), attachPosition = (butSave, 'right', 5, 20), attachControl = (butSave, 'bottom', 5, butAdd))
    cmds.formLayout(SAForm, e = True, attachPosition = [(butLoad, 'left', 5, 20), (butLoad, 'right', 5, 40)], attachControl = (butLoad, 'bottom', 5, butRemove))

    cmds.formLayout(SAForm, e = True, attachForm = (butAdd, 'left', 5), attachPosition = (butAdd, 'right', 5, 20), attachControl = (butAdd, 'bottom', 5, butClear))
    cmds.formLayout(SAForm, e = True, attachPosition = [(butRemove, 'left', 5, 20), (butRemove, 'right', 5, 40)], attachControl = (butRemove, 'bottom', 5, butClear))
    cmds.formLayout(SAForm, e = True, attachForm = [(butClear, 'bottom', 5), (butClear, 'left', 5)], attachPosition = (butClear, 'right', 5, 40))

    cmds.showWindow(SAWindow)
    
def connectTRSn(attrs, *args):
    sel = cmds.ls(sl = True)
    if len(sel) < 2:
        cmds.warning('This tool requires at least two things be selected.')
    else:
        sel1 = sel[0]
        sel2 = sel[1]
        if 't' in attrs:
            cmds.connectAttr(sel1 + '.translate', sel2 + '.translate')
        if 'r' in attrs:
            cmds.connectAttr(sel1 + '.rotate', sel2 + '.rotate')
        if 's' in attrs:
            cmds.connectAttr(sel1 + '.scale', sel2 + '.scale')
        if 'v' in attrs:
            cmds.connectAttr(sel1+ '.visibility', sel2 + '.visibility')
         
def makeCtrl(makeConstraint):
    initial = cmds.ls(sl = True)
    if len(initial) > 0:
        sel = initial[0]
        selTran = cmds.xform(sel, q = True, t = True, ws = True)
        selRot = cmds.xform(sel, q = True, ro = True, ws = True)
        selRad = cmds.getAttr(sel + '.radius')
        ctrlRad = selRad * 2.5
        ctrlName = str(sel) + '_Ctrl'
        grpName =  str(sel) + '_Off'
        cmds.group(em = True, n = grpName)
        cmds.circle(nr = (1, 0, 0), n = ctrlName)
        cmds.parent(ctrlName, grpName)
        cmds.xform(grpName, t = selTran, ws = True)
        cmds.xform(grpName, ro = selRot, ws = True)
        cmds.scale(ctrlRad, ctrlRad, ctrlRad, ctrlName)
        cmds.makeIdentity(ctrlName, apply=True, s=1, n=2 )
        cmds.delete(ctrlName, ch = True)
        if makeConstraint == True:
            cmds.parentConstraint(ctrlName, sel, mo = False)
        return grpName, ctrlName
    else:
        cmds.warning('This tool requires at least one joint be selected.')