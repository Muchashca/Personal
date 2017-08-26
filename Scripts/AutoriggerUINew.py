import pymel.core as pm
from functools import partial
import pymel.core.datatypes as dt
from itertools import count, izip
import math as math

class spineOptionMenu:
    defaultPos = [(0, 99.702, -2.33), (45.298, 0, 0)]
    defaultRot = [(0, 0, 0), (0, 0, 0)]
    defaultOri = [(90, 0, 90), (0, 0, 0)]
    defaultList = {'pos':defaultPos, 'rot':defaultRot, 'ori':defaultOri}
    pelvisName = 'pelvis_B_Jnt'
    spineName = 'spine'
    grpName = 'Spine_Grp'
    spineGrp = None
    spineJnts = []
    spineMults = []
    spinePmas = []
    spineCount = 4
    spineText = None
    
    def __init__(self, parent, pos, templateGrp, uiMain):
        self.parent = parent
        self.pos = pos
        self.templateGrp = templateGrp
        self.uiMain = uiMain
        with pm.rowColumnLayout(p = self.parent, nc = 1, co = (1, 'both', 5), ro = (1, 'both', 5), cw = (1, 250)):
            spineType = pm.optionMenu(l = 'Spine Type:')
            pm.menuItem(l = 'Advanced Twist')
            pm.menuItem(l = 'Straight Twist')
            pm.menuItem(l = 'FK')
        with pm.rowColumnLayout(p = self.parent, nc = 2, co = [(1, 'both', 5),(2, 'both', 5)], ro = (1, 'both', 5), cw = [(1, 125), (2, 125)]):
            pm.text(l = 'Spine Joints:')
            self.spineText = pm.textField(tx = self.spineCount, cc = self.buildTwistSpine)
        self.buildTwistSpine()

    def buildTwistSpine(self, *args):
        temp = pm.textField(self.spineText, q = True, tx = True)
        self.spineCount = int(temp) + 1
        self.uiMain.updateArmSpineCount(self.spineCount)
        children = pm.listRelatives(self.templateGrp, c = True)
        spineGrps = []
        for c in children:
            if 'Spine' in c.name():
                spineGrps.append(c)
        if spineGrps != []:
            for s in spineGrps:
                pm.delete(s)

        pmas = pm.ls(typ = 'plusMinusAverage')
        for p in pmas:
            if 'spine' and 'Pma' in p.name():
                pm.delete(p)
        mults = pm.ls(typ = 'multiplyDivide')
        for m in mults:
            if 'spine' and 'Mult' in p.name():
                pm.delete(m)
        
        self.spineGrp = pm.createNode('transform', n = self.grpName)
        pm.parent(self.spineGrp, self.templateGrp)
        self.pelvisJnt = pm.joint(n = self.pelvisName, r = True, o = self.defaultList.get('ori')[0], p = self.defaultList.get('pos')[0], ax = self.defaultList.get('rot')[0][0], ay = self.defaultList.get('rot')[0][1], az =  self.defaultList.get('rot')[0][2])
        self.spineJnts = []
        self.spineMults = []
        self.spinePmas = []
        for i in range(1, self.spineCount + 1):
            jntName = '%s_%02d_B_Jnt'%(self.spineName, i)
            pm.select(self.pelvisJnt)
            jnt = pm.joint(n = jntName)
            self.spineJnts.append(jnt)
        self.spineJnts[self.spineCount - 1].tx.set(45.298)
        if self.spineCount > 1:
            for i in range(1, self.spineCount):
                multName = '%s_%02d_Mult'%(self.spineName, i)
                mult = pm.createNode('multiplyDivide', n = multName)
                self.spineMults.append(mult)
                pmaName = '%s_%02d_Pma'%(self.spineName, i)
                pma = pm.createNode('plusMinusAverage', n = pmaName)
                self.spinePmas.append(pma)
            for i in range(0, self.spineCount -1):
                self.pelvisJnt.rx >> self.spineMults[i].input1X
                self.spineJnts[self.spineCount -1].rx >> self.spineMults[i].input1Y
                self.spineMults[i].input2X.set(1-(1.0/self.spineCount*(i + 1)))
                self.spineMults[i].input2Y.set(1.0/self.spineCount*(i + 1))
                self.spineMults[i].outputX >> self.spinePmas[i].input1D[0]
                self.spineMults[i].outputY >> self.spinePmas[i].input1D[1]
                self.spinePmas[i].output1D >> self.spineJnts[i].rx
                self.spineJnts[self.spineCount - 1].tx >> self.spineMults[i].input1Z
                self.spineMults[i].input2Z.set(1.0/self.spineCount*(i + 1))
                self.spineMults[i].outputZ >> self.spineJnts[i].tx
                        
