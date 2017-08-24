import maya.cmds as cmds
import json

def setupTemplate(menu, wingsOption, *args):
    currentTemplate = 'templateData.dump'
    value = cmds.optionMenu(menu, q = True, v = True)
    if value == 'Preset 1':
        posList = [[0.0, 180.34, 0.0], [0.0, 99.702, -2.33], [0.0, 145.0, -2.33], [0.0, 150.581, -3.354], [0.0, 165.0, -2.33], [4.328, 146.095, -3.051], [11.737, 143.746, -3.051], [29.464, 123.657, -3.051], [45.7, 108.09, -3.051], [7.594, 98.593, 0.0], [6.132, 51.852, -3.828], [4.693, 7.029, -7.043], [4.693, 1.917, -0.773], [4.693, 1.917, 8.532], [45.275, 107.612, -1.081], [45.358, 106.413, -0.565], [45.639, 102.918, 0.955], [46.783, 100.542, 2.347], [47.966, 98.086, 3.785], [47.397, 105.239, -0.418], [50.685, 101.786, -0.47], [53.136, 99.213, -0.191], [54.777, 97.491, -0.004], [56.411, 95.775, 0.182], [47.809, 105.631, -2.339], [51.294, 101.972, -2.347], [53.747, 99.397, -2.291], [55.874, 97.164, -2.242], [57.833, 95.107, -2.198], [47.596, 105.429, -4.181], [50.781, 102.085, -4.15], [53.133, 99.616, -4.313], [54.969, 97.688, -4.44], [56.771, 95.796, -4.564], [47.258, 105.106, -5.733], [50.004, 102.223, -5.87], [51.92, 100.211, -6.292], [53.093, 98.98, -6.551], [54.56, 97.44, -6.874]]
    if value == 'Preset 2':
        posList = [[0.0, 185.63418663069888, 0.0], [0.0, 100.59035062291028, -2.4115751640240064], [0.0, 150.07656600149394, -2.4115751640240064], [0.0, 155.85296127635146, -3.4714262232345563], [0.0, 170.33821030263476, 1.2139508815817677], [5.154679818928308, 152.28649061165243, -3.157817950831439], [21.397370242250414, 149.00881197220284, -4.075095931449884], [30.48372430671461, 121.70513028212879, -4.502859348475979], [38.13549351021957, 98.91487868916742, -0.5878687623864315], [10.443393621199073, 95.88633286310427, 0.9837345651911579], [8.576792341245806, 54.41792176298072, 1.3143731435858421], [6.189965602029037, 7.247085175178967, -1.7529329381549577], [8.031314143433784, 2.846161694301125, 6.07983292348578], [9.754405791031237, 1.471758005477479, 13.798084064159005], [38.02171647821036, 97.10200847656438, 1.1576566001153523], [37.332297356884844, 95.37411869105132, 2.1447802889031933], [36.39891133934262, 93.03477515420386, 3.4812205183644975], [35.745768828915416, 89.85923544433527, 4.863724393855797], [34.99909804971669, 86.2289669015739, 6.44419914397301], [39.23239442933958, 95.5122891888186, 1.6137031485165287], [39.67760492255226, 87.89916094691884, 3.6321765801513464], [39.71319617851056, 84.69138867994843, 3.432064617062122], [39.41035331113665, 81.82159903695295, 3.1574666905990663], [39.06040320154466, 79.25598724745099, 2.889356488809229], [39.658803305100015, 95.41285863432802, 0.2550483533576369], [40.78654380202077, 87.64867377497309, 1.5465483498131678], [40.569520477770844, 84.29982901744664, 1.3831598605190694], [40.07491068321692, 81.58133084419835, 1.1930006800756632], [39.42651174566704, 78.54325588490771, 0.9632090382954023], [39.420910965839376, 95.47549255320376, -1.019821870435568], [41.03262142647848, 88.02367674273822, -0.6807790955069924], [40.69388689833849, 85.21696092985925, -0.7857109146203421], [40.27885464675231, 82.52177883153524, -0.8849897893455895], [39.859618581471175, 80.02199812912626, -0.976504257938329], [38.8903990111308, 95.32930955784707, -2.604640831033887], [40.38879262537414, 88.52514752037173, -2.6208234788493954], [40.43720677156933, 86.2489724140392, -2.652599018699077], [40.03081432605393, 84.14884234319794, -2.658248743039257], [39.605123903074336, 81.94898536250352, -2.664166750548078]]
    if value == 'Preset 3':
        posList = [[0.0, 98.1384488940239, -1.3858338540792465], [0.0, 59.300603828072546, -1.3858338540792465], [0.0, 86.24287933111191, -1.3858338540792465], [0.0, 89.56233801764249, -1.9948870157003402], [0.0, 98.1384488940239, -1.3858338540792465], [2.5742012534141665, 86.89416176468134, -1.8146691368222283], [8.337243241678257, 85.51189157842535, -1.814669136822226], [15.124341523673055, 69.0933140328585, -1.8146691368222145], [21.069849870729364, 54.71061530239766, 0.8134075516082719], [5.780311005602666, 57.229646900578274, 2.4424906541753444e-15], [3.9054807887110807, 29.38854508143596, -0.41006188772046276], [2.110220783250666, 2.735717416292242, -1.6492121569112184], [2.040305093986479, 1.6685709590580344, 2.008071121645387], [2.000868973017868, 1.0480612264407625, 6.4322233911988285], [20.115478061153837, 53.91877567505924, 1.4972020798720789], [19.85115297843412, 53.300184773366, 1.8879366600052547], [19.238709185147048, 51.86690362415482, 2.793272491031706], [18.789430879351077, 50.81547305451706, 3.457411392916745], [18.355427744382297, 49.68521240551103, 4.0627466161586465], [20.82385766699854, 52.798962973117355, 2.1809272191589413], [21.236853209312983, 50.352907739083626, 2.691142920396806], [21.319729595246727, 48.48959705368742, 2.9969047739212047], [21.176546570354624, 47.35936009452668, 3.1131638853569297], [20.852024288712204, 46.15730253090854, 3.1751913584057427], [21.43277994013768, 52.87732985195855, 1.4266106375089205], [21.827291030446467, 50.11738416472808, 1.7732534255885568], [21.67341373707539, 48.441493609276435, 1.8416255180052776], [21.23952227552493, 46.89379045147427, 1.7993695294971008], [20.884905716803416, 45.62886312199641, 1.7648339957103891], [21.478698762375597, 52.76021881233915, 0.8186874806070364], [22.00117089206111, 50.17924715105192, 0.7964024452751471], [21.916542024873753, 48.64785949755699, 0.7158242127411055], [21.499035065478633, 47.45201964964626, 0.5929181503716686], [21.096209407321236, 46.298230561954526, 0.4743339822485053], [21.218253113582023, 52.69044529743524, 0.13214915037150665], [22.01566455381223, 50.49613301393584, -0.2724088593242326], [21.817159747226803, 49.057625491652594, -0.5002081849069118], [21.622892736981694, 48.149450154324775, -0.6404487731074914], [21.415345609858917, 47.179191838472164, -0.790276225284343]]
    
    if cmds.objExists('localScale_Grp'):
        cmds.delete('localScale_Grp')
    if cmds.objExists('pelvis_PosJnt'):
        cmds.delete('pelvis_PosJnt')
    
    if wingsOption == True:
        spineLocs, lArmLocs, rArmLocs, lLegLocs, rLegLocs, lHandLocs, rHandLocs, heightLoc, locGrp, pelvisPosJnt, wingLocs = autoriggerLocs(True, posList)
        templateData = spineLocs, lArmLocs, rArmLocs, lLegLocs, rLegLocs, lHandLocs, rHandLocs, heightLoc, locGrp, pelvisPosJng, wingLocs
    else:
        spineLocs, lArmLocs, rArmLocs, lLegLocs, rLegLocs, lHandLocs, rHandLocs, heightLoc, locGrp, pelvisPosJnt = autoriggerLocs(False, posList)
        templateData = spineLocs, lArmLocs, rArmLocs, lLegLocs, rLegLocs, lHandLocs, rHandLocs, heightLoc, locGrp, pelvisPosJnt
    
    json.dump(templateData, open(currentTemplate, 'wb'))

