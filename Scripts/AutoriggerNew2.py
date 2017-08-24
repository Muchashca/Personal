import pymel.core as pm
import pymel.core.datatypes as dt

def checkTemplateLeg(baseJnt):
    children = pm.listRelatives(baseJnt, typ = 'joint')
    jointList = [baseJnt]
    for a in children:
        if 'knee' in a.name():
            jointList.append(a)
            children = pm.listRelatives(a, typ = 'joint')
            for b in children:
                if 'foot' in b.name():
                    jointList.append(b)
                    children = pm.listRelatives(b, typ = 'joint')
                    for c in children:
                        if 'ball' in c.name():
                            jointList.append(c)
                            children = pm.listRelatives(c, typ = 'joint')
                            for d in children:
                                if 'toe' in d.name():
                                    jointList.append(d)
                                    return jointList
                                else:
                                    return False
                        else:
                            return False
                else:
                    return False
                    return False
        else:
            return False

def checkTemplateArm(baseJnt):
    children = pm.listRelatives(baseJnt, typ = 'joint')
    jointList = [baseJnt]
    for a in children:
        if 'shoulder' in a.name():
            jointList.append(a)
            children = pm.listRelatives(a, typ = 'joint')
            for b in children:
                if 'elbow' in b.name():
                    jointList.append(b)
                    children = pm.listRelatives(b, typ = 'joint')
                    for c in children:
                        if 'wrist' in c.name():
                            jointList.append(c)
                            return jointList
                        else:
                            return False
                else:
                    return False
        else:
            return False

def checkTemplateSpine(baseJnt):
    children = pm.listRelatives(baseJnt, typ = 'joint')
    jointList = [baseJnt]
    for a in children:
        if 'spine' in a.name():
            jointList.append(a)
            return jointList
            
def checkTemplateNeck(baseJnt):
    children = pm.listRelatives(baseJnt, typ = 'joint')
    jointList = [baseJnt]
    for a in children:
        if 'head' in a.name():
            jointList.append(a)
            return jointList
    
def prepJointInfo(baseJnt):
    constraints = pm.listRelatives(baseJnt, ad = True, typ = 'constraint')
    children = pm.listRelatives(baseJnt, ad = True, typ = 'joint')
    for c in constraints:
        pm.delete(c)
    for c in children:
        pm.disconnectAttr(c)

def getJointInfo(baseJnt):
    pm.disconnectAttr(baseJnt)
    pm.parent(baseJnt, 'template_Grp')
    name = baseJnt.name().replace('Pos', 'B_')
    order = pm.joint(baseJnt, q = True, roo = True)
    pos = pm.xform(baseJnt, q = True, ws = True, t = True)
    rot = pm.xform(baseJnt, q = True, ro = True)
    ori = pm.joint(baseJnt, q = True, o = True)
    jointInfo = {'name':name, 'order':order, 'pos':pos, 'rot':rot, 'ori':ori}
    return jointInfo

#Template = Dict of member sets and info
#Set = List of members by category
#Joint = Dict of joint info

def rigSetup(**template):
    for set in template['Spine']:
        rigSpineSetup(set)
    for set in template['Neck']:
        rigNeckSetup(set)
    for set in template['Arm']:
        rigArmSetup(set)
    for set in template['Leg']:
        rigLegSetup(set)
    pm.delete('template_Grp')
    
def rigSpineSetup(set):
    jointList = []
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2])
        jointList.append(joint)
    pm.parent(jointList[1], jointList[0])
    
def rigNeckSetup(set):
    jointList = []
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2])
        jointList.append(joint)
    pm.parent(jointList[1], jointList[0])
    
def rigArmSetup(set):
    jointList = []
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2])
        jointList.append(joint)
    for i in range(3, 0, -1):
        pm.parent(jointList[i], jointList[i-1])
        
def rigLegSetup(set):
    jointList = []
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2])
        jointList.append(joint)
    for i in range(4, 0, -1):
        pm.parent(jointList[i], jointList[i-1])

def templateSetup(**template):
    if pm.objExists('template_Grp'):
        pm.delete('template_Grp')
    pm.createNode('transform', n = 'template_Grp')
    height = template.get('Neck')[0][1].get('pos')[1]
    radius = {'rad':(height/60)}
    for set in template['Spine']:
        templateSpineSetup(set, **radius)
    for set in template['Neck']:
        templateNeckSetup(set, **radius)
    for set in template['Arm']:
        templateArmSetup(set, **radius)
    for set in template['Leg']:
        templateLegSetup(set, **radius)