#SCENE.template_Grp.Spine_Grp.tx >> SCENE.top.tx  # connect
#SCENE.template_Grp.Spine_Grp.tx // SCENE.top.tx  # disconnect

            
class armOptionMenu:
    name = None
    layout = None
    column = None
    btn = None
    baseGrp = None
    baseJnt = None
    jntList = []
    basePos = dt.Vector()
    grpName = None
    sideMenu = None
    spineMenu = None
    twistBox = None
    delBtn = None
    spineCount = None
    spineJnt = None
    spineMenuItems = None
    defaultPos = [(4.328, 1.095, -0.721), (-7.772, 0, 0), (-26.792, 0, 0), (-22.493, 0, 0)]
    defaultRot = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    defaultOri = [(0, 0, 162.409), (0, 0, -30.983), (0, 0, 4.779), (0, 0, 0)]
    defaultList = {'pos':defaultPos, 'rot':defaultRot, 'ori':defaultOri}
    armJntListL = []
    armJntListR = []
    nameList = ['clavicle', 'shoulder', 'elbow', 'wrist']
        
    def __init__(self, parent, pos, templateGrp, num, uiMain):
        self.parent = parent
        self.basePos = pos
        self.templateGrp = templateGrp
        self.num = num
        self.name = 'Arm%02d'%(num)
        self.uiMain = uiMain
        self.spineCount = self.uiMain.spineCount
        self.spineMenuItems = []
        self.makeClass()

    def setPos(self, pos):
        if self.baseJnt != None:
            pm.xform(self.baseJnt, ws = True, t = pos)
        else:
            pm.warning('Arm not yet built')
    
    def buildArm(self, *args, **dataList):
        #print self.uiMain.spineList
        check = pm.listRelatives(self.baseGrp, c = True)
        #if check != []:
        #    print 'none'
        if self.armJntListL != []:
            pm.delete(self.armJntListL[0])
            self.armJntListL = []
        if self.armJntListR != []:
            pm.delete(self.armJntListR[0])
            self.armJntListR = []
        if self.baseGrp != None:
            pm.delete(self.baseGrp)
        if dataList.get('pos') != None:
            print 'Pos Have'
        else:
            dataList = self.defaultList
        grpName = '%s_Grp'%(self.name)
        self.baseGrp = pm.createNode('transform', n = grpName)
        pm.parent(self.baseGrp, self.templateGrp)
        pm.select(cl = True)
        if self.sideMenu.getValue() == 'Both':
            self.armJntListL = []
            self.armJntListR = []
            for i in range(0, 4):
                joint = pm.joint(n = '%s_%s_B_Jnt_L'%(self.name, self.nameList[i]), r = True, o = dataList.get('ori')[i], p = dataList.get('pos')[i], ax = dataList.get('rot')[i][0], ay = dataList.get('rot')[i][1], az = dataList.get('rot')[i][2])
                self.armJntListL.append(joint)
            pm.select(cl = True)
            for i in range(0, 4):
                joint = pm.joint(n = '%s_%s_B_Jnt_R'%(self.name, self.nameList[i]), r = True, o = dataList.get('ori')[i], p = dataList.get('pos')[i], ax = dataList.get('rot')[i][0], ay = dataList.get('rot')[i][1], az = dataList.get('rot')[i][2])
                self.armJntListR.append(joint)
            pm.select(cl = True)
            changeSides(self.armJntListR)
        if self.sideMenu.getValue() == 'Left':
            self.armJntListL = []
            self.armJntListR = []
            for i in range(0, 4):
                joint = pm.joint(n = '%s_%s_B_Jnt_L'%(self.name, self.nameList[i]), r = True, o = dataList.get('ori')[i], p = dataList.get('pos')[i], ax = dataList.get('rot')[i][0], ay = dataList.get('rot')[i][1], az = dataList.get('rot')[i][2])
                self.armJntListL.append(joint)
            pm.select(cl = True)
        if self.sideMenu.getValue() == 'Right':
            self.armJntListL = []
            self.armJntListR = []
            pm.select(cl = True)
            for i in range(0, 4):
                joint = pm.joint(n = '%s_%s_B_Jnt_R'%(self.name, self.nameList[i]), r = True, o = dataList.get('ori')[i], p = dataList.get('pos')[i], ax = dataList.get('rot')[i][0], ay = dataList.get('rot')[i][1], az = dataList.get('rot')[i][2])
                self.armJntListR.append(joint)
            pm.select(cl = True)
            changeSides(self.armJntListR)
        if self.sideMenu.getValue() == 'Both':
            pm.parent(self.armJntListL[0], self.baseGrp)
            pm.parent(self.armJntListR[0], self.baseGrp)
        if self.sideMenu.getValue() == 'Left':
            pm.parent(self.armJntListL[0], self.baseGrp)
        if self.sideMenu.getValue() == 'Right':
            pm.parent(self.armJntListR[0], self.baseGrp)
        self.connectToSpine()

        return self.baseGrp, self.baseJnt, self.armJntListL, self.armJntListR

    #print main.armList['Arm01'].templateGrp

    def connectToSpine(self, *args):
        pm.delete(self.baseGrp, cn = True)
        pm.pointConstraint(self.uiMain.spineRef.spineJnts[int(self.spineMenu.getValue()) - 1], self.baseGrp, mo = False)
        pm.orientConstraint(self.uiMain.spineRef.spineJnts[int(self.spineMenu.getValue()) - 1], self.baseGrp, mo = True)
        print self.uiMain.spineRef.spineJnts[int(self.spineMenu.getValue()) - 1]

    def btnSel(self, *args):
        pm.select(cl = True)
        if self.armJntListL != []:
            pm.select(self.armJntListL[0], add = True)
        if self.armJntListR != []:
            pm.select(self.armJntListR[0], add = True)
    
    def btnDel(self, *args):
        pm.delete(self.baseGrp)
        pm.deleteUI(self.layout)
        self.uiMain.armList.pop(self.name)
    
    def makeClass(self):
        layoutName = self.name + 'Layout'
        self.layout = pm.frameLayout(layoutName, borderVisible=True, cll = True, l = self.name, p = self.parent)
        with pm.columnLayout(adj = True, p = self.layout) as self.column:
            pm.button(l = 'Select', p = self.column, c = partial(self.btnSel, self.baseJnt))
            self.sideMenu = pm.optionMenu(l = 'Side', cc = self.buildArm)
            pm.menuItem(l = 'Both')
            pm.menuItem(l = 'Left')
            pm.menuItem(l = 'Right')
            self.spineMenu = pm.optionMenu(l = 'Spine', cc = self.connectToSpine)
            self.setSpineCount(self.uiMain.spineCount)
            self.twistBox = pm.checkBox(l = 'Twist')
            self.delBtn = pm.button(l = 'Delete %s'%(self.name), p = self.column, c = partial(self.btnDel, self.layout, self.baseJnt))
        return self.name, self.layout, self.column, self.btn, self.sideMenu
    
    def setSpineCount(self, num):
        items = pm.optionMenu(self.spineMenu, q = True, ill = True)
        for item in items:
            pm.deleteUI(item)
        self.spineMenuItems = []
        for i in range(0, num):
            newItem = pm.menuItem(p = self.spineMenu, l = (i + 1))
            self.spineMenuItems.append(newItem)
        #self.spineCount = num
        #self.spineCount = self.uiMain.spineCount
        #for i in range(0, self.spineCount):
        #    item = pm.menuItem(l = self.spineCount)
        #    self.spineMenuItems.append(item)        
    
    def spineNumber(self, num):
        num = num
    
    def renameClass(self, num):
        self.name = 'Arm%02d'%(num)
        pm.frameLayout(self.layout, e = True, l = self.name)
        layoutName = self.name + 'Layout'
        self.layout = pm.renameUI(self.layout, layoutName)
        self.baseGrp.rename('Arm%02d_Grp'%(num))
        if self.armJntListL != []:
            self.armJntListL[0].rename('Arm%02d_B_Jnt'%(num))
        if self.armJntListL != []:
            self.armJntListR[0].rename('Arm%02d_B_Jnt'%(num))
        pm.button(self.delBtn, e = True, l = 'Delete Arm%02d'%(num), c = partial(self.btnDel, self.layout, self.baseJnt))
        return self.name, self.layout, self.baseGrp, self.baseJnt, self.delBtn