def AutoRiggerRun(wings, nameField, *args):
    currentTemplate = 'templateData.dump'
    
    templateData = json.load(open(currentTemplate, 'rb'))
    
    charName = cmds.textField(nameField, q = True, tx = True)

    lSide = 'L_'
    rSide = 'R_'

    bindJnts = []
    spineJnts = []
    neckJnts = []
    lArmJnts = []
    lArmOffs = []
    lArmFkCtrls = []
    rArmJnts = []
    rArmOffs = []
    rArmFkCtrls = []
    lHandFkOffs = []
    lHandFkCtrls = []
    rHandFkOffs = []
    rHandFkCtrls = []
    lLegJnts = []
    rLegJnts = []
    lHandJnts = []
    rHandJnts = []
    spineCtrlJnts = []
    bindList = []

    heightTran = cmds.getAttr(templateData[7] + '.translateY')

    rootCtrl, rootGrp, rigGrp, geoGrp = rootCtrlMake(charName, heightTran)
    heightTran = cmds.xform(templateData[7], q = True, t = True, ws = True)
    jntScale = heightTran[1] / 36

    spineJnts, spineBind, neckJnt, upperBodyGrp, pelvisOff, pelvisCtrl, upperBodyOff, upperBodyCtrl, spineFkOff = autoSpine(templateData[0], jntScale, rigGrp)
    neckJnts, neckBind = autoNeck(neckJnt, rigGrp, upperBodyCtrl, upperBodyGrp, jntScale)

    lArmLoc, lArmBind, lArmRigGrp, lArmJnts, lArmFkOffs, lArmFkCtrls, lHandCtrl, lHandOff, lArmLowerTwist, lArmUpperTwist = autoArm(templateData[1], jntScale, lSide, 'Temp', rootCtrl, 3)
    rArmLoc, rArmBind, rArmRigGrp, rArmJnts, rArmFkOffs, rArmFkCtrls, rHandCtrl, rHandOff, rArmLowerTwist, rArmUpperTwist = autoArm(templateData[2], jntScale, rSide, lArmJnts, rootCtrl, 3)

    lLegJnts, lLegBind, lLegRigGrp, lLegLoc, lLegTwist = autoLeg(templateData[3], jntScale, lSide,'Temp', rootCtrl)
    rLegJnts, rLegBind, rLegRigGrp, rLegLoc, rLegTwist = autoLeg(templateData[4], jntScale, rSide, lLegJnts, rootCtrl)

    lHandJnts = autoHand(templateData[5], (jntScale/3), lSide, lArmJnts[3], 'Temp')
    rHandJnts = autoHand(templateData[6], (jntScale/3), rSide, rArmJnts[3], lHandJnts)

    cmds.parent(lArmRigGrp, rArmRigGrp, lLegRigGrp, rLegRigGrp, rigGrp)
    cmds.parent(lArmLoc, rArmLoc, lLegLoc, rLegLoc, rigGrp)

    bindList.extend(spineBind)
    bindList.extend(neckBind)
    bindList.extend(lArmBind)
    bindList.extend(rArmBind)
    bindList.extend(lLegBind)
    bindList.extend(rLegBind)
    bindList.extend(lHandJnts)
    bindList.extend(rHandJnts)

    if wings == True:
        cmds.parentConstraint(spineJnts[5], lWingJnt, mo = True)
        cmds.parentConstraint(spineJnts[5], rWingJnt, mo = True)
        cmds.parent(lWingJnt, rWingJnt, rigGrp)

    #Connect segments
    cmds.pointConstraint(spineJnts[6], upperBodyGrp, mo = True)
    cmds.orientConstraint(upperBodyCtrl, upperBodyGrp, mo = True)
    cmds.parentConstraint(upperBodyGrp, lArmLoc, mo = True)
    cmds.parentConstraint(upperBodyGrp, rArmLoc, mo = True)
    cmds.parentConstraint(pelvisCtrl, lLegLoc, mo = True)
    cmds.parentConstraint(pelvisCtrl, rLegLoc, mo = True)

    #Creates finger fk controls
    for index in range(0, 25, 5):
        for i in range(0, 4):
            tempDiv = makeCtrl(lHandJnts[index + i], 1.2, True)
            lHandFkOffs.append(tempDiv[0])
            lHandFkCtrls.append(tempDiv[1])
            
    for index in range(0, 20, 4):
        for i in range(0, 3):
            cmds.parent(lHandFkOffs[index+i+1], lHandFkCtrls[index+i])
        cmds.parent(lHandFkOffs[index], lHandCtrl)
        
    for index in range(0, 25, 5):
        for i in range(0, 4):
            tempDiv = makeCtrl(rHandJnts[index + i], 1.2, True)
            rHandFkOffs.append(tempDiv[0])
            rHandFkCtrls.append(tempDiv[1])
                            
    for index in range(0, 20, 4):
        for i in range(0, 3):
            cmds.parent(rHandFkOffs[index+i+1], rHandFkCtrls[index+i])
        cmds.parent(rHandFkOffs[index], rHandCtrl)

    bodyOffName = 'body_Off'
    bodyCtrlName = 'body_Ctrl'
    cmds.duplicate(pelvisOff, po = True, n = bodyOffName)
    cmds.duplicate(pelvisCtrl, po = False, n = bodyCtrlName)
    cmds.parent(bodyCtrlName, bodyOffName)
    cmds.scale(1.165, 1.165, 1.165, bodyCtrlName)
    cmds.makeIdentity(bodyCtrlName, apply=True, s=1, n=2 )

    cmds.parent(pelvisOff, bodyCtrlName)
    cmds.parent(spineFkOff, bodyCtrlName)
    cmds.parent(bodyOffName, rootCtrl)

    cmds.delete(templateData[9])
    cmds.delete(templateData[8])
     