def templateSpineSetup(set, **kwargs):
    jointList = []
    if kwargs.get('rad') != None:
        radius = kwargs.get('rad')
    else:
        radius = 1
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2], rad = radius)
        jointList.append(joint)
        joint.displayLocalAxis.set(True, k = True)
        joint.jointOrientX.set(k = True)
        joint.jointOrientY.set(k = True)
        joint.jointOrientZ.set(k = True)
    pm.parent(jointList[1], jointList[0])

def templateNeckSetup(set, **kwargs):
    jointList = []
    if kwargs.get('rad') != None:
        radius = kwargs.get('rad')
    else:
        radius = 1
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2], rad = radius)
        jointList.append(joint)
        joint.displayLocalAxis.set(True, k = True)
        joint.jointOrientX.set(k = True)
        joint.jointOrientY.set(k = True)
        joint.jointOrientZ.set(k = True)
    pm.parent(jointList[1], jointList[0])
    
def templateArmSetup(set, **kwargs):
    jointList = []
    if kwargs.get('rad') != None:
        radius = kwargs.get('rad')
    else:
        radius = 1
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2], rad = radius)
        jointList.append(joint)
        joint.displayLocalAxis.set(True, k = True)
        joint.jointOrientX.set(k = True)
        joint.jointOrientY.set(k = True)
        joint.jointOrientZ.set(k = True)
    for i in range(3, 0, -1):
        pm.parent(jointList[i], jointList[i-1])
        
def templateLegSetup(set, **kwargs):
    jointList = []
    if kwargs.get('rad') != None:
        radius = kwargs.get('rad')
    else:
        radius = 10
    for j in set:
        pm.select(cl = True)
        joint = pm.joint(n = j.get('name'))
        pm.joint(joint, e = True, a = True, o = j.get('ori'), p = j.get('pos'), roo = j.get('order'), ax = j.get('rot')[0], ay = j.get('rot')[1], az = j.get('rot')[2], rad = radius)
        jointList.append(joint)
        joint.displayLocalAxis.set(True, k = True)
        joint.jointOrientX.set(k = True)
        joint.jointOrientY.set(k = True)
        joint.jointOrientZ.set(k = True)
    for i in range(4, 0, -1):
        pm.parent(jointList[i], jointList[i-1])

    '''for member in template:
        print member
        for set in member['Spine']:
            print len(set)
            print 'Spine' + str(set)
        for set in member['Neck']:
            print set
        for set in member['Arm']:
            print set
        for set in member['Leg']:
            print set'''
            
'''
if pm.objExists('template_Grp'):
    armList = []
    legList = []
    spineList = []
    neckList = []
    children = pm.listRelatives('template_Grp', ad = True, typ = 'joint')
    memberList = {'Arms':0, 'Legs':0, 'Spine':0, 'Neck':0, 'Hands':0, 'Feet':0, 'partArm':0, 'partLeg':0}
    for c in children:
        if 'hip' in c.name():
            leg = checkTemplateLeg(c)
            if leg != False:
                memberList['Legs'] += 1
                legList.append(leg)
        if 'clavicle' in c.name():
            arm = checkTemplateArm(c)
            if arm != False:
                memberList['Arms'] += 1
                armList.append(arm)
        if 'pelvis' in c.name():
            spine = checkTemplateSpine(c)
            if spine != False:
                memberList['Spine'] += 1
                spineList.append(spine)
        if 'neck' in c.name():
            neck = checkTemplateNeck(c)
            if neck != False:
                memberList['Neck'] += 1
                neckList.append(neck)

    prepJointInfo('template_Grp')

    spineData = []
    for spine in spineList:
        tempData = []
        for j in spine:
            tempData.append(getJointInfo(j))
        spineData.append(tempData)
    neckData = []
    for neck in neckList:
        tempData = []
        for j in neck:
            tempData.append(getJointInfo(j))
        neckData.append(tempData)
    armData = []
    for arm in armList:
        tempData = []
        for j in arm:
            tempData.append(getJointInfo(j))
        armData.append(tempData)
    legData = []
    for leg in legList:
        tempData = []
        for j in leg:
            tempData.append(getJointInfo(j))
        legData.append(tempData)
    template = {'Info':memberList, 'Spine':spineData, 'Neck':neckData, 'Arm':armData, 'Leg':legData}
    templateSetup(**template)
else:
    print("Warning: No template found.")
    '''
