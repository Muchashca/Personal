# Creates a locator and group above each selected object

import maya.cmds as mc

def locGrpEach():
    
    removeSuff = 1
    
    sel = mc.ls (sl = True)
    for obj in sel:
        
        if removeSuff == 1:
            
            objShort = obj.replace ('_JNT', '')
            objShort = objShort.replace ('_Jnt', '')
            objShort = objShort.replace ('_Bnd', '')
            objShort = objShort.replace ('_BND', '')
            objShort = objShort.replace ('_Jt', '')
            objShort = objShort.replace ('_CON', '')
            objShort = objShort.replace ('_Con', '')
            objShort = objShort.replace ('_CTRL', '')
            objShort = objShort.replace ('_Ctrl', '')
            objShort = objShort.replace ('_LOC', '')
            objShort = objShort.replace ('_Loc', '')
            objShort = objShort.replace ('_GRP', '')
            objShort = objShort.replace ('_Grp', '')
            
        else:
            objShort = obj
        
        par = mc.listRelatives (obj, p = True)
        
        loc = mc.spaceLocator (p = (0,0,0), n = '%s_LOC' %objShort)
        grp = mc.group (em = True, w = True, n = '%s_GRP' %objShort)
        
        mc.parent (loc, grp)
        
        if par != None:
            mc.parent (grp, par)
        
        cnst = mc.parentConstraint (obj, grp)
        mc.delete (cnst)
        mc.makeIdentity (grp, a = True, s = 1)
        
        mc.parent (obj, loc)
        mc.setAttr ('%sShape.visibility' %loc[0], 0)
        
locGrpEach()