class uiBase:
    armList = None
    templateGrp = None
    win = None
    form = None
    layout = None
    armBaseColumn = None
    armColumn = None
    armList = {}
    spineRef = None
    spineList = []
    spineLayout = None
    armLayout = None
    spineCount = None
    spineText = None
    
    def __init__(self):
        self.findTemplate()
        self.spineCount = 5
        print 'Ui Created'
        if pm.window('ehAutoRigger2', exists = True):
            pm.deleteUI('ehAutoRigger2')

        with pm.window('ehAutoRigger2', title = 'EH AutoRigger', width = 400, height = 300) as self.win:
            with pm.formLayout('ehMainLayout') as self.form:
                with  pm.frameLayout('Autorigger by Eric Hicken', mh = 5, mw = 5, p = self.form):
                    templateTitle = pm.text(al = 'center', fn = 'boldLabelFont', l = 'Build Template')
                    pm.separator()
                    with pm.frameLayout('templateBuildFrame', cll = True, l = 'Build Template', mh = 5, mw = 5) as self.layout:
                        with pm.frameLayout(cll = True, l = 'Template Base') as fullLayout:
                            with pm.rowColumnLayout('templateBaseFram', p = fullLayout, nc = 2, co = [(1, 'both', 5),(2, 'both', 5)], ro = [(1, 'both', 5), (2, 'both', 5)], cw = [(1, 125), (2, 125)]):
                                pm.optionMenu(l = 'Presets')
                                pm.menuItem(l = 'Preset 1')
                                pm.menuItem(l = 'Preset 2')
                                pm.menuItem(l = 'Preset 3')                    
                                pm.button( label='Build Preset' )
                                pm.button( label='Save Template' )
                                pm.button( label='Load Template' )

                        with pm.frameLayout('spineOptionFrame', cll = True, l = 'Spine Options') as self.spineLayout:
                            '''
                            with pm.rowColumnLayout(nc = 1, co = (1, 'both', 5), ro = (1, 'both', 5), cw = (1, 250)):
                                spineType = pm.optionMenu(l = 'Spine Type:')
                                pm.menuItem(l = 'Advanced Twist')
                                pm.menuItem(l = 'Straight Twist')
                                pm.menuItem(l = 'FK')
                            with pm.rowColumnLayout(p = self.spineLayout, nc = 2, co = [(1, 'both', 5),(2, 'both', 5)], ro = (1, 'both', 5), cw = [(1, 125), (2, 125)]):
                                pm.text(l = 'Spine Count:')
                                self.spineText = pm.textField(tx = self.spineCount, cc = self.spineNumber)
                            '''
                            
                        with pm.frameLayout('armOptionFrame', cll = True, l = 'Arm Options') as self.armLayout:
                            with pm.columnLayout('armOptionTop', adj = True) as self.armBaseColumn:
                                armList = {}
                                addArmBtn = pm.button(p = self.armBaseColumn, l = 'Add Arm', c = 'print "Hi"')
                                with pm.rowColumnLayout('armColumn', p = self.armBaseColumn, nc = 2, co = [(1, 'both', 5),(2, 'both', 5)], ro = (1, 'both', 5), cw = [(1, 125), (2, 125)]) as self.armColumn:
                                    pm.button(addArmBtn, e = True, c = partial(self.armBtn, self))
                            with pm.columnLayout('armColumnBot', adj = True):
                                updateArmBtn = pm.button(l = 'Update', c = partial(self.updateOptionMenu, self))
                                
                self.form.redistribute()
                self.spineRef = spineOptionMenu(self.spineLayout, (0, 0, 0), 'template_Grp', self)
                pm.showWindow(self.win)
                
    def updateArmSpineCount(self, num):
        number = int(num)
        self.spineCount = number
        for v in self.armList.values():
            v.setSpineCount(number)

    def findTemplate(self):
        transforms = pm.ls(typ = 'transform', ni = True, o = True, r = True)
        for t in transforms:
            if t.name() == 'template_Grp':
                self.templateGrp = t
        if self.templateGrp == None:
            self.templaetGrp = pm.createNode('transform', n = 'template_Grp')
            
        return self.templateGrp

    def armBtn(self, *args):
        if self.armList != None:
            self.armList = self.updateOptionMenu(self)
            num = len(self.armList) + 1
        else:
            self.armList = {}
            self.armList = self.updateOptionMenu(self)
            num = 1
            
        arm = armOptionMenu(self.armColumn, (0, 0, 0), self.templateGrp, num, self)
        children = pm.listRelatives(self.templateGrp, c = True)
        armGrps = []
        for c in children:
            if 'Arm' in c.name():
                armGrps.append(c)
        armDigits = []
        for a in armGrps:
            string = (re.findall('\d+', a.name()))
            for s in string:
                armDigits.append(int(s))
        
        name = 'Arm%02d'%(num)
        self.armList[name] = arm
        arm.buildArm()
        return self.armList
        
    def updateOptionMenu(self, *args):
        #Check Arm Groups in Scene
        #Save as Numbers
        sceneGrps = pm.listRelatives(self.templateGrp, c = True)
        armGrps = []

        for g in sceneGrps:
            if 'Arm' in g.name():
                armGrps.append(g)
        
        if armGrps != []:
            armGrps = sorted(armGrps)
            
            sceneNumbers = []
            for a in armGrps:
                string = (re.findall('\d+', a.name()))
                for s in string:
                    sceneNumbers.append(int(s))

        #Check Arm Grps in UI
        #Save as Numbers
        uiGrps = pm.rowColumnLayout(self.armColumn, q = True, ca = True)
        
        if uiGrps != None:
            uiGrps = sorted(uiGrps)
        
            uiNumbers = []
            for g in uiGrps:
                string = (re.findall('\d+', g))
                for s in string:
                    uiNumbers.append(int(s))
            uiNumbers = sorted(uiNumbers)

        if armGrps != [] and uiGrps != None:
            sceneNotUi = set(sceneNumbers).difference(set(uiNumbers))
            uiNotScene = set(uiNumbers).difference(set(sceneNumbers))
            
            #Delete arms present in Scene but not UI
            if len(sceneNotUi) != 0:
                for i in sceneNotUi:
                    pm.delete(armGrps[sceneNumbers.index(i)])
            
            #Delete arms present in Ui but not Scene
            if len(uiNotScene) != 0:
                for i in uiNotScene:
                    pm.deleteUI(uiGrps[uiNumbers.index(i)])
            
            #Update internal reference
            remaining = set(sceneNumbers).intersection(uiNumbers)
            newList = {}
            for index, r in enumerate(remaining):
                name = 'Arm%02d'%(r)
                self.armList[name].renameClass(10 + index + len(remaining))
                self.armList[name].renameClass(index + 1)
                rename = 'Arm%02d'%(index + 1)
                newList[rename] = self.armList[name]
                
            print 'Reconciled UI and Scene Arms'
            
        if armGrps == [] and uiGrps != None:
            for u in uiGrps:
                pm.deleteUI(u)
            newList = {}
            print 'Cleared UI'
            
        if armGrps != [] and uiGrps == None and armGrps != []:
            for s in armGrps:
                pm.delete(s)
            newList = {}
            print 'Cleared Scene Arms'
        
        if armGrps == [] and uiGrps == None:
            newList = {}
            print 'Nothing to Update'
        
        self.armList = newList
        return self.armList
            
            