templateSetup(**testPreset)
'''
pm.delete(cn = True)
pm.disconnectAttr(pm.selected())

list = pm.listRelatives(ad = True, type = 'constraint')
for l in list:
    pm.delete(l)
sel = pm.selected()
type(sel[0])
'''
testPreset = {'Info': {'Feet': 0, 'partArm': 0, 'Neck': 1, 'Hands': 0, 'Spine': 1, 'partLeg': 0, 'Legs': 2, 'Arms': 2}, 
              'Spine': 
                  [[{'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999999, -6.3611093629270335e-15, 90.0], 'pos': [0.0, 99.702, -2.33], 'name': u'pelvis_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999999, 10.396969050684161, 90.0], 'pos': [-4.930380657631324e-32, 145.0, -2.33], 'name': u'spine_B_Jnt', 'order': u'xyz'}]], 
              'Leg': 
                  [[{'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999997, 4.679688981819485, -91.7915561875297], 'pos': [7.594, 98.593, 4.440892098500626e-16], 'name': u'L_hip_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999999, 4.1004983749878905, -91.83879522656909], 'pos': [6.131999999999978, 51.85200000000002, -3.828000000000004], 'name': u'L_knee_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999999, -50.80926030103901, -90.00000000000004], 'pos': [4.692999999999959, 7.029000000000025, -7.043000000000012], 'name': u'L_foot_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999997, -89.99999999999999, 0.0], 'pos': [4.692999999999957, 1.9170000000000131, -0.7730000000000095], 'name': u'L_ball_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999997, -89.99999999999999, 0.0], 'pos': [4.69299999999996, 1.9170000000000138, 8.53199999999999], 'name': u'L_toe_B_Jnt', 'order': u'xyz'}], 
                  [{'rot': [0.0, 0.0, 0.0], 'ori': [-89.99999999999999, -4.679688981819475, 91.7915561875297], 'pos': [-7.593999862670898, 98.59300231933594, 4.440892098500626e-16], 'name': u'R_hip_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [-90.0, -4.1004983749878745, 91.8387952265691], 'pos': [-6.131999969482422, 51.85200119018556, -3.8280000686645503], 'name': u'R_knee_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [-89.99999999999999, 50.80926030103901, 90.00000000000009], 'pos': [-4.692999839782715, 7.028999805450432, -7.043000221252441], 'name': u'R_foot_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [-90.00000000000006, 90.0, 0.0], 'pos': [-4.692999839782714, 1.9170000553131112, -0.7730000019073504], 'name': u'R_ball_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [-90.00000000000006, 90.0, 0.0], 'pos': [-4.692999839782715, 1.9170000553131104, 8.531999588012695], 'name': u'R_toe_B_Jnt', 'order': u'xyz'}]], 
              'Neck': 
                  [[{'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999999, -4.062177727117156, 90.0], 'pos': [2.888982376975575e-16, 150.58100000000002, -3.3540000000000094], 'name': u'neck_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [89.99999999999999, -4.062177727117156, 90.0], 'pos': [6.29958750862403e-16, 165.0, -2.330000000000003], 'name': u'head_B_Jnt', 'order': u'xyz'}]], 
              'Arm': 
                  [[{'rot': [0.0, 0.0, 0.0], 'ori': [0.0, -0.0, 162.408946535663], 'pos': [4.328, 146.095, -3.0510000000000037], 'name': u'L_clavicle_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [0.0, -0.0, 131.425929467542], 'pos': [11.736999999999977, 143.74599999999998, -3.0510000000000033], 'name': u'L_shoulder_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [0.0, -0.0, 136.2050820411402], 'pos': [29.46399999999999, 123.657, -3.0510000000000046], 'name': u'L_elbow_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [0.0, -0.0, 136.2050820411402], 'pos': [45.69999999999999, 108.09000000000002, -3.051000000000004], 'name': u'L_wrist_B_Jnt', 'order': u'xyz'}], 
                  [{'rot': [0.0, 0.0, 0.0], 'ori': [0.0, 180.0, 17.591053464336955], 'pos': [-4.328000068664551, 146.09500122070312, -3.0510001182556112], 'name': u'R_clavicle_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [0.0, 180.0, 48.574070532457974], 'pos': [-11.737000465393074, 143.74600219726565, -3.0510001182556157], 'name': u'R_shoulder_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [0.0, 180.0, 43.794917958859784], 'pos': [-29.464000701904286, 123.65699768066406, -3.051000118255615], 'name': u'R_elbow_B_Jnt', 'order': u'xyz'}, 
                  {'rot': [0.0, 0.0, 0.0], 'ori': [0.0, 180.0, 43.794917958859784], 'pos': [-45.70000076293945, 108.08999633789062, -3.051000118255615], 'name': u'R_wrist_B_Jnt', 'order': u'xyz'}]]}