def ehAutoRiggerUI():
    winName = 'ehAutoRigger'
    if(cmds.window(winName, ex = True)):
        cmds.deleteUI(winName)
    ehARWin = cmds.window(winName, title = "Auto Rigger", width = 400, height = 300)
    ehARColumn = cmds.frameLayout('Autorigger by Eric Hicken', mh = 5, mw = 5)
    ehARGrid = cmds.gridLayout(numberOfRowsColumns = (3,1), cellWidthHeight = (80,20), p = ehARColumn)
    presetMenu = cmds.optionMenu(label='Preset Templates', p = ehARColumn)
    cmds.menuItem(label='Preset 1', p = presetMenu)
    cmds.menuItem(label='Preset 2', p = presetMenu)
    cmds.menuItem(label='Preset 3', p = presetMenu)
    cmds.text(label='Character Name')
    nameField = cmds.textField()
    butTemplate = cmds.button(l = 'Create Template', c = lambda x: setupTemplate(presetMenu, False), p = ehARColumn)
    butRig = cmds.button(l = 'Create Rig from Template', c = lambda x: AutoRiggerRun(False, nameField), p = ehARColumn)
    butEx = cmds.button(l = 'Exit', command=('cmds.deleteUI(\"' + ehARWin + '\", window=True)'), p = ehARColumn )
    cmds.showWindow(winName)
    
ehAutoRiggerUI()