main = uiBase()

'''
Get Scene objects
get UI objects
find scene objects without ui
find ui objects without scene

'''


'''
print updateOptionMenu(armColumn, templateGrp, armList)


armList['Arm03'].renameClass(5)
pm.deleteUI(armList['Arm03'].layout)

test1 = ['Arm03', 'Arm04', 'Arm01']
test2 = sorted(test1)
print test2

print armList['Arm03'].layout
pm.renameUI(armList['Arm03'].layout, 'test')
print armList['Arm03'].layout

children = pm.rowColumnLayout(armList['Arm03'].parent, q = True, ca = True)
print children

'''

def changeSides(arm):
    arm[0].tx.set(arm[0].tx.get() * -1)
    arm[0].jointOrientZ.set(180 - arm[0].jointOrientZ.get())
    #newArm = []
    for i in range(1, len(arm)):
        arm[i].jointOrientZ.set(arm[i].jointOrientZ.get() * -1)
    for a in arm:
        pm.parent(a, w = True)
    for a in arm:
        if a.jointOrientY.get >= 0:
            a.jointOrientY.set(a.jointOrientY.get() - 180)
        else:
            a.jointOrientY.set(a.jointOrientY.get() + 180)
    #    if '_L' in a.name():
    #        name = a.name().replace('_L', '_R')
    #    if '_R' in a.name():
    #        name = a.name().replace('_R', '_L')
    #    a = pm.rename(a, name)
    #    newArm.append(a)
    for i in range(len(arm) - 1, 0, -1):
        pm.parent(arm[i], arm[i-1])
    pm.select(cl = True)
    return arm
        
        

