from maya.OpenMaya import MVector
import maya.cmds as cmds
import pymel.core as pmc

Nova = [[0.0, 180.34, 0.0], [0.0, 99.702, -2.33], [0.0, 145.0, -2.33], [0.0, 150.581, -3.354], [0.0, 165.0, -2.33], [4.328, 146.095, -3.051], [11.737, 143.746, -3.051], [29.464, 123.657, -3.051], [45.7, 108.09, -3.051], [7.594, 98.593, 0.0], [6.132, 51.852, -3.828], [4.693, 7.029, -7.043], [4.693, 1.917, -0.773], [4.693, 1.917, 8.532], [45.275, 107.612, -1.081], [45.358, 106.413, -0.565], [45.639, 102.918, 0.955], [46.783, 100.542, 2.347], [47.966, 98.086, 3.785], [47.397, 105.239, -0.418], [50.685, 101.786, -0.47], [53.136, 99.213, -0.191], [54.777, 97.491, -0.004], [56.411, 95.775, 0.182], [47.809, 105.631, -2.339], [51.294, 101.972, -2.347], [53.747, 99.397, -2.291], [55.874, 97.164, -2.242], [57.833, 95.107, -2.198], [47.596, 105.429, -4.181], [50.781, 102.085, -4.15], [53.133, 99.616, -4.313], [54.969, 97.688, -4.44], [56.771, 95.796, -4.564], [47.258, 105.106, -5.733], [50.004, 102.223, -5.87], [51.92, 100.211, -6.292], [53.093, 98.98, -6.551], [54.56, 97.44, -6.874]]
Morning = [[0.0, 185.63418663069888, 0.0], [0.0, 100.59035062291028, -2.4115751640240064], [0.0, 150.07656600149394, -2.4115751640240064], [0.0, 155.85296127635146, -3.4714262232345563], [0.0, 170.33821030263476, 1.2139508815817677], [5.154679818928308, 152.28649061165243, -3.157817950831439], [21.397370242250414, 149.00881197220284, -4.075095931449884], [30.48372430671461, 121.70513028212879, -4.502859348475979], [38.13549351021957, 98.91487868916742, -0.5878687623864315], [10.443393621199073, 95.88633286310427, 0.9837345651911579], [8.576792341245806, 54.41792176298072, 1.3143731435858421], [6.189965602029037, 7.247085175178967, -1.7529329381549577], [8.031314143433784, 2.846161694301125, 6.07983292348578], [9.754405791031237, 1.471758005477479, 13.798084064159005], [38.02171647821036, 97.10200847656438, 1.1576566001153523], [37.332297356884844, 95.37411869105132, 2.1447802889031933], [36.39891133934262, 93.03477515420386, 3.4812205183644975], [35.745768828915416, 89.85923544433527, 4.863724393855797], [34.99909804971669, 86.2289669015739, 6.44419914397301], [39.23239442933958, 95.5122891888186, 1.6137031485165287], [39.67760492255226, 87.89916094691884, 3.6321765801513464], [39.71319617851056, 84.69138867994843, 3.432064617062122], [39.41035331113665, 81.82159903695295, 3.1574666905990663], [39.06040320154466, 79.25598724745099, 2.889356488809229], [39.658803305100015, 95.41285863432802, 0.2550483533576369], [40.78654380202077, 87.64867377497309, 1.5465483498131678], [40.569520477770844, 84.29982901744664, 1.3831598605190694], [40.07491068321692, 81.58133084419835, 1.1930006800756632], [39.42651174566704, 78.54325588490771, 0.9632090382954023], [39.420910965839376, 95.47549255320376, -1.019821870435568], [41.03262142647848, 88.02367674273822, -0.6807790955069924], [40.69388689833849, 85.21696092985925, -0.7857109146203421], [40.27885464675231, 82.52177883153524, -0.8849897893455895], [39.859618581471175, 80.02199812912626, -0.976504257938329], [38.8903990111308, 95.32930955784707, -2.604640831033887], [40.38879262537414, 88.52514752037173, -2.6208234788493954], [40.43720677156933, 86.2489724140392, -2.652599018699077], [40.03081432605393, 84.14884234319794, -2.658248743039257], [39.605123903074336, 81.94898536250352, -2.664166750548078]]
SLY = [[0.0, 98.1384488940239, -1.3858338540792465], [0.0, 59.300603828072546, -1.3858338540792465], [0.0, 86.24287933111191, -1.3858338540792465], [0.0, 89.56233801764249, -1.9948870157003402], [0.0, 98.1384488940239, -1.3858338540792465], [2.5742012534141665, 86.89416176468134, -1.8146691368222283], [8.337243241678257, 85.51189157842535, -1.814669136822226], [15.124341523673055, 69.0933140328585, -1.8146691368222145], [21.069849870729364, 54.71061530239766, 0.8134075516082719], [5.780311005602666, 57.229646900578274, 2.4424906541753444e-15], [3.9054807887110807, 29.38854508143596, -0.41006188772046276], [2.110220783250666, 2.735717416292242, -1.6492121569112184], [2.040305093986479, 1.6685709590580344, 2.008071121645387], [2.000868973017868, 1.0480612264407625, 6.4322233911988285], [20.115478061153837, 53.91877567505924, 1.4972020798720789], [19.85115297843412, 53.300184773366, 1.8879366600052547], [19.238709185147048, 51.86690362415482, 2.793272491031706], [18.789430879351077, 50.81547305451706, 3.457411392916745], [18.355427744382297, 49.68521240551103, 4.0627466161586465], [20.82385766699854, 52.798962973117355, 2.1809272191589413], [21.236853209312983, 50.352907739083626, 2.691142920396806], [21.319729595246727, 48.48959705368742, 2.9969047739212047], [21.176546570354624, 47.35936009452668, 3.1131638853569297], [20.852024288712204, 46.15730253090854, 3.1751913584057427], [21.43277994013768, 52.87732985195855, 1.4266106375089205], [21.827291030446467, 50.11738416472808, 1.7732534255885568], [21.67341373707539, 48.441493609276435, 1.8416255180052776], [21.23952227552493, 46.89379045147427, 1.7993695294971008], [20.884905716803416, 45.62886312199641, 1.7648339957103891], [21.478698762375597, 52.76021881233915, 0.8186874806070364], [22.00117089206111, 50.17924715105192, 0.7964024452751471], [21.916542024873753, 48.64785949755699, 0.7158242127411055], [21.499035065478633, 47.45201964964626, 0.5929181503716686], [21.096209407321236, 46.298230561954526, 0.4743339822485053], [21.218253113582023, 52.69044529743524, 0.13214915037150665], [22.01566455381223, 50.49613301393584, -0.2724088593242326], [21.817159747226803, 49.057625491652594, -0.5002081849069118], [21.622892736981694, 48.149450154324775, -0.6404487731074914], [21.415345609858917, 47.179191838472164, -0.790276225284343]]

def autoriggerLocs(wings, posList):
    lSide = 'L_'
    rSide = 'R_'
    
    spineLocs = []
    lArmLocs = []
    rArmLocs = []
    lLegLocs = []
    rLegLocs = []
    lHandLocs = []
    rHandLocs = []
    wingLocs = []
    spinePosJnts = []
    lArmPosJnts = []
    rArmPosJnts = []
    lLegPosJnts = []
    rLegPosJnts = []
    lHandPosJnts = []
    rHandPosJnts = []

    heightLocName = 'height_Loc'
    cmds.spaceLocator(n = heightLocName)
    cmds.xform(heightLocName, t = (posList[0][0], posList[0][1], posList[0][2]), ws= True)
    
    locScale = (cmds.getAttr('height_Loc.translateY'))/36
    jntScale = (cmds.getAttr('height_Loc.translateY'))/60
    
    cmds.setAttr(heightLocName + '.localScaleX', locScale)
    cmds.setAttr(heightLocName + '.localScaleY', locScale)
    cmds.setAttr(heightLocName + '.localScaleZ', locScale)
             
    pelvisPosLocName = 'pelvisPos_Loc'
    spineLocs.append(pelvisPosLocName)
    spinePosLocName = 'spinePos_Loc'
    spineLocs.append(spinePosLocName)
    neckPosLocName = 'neckPos_Loc'
    spineLocs.append(neckPosLocName)
    headPosLocName = 'headPos_Loc'
    spineLocs.append(headPosLocName)
    lClaviclePosLocName = lSide + 'claviclePos_Loc'
    lArmLocs.append(lClaviclePosLocName)
    lShoulderPosLocName = lSide + 'shoulderPos_Loc'
    lArmLocs.append(lShoulderPosLocName)
    lElbowPosLocName = lSide + 'elbowPos_Loc'
    lArmLocs.append(lElbowPosLocName)
    lWristPosLocName = lSide + 'wristPos_Loc'
    lArmLocs.append(lWristPosLocName)
    lHipPosLocName = lSide + 'hipPos_Loc'
    lLegLocs.append(lHipPosLocName)
    lKneePosLocName = lSide + 'kneePos_Loc'
    lLegLocs.append(lKneePosLocName)
    lFootPosLocName = lSide + 'footPos_Loc'
    lLegLocs.append(lFootPosLocName)
    lBallPosLocName = lSide + 'ballPos_Loc'
    lLegLocs.append(lBallPosLocName)
    lToePosLocName = lSide + 'toePos_Loc'
    lLegLocs.append(lToePosLocName)
    rClaviclePosLocName = rSide + 'claviclePos_Loc'
    rArmLocs.append(rClaviclePosLocName)
    rShoulderPosLocName = rSide + 'shoulderPos_Loc'
    rArmLocs.append(rShoulderPosLocName)
    rElbowPosLocName = rSide + 'elbowPos_Loc'
    rArmLocs.append(rElbowPosLocName)
    rWristPosLocName = rSide + 'wristPos_Loc'
    rArmLocs.append(rWristPosLocName)
    rHipPosLocName = rSide + 'hipPos_Loc'
    rLegLocs.append(rHipPosLocName)
    rKneePosLocName = rSide + 'kneePos_Loc'
    rLegLocs.append(rKneePosLocName)
    rFootPosLocName = rSide + 'footPos_Loc'
    rLegLocs.append(rFootPosLocName)
    rBallPosLocName = rSide + 'ballPos_Loc'
    rLegLocs.append(rBallPosLocName)
    rToePosLocName = rSide + 'toePos_Loc'
    rLegLocs.append(rToePosLocName)
        
    lThumbBasePosLocName = lSide + 'thumbBasePos_Loc'
    lHandLocs.append(lThumbBasePosLocName)
    lThumb01PosLocName = lSide + 'thumb01Pos_Loc'
    lHandLocs.append(lThumb01PosLocName)
    lThumb02PosLocName = lSide + 'thumb02Pos_Loc'
    lHandLocs.append(lThumb02PosLocName)
    lThumb03PosLocName = lSide + 'thumb03Pos_Loc'
    lHandLocs.append(lThumb03PosLocName)
    lThumbEndPosLocName = lSide + 'thumbEndPos_Loc'
    lHandLocs.append(lThumbEndPosLocName)
    lIndexBasePosLocName = lSide + 'indexBasePos_Loc'
    lHandLocs.append(lIndexBasePosLocName)
    lIndex01PosLocName = lSide + 'index01Pos_Loc'
    lHandLocs.append(lIndex01PosLocName)
    lIndex02PosLocName = lSide + 'index02Pos_Loc'
    lHandLocs.append(lIndex02PosLocName)
    lIndex03PosLocName = lSide + 'index03Pos_Loc'
    lHandLocs.append(lIndex03PosLocName)
    lIndexEndPosLocName = lSide + 'indexEndPos_Loc'
    lHandLocs.append(lIndexEndPosLocName)
    lMiddleBasePosLocName = lSide + 'middleBasePos_Loc'
    lHandLocs.append(lMiddleBasePosLocName)
    lMiddle01PosLocName = lSide + 'middle01Pos_Loc'
    lHandLocs.append(lMiddle01PosLocName)
    lMiddle02PosLocName = lSide + 'middle02Pos_Loc'
    lHandLocs.append(lMiddle02PosLocName)
    lMiddle03PosLocName = lSide + 'middle03Pos_Loc'
    lHandLocs.append(lMiddle03PosLocName)
    lMiddleEndPosLocName = lSide + 'middleEndPos_Loc'
    lHandLocs.append(lMiddleEndPosLocName)
    lRingBasePosLocName = lSide + 'ringBasePos_Loc'
    lHandLocs.append(lRingBasePosLocName)
    lRing01PosLocName = lSide + 'ring01Pos_Loc'
    lHandLocs.append(lRing01PosLocName)
    lRing02PosLocName = lSide + 'ring02Pos_Loc'
    lHandLocs.append(lRing02PosLocName)
    lRing03PosLocName = lSide + 'ring03Pos_Loc'
    lHandLocs.append(lRing03PosLocName)
    lRingEndPosLocName = lSide + 'ringEndPos_Loc'
    lHandLocs.append(lRingEndPosLocName)
    lPinkyBasePosLocName = lSide + 'pinkyBasePos_Loc'
    lHandLocs.append(lPinkyBasePosLocName)
    lPinky01PosLocName = lSide + 'pinky01Pos_Loc'
    lHandLocs.append(lPinky01PosLocName)
    lPinky02PosLocName = lSide + 'pinky02Pos_Loc'
    lHandLocs.append(lPinky02PosLocName)
    lPinky03PosLocName = lSide + 'pinky03Pos_Loc'
    lHandLocs.append(lPinky03PosLocName)
    lPinkyEndPosLocName = lSide + 'pinkyEndPos_Loc'
    lHandLocs.append(lPinkyEndPosLocName)
    rThumbBasePosLocName = rSide + 'thumbBasePos_Loc'
    rHandLocs.append(rThumbBasePosLocName)
    rThumb01PosLocName = rSide + 'thumb01Pos_Loc'
    rHandLocs.append(rThumb01PosLocName)
    rThumb02PosLocName = rSide + 'thumb02Pos_Loc'
    rHandLocs.append(rThumb02PosLocName)
    rThumb03PosLocName = rSide + 'thumb03Pos_Loc'
    rHandLocs.append(rThumb03PosLocName)
    rThumbEndPosLocName = rSide + 'thumbEndPos_Loc'
    rHandLocs.append(rThumbEndPosLocName)
    rIndexBasePosLocName = rSide + 'indexBasePos_Loc'
    rHandLocs.append(rIndexBasePosLocName)
    rIndex01PosLocName = rSide + 'index01Pos_Loc'
    rHandLocs.append(rIndex01PosLocName)
    rIndex02PosLocName = rSide + 'index02Pos_Loc'
    rHandLocs.append(rIndex02PosLocName)
    rIndex03PosLocName = rSide + 'index03Pos_Loc'
    rHandLocs.append(rIndex03PosLocName)
    rIndexEndPosLocName = rSide + 'indexEndPos_Loc'
    rHandLocs.append(rIndexEndPosLocName)
    rMiddleBasePosLocName = rSide + 'middleBasePos_Loc'
    rHandLocs.append(rMiddleBasePosLocName)
    rMiddle01PosLocName = rSide + 'middle01Pos_Loc'
    rHandLocs.append(rMiddle01PosLocName)
    rMiddle02PosLocName = rSide + 'middle02Pos_Loc'
    rHandLocs.append(rMiddle02PosLocName)
    rMiddle03PosLocName = rSide + 'middle03Pos_Loc'
    rHandLocs.append(rMiddle03PosLocName)
    rMiddleEndPosLocName = rSide + 'middleEndPos_Loc'
    rHandLocs.append(rMiddleEndPosLocName)
    rRingBasePosLocName = rSide + 'ringBasePos_Loc'
    rHandLocs.append(rRingBasePosLocName)
    rRing01PosLocName = rSide + 'ring01Pos_Loc'
    rHandLocs.append(rRing01PosLocName)
    rRing02PosLocName = rSide + 'ring02Pos_Loc'
    rHandLocs.append(rRing02PosLocName)
    rRing03PosLocName = rSide + 'ring03Pos_Loc'
    rHandLocs.append(rRing03PosLocName)
    rRingEndPosLocName = rSide + 'ringEndPos_Loc'
    rHandLocs.append(rRingEndPosLocName)
    rPinkyBasePosLocName = rSide + 'pinkyBasePos_Loc'
    rHandLocs.append(rPinkyBasePosLocName)
    rPinky01PosLocName = rSide + 'pinky01Pos_Loc'
    rHandLocs.append(rPinky01PosLocName)
    rPinky02PosLocName = rSide + 'pinky02Pos_Loc'
    rHandLocs.append(rPinky02PosLocName)
    rPinky03PosLocName = rSide + 'pinky03Pos_Loc'
    rHandLocs.append(rPinky03PosLocName)
    rPinkyEndPosLocName = rSide + 'pinkyEndPos_Loc'
    rHandLocs.append(rPinkyEndPosLocName)

    for l in spineLocs:
        cmds.spaceLocator(n = l)
    for l in lArmLocs:
        cmds.spaceLocator(n = l)
    for l in rArmLocs:
        cmds.spaceLocator(n = l)    
    for l in lLegLocs:
        cmds.spaceLocator(n = l)
    for l in rLegLocs:
        cmds.spaceLocator(n = l)
    for l in lHandLocs:
        cmds.spaceLocator(n = l)    
    for l in rHandLocs:
        cmds.spaceLocator(n = l)
    
    cmds.xform(pelvisPosLocName, t = (posList[1][0], posList[1][1], posList[1][2]), ws = True)
    cmds.xform(spinePosLocName, t = (posList[2][0], posList[2][1], posList[2][2]), ws = True)
    cmds.xform(neckPosLocName, t = (posList[3][0], posList[3][1], posList[3][2]), ws = True)
    cmds.xform(headPosLocName, t = (posList[4][0], posList[4][1], posList[4][2]), ws = True)
    cmds.xform(lClaviclePosLocName, t = (posList[5][0], posList[5][1], posList[5][2]), ws = True)
    cmds.xform(lShoulderPosLocName, t = (posList[6][0], posList[6][1], posList[6][2]), ws = True)
    cmds.xform(lElbowPosLocName, t = (posList[7][0], posList[7][1], posList[7][2]), ws = True)
    cmds.xform(lWristPosLocName, t = (posList[8][0], posList[8][1], posList[8][2]), ws = True)
    cmds.xform(lHipPosLocName, t = (posList[9][0], posList[9][1], posList[9][2]), ws = True)
    cmds.xform(lKneePosLocName, t = (posList[10][0], posList[10][1], posList[10][2]), ws = True)
    cmds.xform(lFootPosLocName, t = (posList[11][0], posList[11][1], posList[11][2]), ws = True)
    cmds.xform(lBallPosLocName, t = (posList[12][0], posList[12][1], posList[12][2]), ws = True)
    cmds.xform(lToePosLocName, t = (posList[13][0], posList[13][1], posList[13][2]), ws = True)
    cmds.xform(lThumbBasePosLocName, t = (posList[14][0], posList[14][1], posList[14][2]), ws = True)
    cmds.xform(lThumb01PosLocName, t = (posList[15][0], posList[15][1], posList[15][2]), ws = True)
    cmds.xform(lThumb02PosLocName, t = (posList[16][0], posList[16][1], posList[16][2]), ws = True)
    cmds.xform(lThumb03PosLocName, t = (posList[17][0], posList[17][1], posList[17][2]), ws = True)
    cmds.xform(lThumbEndPosLocName, t = (posList[18][0], posList[18][1], posList[18][2]), ws = True)
    cmds.xform(lIndexBasePosLocName, t = (posList[19][0], posList[19][1], posList[19][2]), ws = True)
    cmds.xform(lIndex01PosLocName, t = (posList[20][0], posList[20][1], posList[20][2]), ws = True)
    cmds.xform(lIndex02PosLocName, t = (posList[21][0], posList[21][1], posList[21][2]), ws = True)
    cmds.xform(lIndex03PosLocName, t = (posList[22][0], posList[22][1], posList[22][2]), ws = True)
    cmds.xform(lIndexEndPosLocName, t = (posList[23][0], posList[23][1], posList[23][2]), ws = True)
    cmds.xform(lMiddleBasePosLocName, t = (posList[24][0], posList[24][1], posList[24][2]), ws = True)
    cmds.xform(lMiddle01PosLocName, t = (posList[25][0], posList[25][1], posList[25][2]), ws = True)
    cmds.xform(lMiddle02PosLocName, t = (posList[26][0], posList[26][1], posList[26][2]), ws = True)
    cmds.xform(lMiddle03PosLocName, t = (posList[27][0], posList[27][1], posList[27][2]), ws = True)
    cmds.xform(lMiddleEndPosLocName, t = (posList[28][0], posList[28][1], posList[28][2]), ws = True)
    cmds.xform(lRingBasePosLocName, t = (posList[29][0], posList[29][1], posList[29][2]), ws = True)
    cmds.xform(lRing01PosLocName, t = (posList[30][0], posList[30][1], posList[30][2]), ws = True)
    cmds.xform(lRing02PosLocName, t = (posList[31][0], posList[31][1], posList[31][2]), ws = True)
    cmds.xform(lRing03PosLocName, t = (posList[32][0], posList[32][1], posList[32][2]), ws = True)
    cmds.xform(lRingEndPosLocName, t = (posList[33][0], posList[33][1], posList[33][2]), ws = True)
    cmds.xform(lPinkyBasePosLocName, t = (posList[34][0], posList[34][1], posList[34][2]), ws = True)
    cmds.xform(lPinky01PosLocName, t = (posList[35][0], posList[35][1], posList[35][2]), ws = True)
    cmds.xform(lPinky02PosLocName, t = (posList[36][0], posList[36][1], posList[36][2]), ws = True)
    cmds.xform(lPinky03PosLocName, t = (posList[37][0], posList[37][1], posList[37][2]), ws = True)
    cmds.xform(lPinkyEndPosLocName, t = (posList[38][0], posList[38][1], posList[38][2]), ws = True)
        
    for index, l in enumerate(lArmLocs):
        mirrorConnect(lArmLocs[index], rArmLocs[index], 'x')
    for index, l in enumerate(lLegLocs):
        mirrorConnect(lLegLocs[index], rLegLocs[index], 'x')
    for index, l in enumerate(lHandLocs):
        mirrorConnect(lHandLocs[index], rHandLocs[index], 'x')
    
    cmds.group(n = 'localScale_Grp', em = True)
    cmds.group(n = 'heightScale_Grp', em = True)
    cmds.parent('heightScale_Grp', 'localScale_Grp')
    cmds.parent(heightLocName, 'localScale_Grp')
    cmds.connectAttr(heightLocName + '.scale', 'localScale_Grp.scale')
    cmds.createNode('multiplyDivide', n = 'heightScale_Mult')
    cmds.setAttr('heightScale_Mult.operation', 2)
    cmds.setAttr('heightScale_Mult.input2X', 180.34)
    cmds.connectAttr(heightLocName + '.translateY', 'heightScale_Mult.input1X')
    cmds.connectAttr('heightScale_Mult.outputX', 'heightScale_Grp.scaleX')
    cmds.connectAttr('heightScale_Mult.outputX', 'heightScale_Grp.scaleY')
    cmds.connectAttr('heightScale_Mult.outputX', 'heightScale_Grp.scaleZ')
    
    if wings == True:
        lWingPosLocName = lSide + 'wingPos_Loc'
        wingLocs.append(lWingPosLocName)
        rWingPosLocName = rSide + 'wingPos_Loc'
        wingLocs.append(rWingPosLocName)
        for l in wingLocs:
            cmds.spaceLocator(n = l)
        cmds.xform(lWingPosLocName, t = (4.809, 139.016, -9.579), ws = True)
        mirrorConnect(lWingPosLocName, rWingPosLocName, 'x')
        for l in wingLocs:
            cmds.setAttr(l + '.localScaleX', locScale)
            cmds.setAttr(l + '.localScaleY', locScale)
            cmds.setAttr(l + '.localScaleZ', locScale)
            cmds.parent(l, 'heightScale_Grp')
        
    cmds.select(cl = True)

    for l in spineLocs:
        cmds.setAttr(l + '.localScaleX', locScale)
        cmds.setAttr(l + '.localScaleY', locScale)
        cmds.setAttr(l + '.localScaleZ', locScale)
        cmds.parent(l, 'heightScale_Grp')
        spinePosJnts.append(makeJntAt(l, 4, '_PosJnt'))
    for index in range(0, (len(spinePosJnts)-1)):
        cmds.parent(spinePosJnts[index + 1], spinePosJnts[index])
    jntOrient(spinePosJnts[0], 'spine')
    
    for l in lArmLocs:
        cmds.setAttr(l + '.localScaleX', locScale)
        cmds.setAttr(l + '.localScaleY', locScale)
        cmds.setAttr(l + '.localScaleZ', locScale)
        cmds.parent(l, 'heightScale_Grp')      
        lArmPosJnts.append(makeJntAt(l, 3, '_PosJnt'))
    for index in range(0, (len(lArmPosJnts)-1)):
        cmds.parent(lArmPosJnts[index + 1], lArmPosJnts[index])
    jntOrient(lArmPosJnts[0], 'lArm')
    
    for l in rArmLocs:
        cmds.setAttr(l + '.localScaleX', locScale)
        cmds.setAttr(l + '.localScaleY', locScale)
        cmds.setAttr(l + '.localScaleZ', locScale)
        cmds.parent(l, 'heightScale_Grp')
        rArmPosJnts.append(makeJntAt(l, 3, '_PosJnt'))
    for index in range(0, (len(rArmPosJnts)-1)):
        cmds.parent(rArmPosJnts[index + 1], rArmPosJnts[index])
          
    for l in lLegLocs:
        cmds.setAttr(l + '.localScaleX', locScale)
        cmds.setAttr(l + '.localScaleY', locScale)
        cmds.setAttr(l + '.localScaleZ', locScale)
        cmds.parent(l, 'heightScale_Grp')
        lLegPosJnts.append(makeJntAt(l, 3, '_PosJnt'))
    for index in range(0, (len(lLegPosJnts)-1)):
        cmds.parent(lLegPosJnts[index + 1], lLegPosJnts[index])
    jntOrient(lLegPosJnts[0], 'lLeg')
    
    for l in rLegLocs:
        cmds.setAttr(l + '.localScaleX', locScale)
        cmds.setAttr(l + '.localScaleY', locScale)
        cmds.setAttr(l + '.localScaleZ', locScale)
        cmds.parent(l, 'heightScale_Grp')
        rLegPosJnts.append(makeJntAt(l, 3, '_PosJnt'))
    for index in range(0, (len(rLegPosJnts)-1)):
        cmds.parent(rLegPosJnts[index + 1], rLegPosJnts[index])
    
    for l in lHandLocs:
        cmds.setAttr(l + '.localScaleX', locScale)
        cmds.setAttr(l + '.localScaleY', locScale)
        cmds.setAttr(l + '.localScaleZ', locScale)
        cmds.parent(l, 'heightScale_Grp')
        lHandPosJnts.append(makeJntAt(l, 1.5, '_PosJnt'))
    for index, j in enumerate(lHandPosJnts):
        if index > -1 and index < 4:
            cmds.parent(lHandPosJnts[index + 1], lHandPosJnts[index])
        if index > 4 and index < 9:
            cmds.parent(lHandPosJnts[index + 1], lHandPosJnts[index])
        if index > 9 and index < 14:
            cmds.parent(lHandPosJnts[index + 1], lHandPosJnts[index])
        if index > 14 and index < 19:
            cmds.parent(lHandPosJnts[index + 1], lHandPosJnts[index])
        if index > 19 and index < 24:
            cmds.parent(lHandPosJnts[index + 1], lHandPosJnts[index])
    for index in range(0, 21, 5):
        jntOrient(lHandPosJnts[index], 'lArm')
        cmds.parent(lHandPosJnts[index], lArmPosJnts[3])
        
    for l in rHandLocs:
        cmds.setAttr(l + '.localScaleX', locScale)
        cmds.setAttr(l + '.localScaleY', locScale)
        cmds.setAttr(l + '.localScaleZ', locScale)
        cmds.parent(l, 'heightScale_Grp') 
        rHandPosJnts.append(makeJntAt(l, 1.5, '_PosJnt'))
    for index, j in enumerate(rHandPosJnts):
        if index > -1 and index < 4:
            cmds.parent(rHandPosJnts[index + 1], rHandPosJnts[index])
        if index > 4 and index < 9:
            cmds.parent(rHandPosJnts[index + 1], rHandPosJnts[index])
        if index > 9 and index < 14:
            cmds.parent(rHandPosJnts[index + 1], rHandPosJnts[index])
        if index > 14 and index < 19:
            cmds.parent(rHandPosJnts[index + 1], rHandPosJnts[index])
        if index > 19 and index < 24:
            cmds.parent(rHandPosJnts[index + 1], rHandPosJnts[index])
    for index in range(0, 21, 5):
        jntOrient(rHandPosJnts[index], 'rArm')
        cmds.parent(rHandPosJnts[index], rArmPosJnts[3])
        
    orientMatch(rLegPosJnts[0], lLegPosJnts[0])  
    orientMatch(rArmPosJnts[0], lArmPosJnts[0])  
    
    cmds.parent(lArmPosJnts[0], rArmPosJnts[0], spinePosJnts[1])
    cmds.parent(lLegPosJnts[0], rLegPosJnts[0], spinePosJnts[0])
    
    for index, l in enumerate(lArmLocs):
        connectTRS(lArmPosJnts[index], rArmPosJnts[index], 'r')
        cmds.pointConstraint(lArmPosJnts[index], l, mo = False)
        cmds.pointConstraint(rArmLocs[index], rArmPosJnts[index], mo = False)
        
    for index, l in enumerate(lLegLocs):
        connectTRS(lLegPosJnts[index], rLegPosJnts[index], 'r')
        cmds.parentConstraint(lLegPosJnts[index], l, mo = False)
        cmds.pointConstraint(rLegLocs[index], rLegPosJnts[index], mo = False)
        
    for index, l in enumerate(lHandLocs):
        connectTRS(lHandPosJnts[index], rHandPosJnts[index], 'r')
        cmds.parentConstraint(lHandPosJnts[index], l, mo = False)
        cmds.pointConstraint(rHandLocs[index], rHandPosJnts[index], mo = False)
                
    for index, j in enumerate(lHandPosJnts):
        cmds.connectAttr(lHandPosJnts[index] + '.jointOrient', rHandPosJnts[index] + '.jointOrient')
               
    for index, j in enumerate(lArmPosJnts):
        if index > 0:
            cmds.connectAttr(lArmPosJnts[index] + '.jointOrient', rArmPosJnts[index] + '.jointOrient')

    for index, j in enumerate(lLegPosJnts):
        if index > 0:
            cmds.connectAttr(lLegPosJnts[index] + '.jointOrient', rLegPosJnts[index] + '.jointOrient')

    if wings == True:
        return spineLocs, lArmLocs, rArmLocs, lLegLocs, rLegLocs, lHandLocs, rHandLocs, heightLocName, 'localScale_Grp', spinePosJnts[0], wingLocs
    else:
        return spineLocs, lArmLocs, rArmLocs, lLegLocs, rLegLocs, lHandLocs, rHandLocs, heightLocName, 'localScale_Grp', spinePosJnts[0]

def autoSpine(locList, jntScale, rigGrp):
    baseJnts = []
    bindList = []
        
    #Make and Parents Joints
    for l in locList:
        baseJnts.append(makeJntAt(l, jntScale, '_B_Jnt'))
    for index in range(0, (len(locList)-1)):
        cmds.parent(baseJnts[index + 1], baseJnts[index])
        
    #Orients Joints
    jntOrient(baseJnts[0], 'spine')
    
    cmds.select(baseJnts[0])
    jntSegCreate(6, 'spine_B_Jnt')
    
    cmds.parent(baseJnts[2], w = True)
    neckJnt = baseJnts[2]
    cmds.select(baseJnts[0], hi = True)
    baseJnts = cmds.ls(sl = True)
    
    #Naming and Organization
    spineJnts = []
    for index, j in enumerate(baseJnts):
        if index == 0:
            spineJnts.append(j)
        else:
            name = 'spine_B_Jnt_0' + str(index)
            cmds.rename(j, name)
            spineJnts.append(name)
        
    #Spine spline setup
    spineCtrlJnts = []
    pelvisCtrlJntName = 'pelvis_Ctrl_Jnt'
    spineCtrlJntName = 'spine_Ctrl_Jnt'
    spineCtrlJnts.append(pelvisCtrlJntName)
    spineCtrlJnts.append(spineCtrlJntName)

    pos = []
    for index, s in enumerate(spineJnts):
        if index % 2 == 0:
            pos.append(cmds.xform(s, q = True, t = True, ws = True))
        if index == 0:
            cmds.duplicate(s, po = True, n = pelvisCtrlJntName)
        if index == 6:
            cmds.duplicate(s, po = True, n = spineCtrlJntName)

    spineCrvName = 'spine_Crv'
    cmds.curve(p = pos, n = spineCrvName)
    cmds.setAttr(spineCrvName + '.inheritsTransform', 0)
    cmds.setAttr(spineCrvName + '.v', 0)
    checkPar = cmds.listRelatives(pelvisCtrlJntName, p = True) 
    if checkPar:
        cmds.parent(pelvisCtrlJntName, w = True)
    checkPar = cmds.listRelatives(spineCtrlJntName, p = True) 
    if checkPar:
        cmds.parent(spineCtrlJntName, w = True)
    cmds.setAttr(pelvisCtrlJntName + '.radius', jntScale * 5 / 3)
    cmds.setAttr(spineCtrlJntName + '.radius', jntScale * 5 / 3)
    ctrlJntOrientX = cmds.getAttr(spineJnts[0] + '.jointOrientX')
    ctrlJntOrientY = cmds.getAttr(spineJnts[0] + '.jointOrientY')
    ctrlJntOrientZ = cmds.getAttr(spineJnts[0] + '.jointOrientZ')

    for j in spineCtrlJnts:
        cmds.setAttr(j + '.jointOrientX', ctrlJntOrientX)
        cmds.setAttr(j + '.jointOrientY', ctrlJntOrientY)
        cmds.setAttr(j + '.jointOrientZ', ctrlJntOrientZ)

    spineIkName = 'spine_Ik'
    cmds.select(spineJnts[0], spineJnts[6], spineCrvName)
    cmds.ikHandle(sol = 'ikSplineSolver', c = spineCrvName, ccv = False, snc = True, pcv = False, n = spineIkName)
    cmds.setAttr(spineIkName + '.visibility', 0)
    cmds.setAttr(spineIkName + '.dTwistControlEnable', 1)
    cmds.setAttr(spineIkName + '.dWorldUpType', 4)
    cmds.setAttr(spineIkName + '.dWorldUpVectorX', 0)
    cmds.setAttr(spineIkName + '.dWorldUpVectorY', 1)
    cmds.setAttr(spineIkName + '.dWorldUpVectorZ', 0)
    cmds.setAttr(spineIkName + '.dWorldUpVectorEndX', 0)
    cmds.setAttr(spineIkName + '.dWorldUpVectorEndY', 1)
    cmds.setAttr(spineIkName + '.dWorldUpVectorEndZ', 0)
    cmds.connectAttr(spineCtrlJnts[0] + '.worldMatrix[0]', spineIkName + '.dWorldUpMatrix')
    cmds.connectAttr(spineCtrlJnts[1] + '.worldMatrix[0]', spineIkName + '.dWorldUpMatrixEnd')

    cmds.select(spineCtrlJnts[0], spineCtrlJnts[1], spineCrvName)
    cmds.skinCluster(tsb = True, dr = 4, mi = 2)

    pelvisOff, pelvisCtrl = makeCtrl(spineCtrlJnts[0], 3.5, True)
    upperBodyOff, upperBodyCtrl = makeCtrl(spineCtrlJnts[1], 2.8, True)
    
    upperBodyGrpName = 'upperBodyGrp'
    makeGrpAt(spineJnts[6], upperBodyGrpName)
    cmds.setAttr(upperBodyGrpName + '.rotateY', 0)
    cmds.pointConstraint(spineJnts[6], upperBodyGrpName, mo = False)
    cmds.orientConstraint(upperBodyCtrl, upperBodyGrpName, mo = False)

    spineRigGrpName = 'spineRig_Grp'
    cmds.group(em = True, n = spineRigGrpName)
    cmds.parent(spineJnts[0], spineIkName, spineCrvName, upperBodyGrpName, spineCtrlJnts[0], spineCtrlJnts[1], pelvisOff, upperBodyOff, spineRigGrpName)
    cmds.parent(spineRigGrpName, rigGrp)
    
    spineFk1 = makeCtrl(spineJnts[2], 4, False)
    spineFk2 = makeCtrl(spineJnts[4], 4, False)
    spineFkCtrl1Name = 'spine_Fk_01_Ctrl'
    spineFkCtrl2Name = 'spine_Fk_02_Ctrl'
    spineFkOff1Name = 'spine_Fk_01_Off'
    spineFkOff2Name = 'spine_Fk_02_Off'
    spineFkCtrl1 = cmds.rename(spineFk1[1], spineFkCtrl1Name)
    spineFkCtrl2 = cmds.rename(spineFk2[1], spineFkCtrl2Name)
    spineFkOff1 = cmds.rename(spineFk1[0], spineFkOff1Name)
    spineFkOff2 = cmds.rename(spineFk2[0], spineFkOff2Name)
    
    cmds.parent(spineFkOff2, spineFkCtrl1)
    cmds.parent(upperBodyOff, spineFkCtrl2)
    
    for index in range(0, 7):
        bindList.append(spineJnts[index])
    
    return spineJnts, bindList, neckJnt, upperBodyGrpName, pelvisOff, pelvisCtrl, upperBodyOff, upperBodyCtrl, spineFkOff1

def autoNeck(baseJnt, rigGrp, upperBodyCtrl, upperBodyGrp, jntScale):
    bindList = []
    cmds.select(baseJnt)
    jntSegCreate(3, 'mid_Jnt')
    cmds.select(baseJnt, hi = True)
    neckJnts = cmds.ls(sl = True)
    
    #Neck spline setup
    neckCtrlJnts = []
    neckBaseCtrlJntName = 'neckBase_Ctrl_Jnt'
    neckEndCtrlJntName = 'neckEnd_Ctrl_Jnt'
    neckCtrlJnts.append(neckBaseCtrlJntName)
    neckCtrlJnts.append(neckEndCtrlJntName)
    cmds.duplicate(neckJnts[0], po = True, n = neckBaseCtrlJntName)
    cmds.duplicate(neckJnts[3], po = True, n = neckEndCtrlJntName)
    cmds.setAttr(neckBaseCtrlJntName + '.radius', jntScale * 5 / 3)
    cmds.setAttr(neckEndCtrlJntName + '.radius', jntScale * 5 / 3)
    neckJnts[0] = cmds.rename(neckJnts[0], 'neck_B_Jnt_00')
    neckJnts[1] = cmds.rename(neckJnts[1], 'neck_B_Jnt_01')
    neckJnts[2] = cmds.rename(neckJnts[2], 'neck_B_Jnt_02')
    neckJnts[3] = cmds.rename(neckJnts[3], 'head_Pos_Jnt')
    headJntName = 'head_B_Jnt'
    headJnt = cmds.duplicate(neckJnts[3], po = True, n = headJntName)
    cmds.setAttr(headJntName + '.radius', jntScale * 5 / 4)

    pos = []
    for index, s in enumerate(neckJnts):
        pos.append(cmds.xform(s, q = True, t = True, ws = True))
        
    neckCrvName = 'neck_Crv'
    cmds.curve(p = pos, n = neckCrvName)
    cmds.setAttr(neckCrvName + '.inheritsTransform', 0)
    cmds.setAttr(neckCrvName + '.v', 0)

    checkPar = cmds.listRelatives(neckBaseCtrlJntName, p = True) 
    if checkPar:
        cmds.parent(neckBaseCtrlJntName, w = True)
    checkPar = cmds.listRelatives(neckEndCtrlJntName, p = True) 
    if checkPar:
        cmds.parent(neckEndCtrlJntName, w = True)

    neckIkName = 'neck_IK'
    cmds.select(neckJnts[0], neckJnts[3], neckCrvName)
    neckIk = cmds.ikHandle(sol = 'ikSplineSolver', c = neckCrvName, ccv = False, snc = True, pcv = False, n = neckIkName)
    cmds.setAttr(neckIkName + '.visibility', 0)
    cmds.setAttr(neckIkName + '.dTwistControlEnable', 1)
    cmds.setAttr(neckIkName + '.dWorldUpType', 4)
    cmds.setAttr(neckIkName + '.dWorldUpVectorX', 0)
    cmds.setAttr(neckIkName + '.dWorldUpVectorY', 1)
    cmds.setAttr(neckIkName + '.dWorldUpVectorZ', 0)
    cmds.setAttr(neckIkName + '.dWorldUpVectorEndX', 0)
    cmds.setAttr(neckIkName + '.dWorldUpVectorEndY', 1)
    cmds.setAttr(neckIkName + '.dWorldUpVectorEndZ', 0)
    cmds.connectAttr(neckCtrlJnts[0] + '.worldMatrix[0]', neckIkName + '.dWorldUpMatrix')
    cmds.connectAttr(neckCtrlJnts[1] + '.worldMatrix[0]', neckIkName + '.dWorldUpMatrixEnd')
    
    cmds.select(neckCtrlJnts[0], neckCtrlJnts[1], neckCrvName)
    cmds.skinCluster(tsb = True, dr = 4, mi = 2)
    
    neckBaseOff, neckBaseCtrl = makeCtrl(neckCtrlJnts[0], 2, True)
    neckEndOff, neckEndCtrl = makeCtrl(neckCtrlJnts[1], 2, True)
    
    neckRigGrpName = 'neckRig_Grp'
    cmds.group(em = True, n = neckRigGrpName)
    cmds.parent(headJntName, neckRigGrpName)

    cmds.parent(neckBaseOff, upperBodyCtrl)
    cmds.parent(neckEndOff, neckBaseCtrl)
    cmds.parentConstraint(upperBodyGrp, neckBaseOff, mo = True)
    
    cmds.parent(neckJnts[0], neckIkName, neckCrvName, neckCtrlJnts, neckRigGrpName)
    cmds.parent(neckRigGrpName, rigGrp)
    cmds.pointConstraint(neckJnts[3], headJnt, mo = False)
    cmds.orientConstraint(neckEndCtrl, headJnt, mo = False)
    
    #Fill Bind List
    for index in range(0, 3):
        bindList.append(neckJnts[index])
    bindList.append(headJntName)
    
    return neckJnts, bindList

def autoArm(locList, jntScale, side, lArmJnts, rootCtrl, armCtrlNum):
    baseJnts = []
    fkOffs = []
    fkCtrls = []
    bindList = []
    
    mainLocName = side + 'arm_spaceLoc'
    mainLoc = cmds.spaceLocator(n = mainLocName)
    clavicleTran = cmds.xform(locList[0], q = True, t = True, ws = True)
    cmds.xform(mainLocName, t = clavicleTran, ws = True)
    cmds.setAttr(mainLocName + 'Shape.localScaleX', 5)
    cmds.setAttr(mainLocName + 'Shape.localScaleY', 5)
    cmds.setAttr(mainLocName + 'Shape.localScaleZ', 5)
    
    armRigGrp = side + 'armRigGrp'
    cmds.group(em = True, n = armRigGrp)
    cmds.setAttr(armRigGrp + '.inheritsTransform', 0)
    
    #Makes and Parents Joints
    for l in locList:
        baseJnts.append(makeJntAt(l, jntScale, '_B_Jnt'))
    for index in range(0, (len(locList)-1)):
        cmds.parent(baseJnts[index + 1], baseJnts[index])
    
    #Orients Joints
    if side == 'L_':
        jntOrient(baseJnts[0], 'lArm')
    if side == 'R_':
        orientMatch(baseJnts[0], lArmJnts[0])
    setJointAngle(baseJnts[2], '+y')
    
    #Settings Control
    settingsName = side + 'armSettings_Ctrl'
    settingsCtrl = makeShape('cube', settingsName)
    settingsGrp = cmds.group(settingsCtrl, n = (side + 'armSettings_Grp'))
    settingsConstraintName = side + 'armSettingsGrp_ParConstraint'
    cmds.parentConstraint(baseJnts[3], settingsGrp, mo = False, n = settingsConstraintName)
    if side == 'L_':
        cmds.setAttr(settingsCtrl + '.translateZ', -14)
    if side == 'R_':
        cmds.setAttr(settingsCtrl + '.translateZ', 14)
    cmds.setAttr(settingsCtrl + '.scale', 3, 3, 3)
    cmds.addAttr(settingsCtrl, ln = 'IkFkSwitch', nn = 'Ik/Fk Switch', at = 'float', dv = 1, min = 0, max = 1, k = True, h = False)
    cmds.addAttr(settingsCtrl, ln = 'FkIkSwitch', nn = 'Fk/Ik Switch', at = 'float', dv = 0, min = 0, max = 1, k = True, h = True)
    cmds.setDrivenKeyframe(settingsCtrl + '.FkIkSwitch', cd = settingsCtrl + '.IkFkSwitch')
    cmds.setAttr(settingsCtrl + '.IkFkSwitch', 0)
    cmds.setAttr(settingsCtrl + '.FkIkSwitch', 1)
    cmds.setDrivenKeyframe(settingsCtrl + '.FkIkSwitch', cd = settingsCtrl + '.IkFkSwitch')
    cmds.selectKey(settingsCtrl + '_FkIkSwitch', k = True, f = (0, 1))
    cmds.keyTangent(itt = 'clamped', ott = 'clamped')
    cmds.setAttr(settingsCtrl + '.IkFkSwitch', 1)
    
    #Limb Duplication
    fkJnts = duplicateJntChain(baseJnts, '_B_', '_Fk_')
    ikJnts = duplicateJntChain(baseJnts, '_B_', '_Ik_')    
        
    upperArmTwist = makeLimbTwistJnt(baseJnts[1], 6)
    lowerArmTwist = makeLimbTwistJnt(baseJnts[2], 6)

    cmds.select(upperArmTwist[0])
    upperTwistCtrlJnts = makeSplineCtrls(armCtrlNum)
    cmds.select(lowerArmTwist[0])
    lowerTwistCtrlJnts = makeSplineCtrls(armCtrlNum)
                
    for index, j in enumerate(upperTwistCtrlJnts):
        name = str(j).replace('_00', '')
        upperTwistCtrlJnts[index] = cmds.rename(upperTwistCtrlJnts[index], name)      
    
    if armCtrlNum == 2:     
        upperTwistCtrlJnts.append(justGrp(upperTwistCtrlJnts[0], 'Jnt', 'Off', True))
        upperTwistCtrlJnts.append(justGrp(upperTwistCtrlJnts[1], 'Jnt', 'Off', True))
    if armCtrlNum == 3:
        temp = upperTwistCtrlJnts[2]
        del upperTwistCtrlJnts[2]
        upperTwistCtrlJnts.append(justGrp(upperTwistCtrlJnts[0], 'Jnt', 'Off', True))
        upperTwistCtrlJnts.append(justGrp(upperTwistCtrlJnts[1], 'Jnt', 'Off', True))
        upperTwistCtrlJnts.append(temp)
        upperTwistCtrlJnts.append(justGrp(upperTwistCtrlJnts[4], 'Jnt', 'Off', True))

    for index, j in enumerate(lowerTwistCtrlJnts):
        name = str(j).replace('_00', '')
        lowerTwistCtrlJnts[index] = cmds.rename(lowerTwistCtrlJnts[index], name)           

    if armCtrlNum == 2:
        lowerTwistCtrlJnts.append(justGrp(lowerTwistCtrlJnts[0], 'Jnt', 'Off', True))
        lowerTwistCtrlJnts.append(justGrp(lowerTwistCtrlJnts[1], 'Jnt', 'Off', True))
    if armCtrlNum == 3:
        temp = lowerTwistCtrlJnts[2]
        del lowerTwistCtrlJnts[2]
        lowerTwistCtrlJnts.append(justGrp(lowerTwistCtrlJnts[0], 'Jnt', 'Off', True))
        lowerTwistCtrlJnts.append(justGrp(lowerTwistCtrlJnts[1], 'Jnt', 'Off', True))
        lowerTwistCtrlJnts.append(temp)
        lowerTwistCtrlJnts.append(justGrp(lowerTwistCtrlJnts[4], 'Jnt', 'Off', True))

    upperArmCrv = makeCrvFromChain(upperArmTwist[0], 3, upperArmTwist[0].replace('B_Jnt_00', ''))
    lowerArmCrv = makeCrvFromChain(lowerArmTwist[0], 3, lowerArmTwist[0].replace('B_Jnt_00', ''))
    cmds.setAttr(upperArmCrv + '.v', 0)
    cmds.setAttr(lowerArmCrv + '.v', 0)
    
    #upperArmStretch
    cmds.select(upperArmCrv)
    cmds.pickWalk(d = 'down')
    upperArmCrvShape = cmds.ls(sl = True)
    upperArmCrvMult = side + 'upperArm_Length_Mult'
    upperArmCrvInfo = side + 'upperArm_CrvInfo'
    cmds.createNode('multiplyDivide', n = upperArmCrvMult)
    cmds.createNode('curveInfo', n = upperArmCrvInfo)
    upperArmCrvShape = cmds.rename(upperArmCrvShape, upperArmCrv + 'Shape')
    cmds.connectAttr(upperArmCrvShape + '.worldSpace[0]', upperArmCrvInfo + '.inputCurve')
    cmds.connectAttr(upperArmCrvInfo + '.arcLength', upperArmCrvMult + '.input1X')
    crvLength = cmds.getAttr(upperArmCrvMult + '.input1X')
    cmds.setAttr(upperArmCrvMult + '.input2X', crvLength)
    cmds.setAttr(upperArmCrvMult + '.operation', 2)
    for j in range(1, 7):
        cmds.connectAttr(upperArmCrvMult + '.outputX', upperArmTwist[j] + '.scaleX')
    
    #lowerArmStretch
    cmds.select(lowerArmCrv)
    cmds.pickWalk(d = 'down')
    lowerArmCrvShape = cmds.ls(sl = True)
    lowerArmCrvMult = side + 'lowerArm_Length_Mult'
    lowerArmCrvInfo = side + 'lowerArm_CrvInfo'
    cmds.createNode('multiplyDivide', n = lowerArmCrvMult)
    cmds.createNode('curveInfo', n = lowerArmCrvInfo)
    lowerArmCrvShape = cmds.rename(lowerArmCrvShape, lowerArmCrv + 'Shape')
    cmds.connectAttr(lowerArmCrvShape + '.worldSpace[0]', lowerArmCrvInfo + '.inputCurve')
    cmds.connectAttr(lowerArmCrvInfo + '.arcLength', lowerArmCrvMult + '.input1X')
    crvLength = cmds.getAttr(lowerArmCrvMult + '.input1X')
    cmds.setAttr(lowerArmCrvMult + '.input2X', crvLength)
    cmds.setAttr(lowerArmCrvMult + '.operation', 2)
    for j in range(1, 7):
        cmds.connectAttr(lowerArmCrvMult + '.outputX', lowerArmTwist[j] + '.scaleX')
   
    #Upperarm Twist Spline
    upperArmIkName = side + 'upperArm_Ik'
    cmds.select(upperArmTwist[0], upperArmTwist[-1], upperArmCrv)
    cmds.ikHandle(sol = 'ikSplineSolver', c = upperArmCrv, ccv = False, snc = True, pcv = False, n = upperArmIkName)
    cmds.setAttr(upperArmIkName + '.visibility', 0)
    cmds.setAttr(upperArmIkName + '.dTwistControlEnable', 1)
    cmds.setAttr(upperArmIkName + '.dWorldUpType', 4)
    if side == 'L_':
        cmds.setAttr(upperArmIkName + '.dForwardAxis', 1)
    if side == 'R_':
        cmds.setAttr(upperArmIkName + '.dForwardAxis', 0)
    cmds.setAttr(upperArmIkName + '.dWorldUpVectorX', 0)
    cmds.setAttr(upperArmIkName + '.dWorldUpVectorY', 1)
    cmds.setAttr(upperArmIkName + '.dWorldUpVectorZ', 0)
    cmds.setAttr(upperArmIkName + '.dWorldUpVectorEndX', 0)
    cmds.setAttr(upperArmIkName + '.dWorldUpVectorEndY', 1)
    cmds.setAttr(upperArmIkName + '.dWorldUpVectorEndZ', 0)
    cmds.connectAttr(upperTwistCtrlJnts[1] + '.worldMatrix[0]', upperArmIkName + '.dWorldUpMatrix')
    cmds.connectAttr(upperTwistCtrlJnts[0] + '.worldMatrix[0]', upperArmIkName + '.dWorldUpMatrixEnd')
    
    if armCtrlNum == 2:
        cmds.select(upperTwistCtrlJnts[0], upperTwistCtrlJnts[1], upperArmCrv)
    if armCtrlNum == 3:
        cmds.select(upperTwistCtrlJnts[0], upperTwistCtrlJnts[1], upperTwistCtrlJnts[4], upperArmCrv)

    cmds.skinCluster(tsb = True, dr = 4, mi = 2)
    
    cmds.parent(upperArmIkName, upperArmCrv, upperArmTwist[0], armRigGrp)
    
    #Lowerarm Twist Spline
    lowerArmIkName = side + 'lowerArm_Ik'
    cmds.select(lowerArmTwist[0], lowerArmTwist[-1], lowerArmCrv)
    cmds.ikHandle(sol = 'ikSplineSolver', c = lowerArmCrv, ccv = False, snc = True, pcv = False, n = lowerArmIkName)
    cmds.setAttr(lowerArmIkName + '.visibility', 0)
    cmds.setAttr(lowerArmIkName + '.dTwistControlEnable', 1)
    cmds.setAttr(lowerArmIkName + '.dWorldUpType', 4)
    if side == 'L_':
        cmds.setAttr(lowerArmIkName + '.dForwardAxis', 1)
    if side == 'R_':
        cmds.setAttr(lowerArmIkName + '.dForwardAxis', 0)
    cmds.setAttr(lowerArmIkName + '.dWorldUpVectorX', 0)
    cmds.setAttr(lowerArmIkName + '.dWorldUpVectorY', 1)
    cmds.setAttr(lowerArmIkName + '.dWorldUpVectorZ', 0)
    cmds.setAttr(lowerArmIkName + '.dWorldUpVectorEndX', 0)
    cmds.setAttr(lowerArmIkName + '.dWorldUpVectorEndY', 1)
    cmds.setAttr(lowerArmIkName + '.dWorldUpVectorEndZ', 0)
    cmds.connectAttr(lowerTwistCtrlJnts[1] + '.worldMatrix[0]', lowerArmIkName + '.dWorldUpMatrix')
    cmds.connectAttr(lowerTwistCtrlJnts[0] + '.worldMatrix[0]', lowerArmIkName + '.dWorldUpMatrixEnd')
    
    if armCtrlNum == 2:
        cmds.select(lowerTwistCtrlJnts[0], lowerTwistCtrlJnts[1], lowerArmCrv)
    if armCtrlNum == 3:
        cmds.select(lowerTwistCtrlJnts[0], lowerTwistCtrlJnts[1], lowerTwistCtrlJnts[4], lowerArmCrv)

    cmds.skinCluster(tsb = True, dr = 4, mi = 2)

    cmds.parentConstraint(baseJnts[1], upperTwistCtrlJnts[2], mo = True)
    cmds.parentConstraint(baseJnts[1], upperTwistCtrlJnts[3], mo = False)
    cmds.parentConstraint(baseJnts[2], lowerTwistCtrlJnts[2], mo = True)
    cmds.parentConstraint(baseJnts[2], lowerTwistCtrlJnts[3], mo = False)
    if armCtrlNum == 3:
        cmds.parentConstraint(baseJnts[1], upperTwistCtrlJnts[5], mo = True)
        cmds.parentConstraint(baseJnts[2], lowerTwistCtrlJnts[5], mo = True)
    
    cmds.connectAttr(baseJnts[2] + '.rotateX', upperTwistCtrlJnts[0] + '.rotateX')
    cmds.connectAttr(baseJnts[3] + '.rotateX', lowerTwistCtrlJnts[0] + '.rotateX')
       
    cmds.parent(lowerArmIkName, lowerArmCrv, lowerArmTwist[0], armRigGrp)
       
    #Arm Fk setup
    tempDiv = []
    for index, j in enumerate(fkJnts):
        if index == 3:
            tempDiv.append(makeCtrl(j, 1.5, False))
        else:
            tempDiv.append(makeCtrl(j, 1.5, True))
                
    for index in range(0, len(tempDiv)):
        fkOffs.append(tempDiv[index][0])
        fkCtrls.append(tempDiv[index][1])
                    
    for index in range(0, 3):
        cmds.parent(fkOffs[index+1], fkCtrls[index])
    
    cmds.parent(fkOffs[0], rootCtrl)
    
    #Arm Ik Setup
    ikCtrl = makeCtrl(ikJnts[3], 2, False)
    cmds.select(ikJnts[1], ikJnts[3])
    armIkName = side + 'arm_Ik'
    cmds.ikHandle(sol = "ikRPsolver", srp = True, s = 'sticky', n = armIkName)
    cmds.setAttr(armIkName + '.v', 0)
    
    cmds.parent(armIkName, ikCtrl[1])
    cmds.parent(ikCtrl[0], rootCtrl)
    
    pvCtrl = side + 'arm_PV_Ctrl'
    if side == 'L_':
        pvGrp = pvLocCreate(baseJnts[2], pvCtrl, 'z', -15)
    if side == 'R_':
        pvGrp = pvLocCreate(baseJnts[2], pvCtrl, 'z', 15)
    cmds.poleVectorConstraint(pvCtrl, armIkName)
    cmds.parent(pvGrp, rootCtrl)
    cmds.parentConstraint(fkCtrls[0], ikJnts[0], mo = False)
    cmds.orientConstraint(ikCtrl[1], ikJnts[3], mo = False)
    
    #IKFK Blend Setup
    for index, j in enumerate(baseJnts):
        tranBlendName = str(j).replace('B_Jnt', 'Tran_Blnd')
        rotBlendName = str(j).replace('B_Jnt', 'Rot_Blnd')
        cmds.createNode('blendColors', n = tranBlendName)
        cmds.createNode('blendColors', n = rotBlendName)
        cmds.connectAttr(settingsCtrl + '.IkFkSwitch', tranBlendName + '.blender')
        cmds.connectAttr(settingsCtrl + '.IkFkSwitch', rotBlendName + '.blender')
        cmds.connectAttr(fkJnts[index] + '.translate', tranBlendName + '.color1')
        cmds.connectAttr(ikJnts[index] + '.translate', tranBlendName + '.color2')
        cmds.connectAttr(fkJnts[index] + '.rotate', rotBlendName + '.color1')        
        cmds.connectAttr(ikJnts[index] + '.rotate', rotBlendName + '.color2')
        cmds.connectAttr(tranBlendName + '.output', j + '.translate')
        cmds.connectAttr(rotBlendName + '.output', j + '.rotate')

    #Cleanup
    cmds.parentConstraint(mainLoc, fkOffs[0], mo = True)
    cmds.parent(baseJnts[0], fkJnts[0], ikJnts[0], armRigGrp)
    cmds.parent(upperTwistCtrlJnts[2], upperTwistCtrlJnts[3], armRigGrp)
    cmds.parent(lowerTwistCtrlJnts[2], lowerTwistCtrlJnts[3], armRigGrp)
    if armCtrlNum == 3:
        cmds.parent(upperTwistCtrlJnts[5], lowerTwistCtrlJnts[5], armRigGrp)
    cmds.parent(settingsGrp, rootCtrl)

    #Hand Control Setup
    handCtrl = makeCtrl(baseJnts[3], 1.2, False)
    handCtrlName = str(baseJnts[3]).replace('wrist_B_Jnt', 'hand_Ctrl')
    cmds.rename(handCtrl[1], handCtrlName)
    handGrpName = str(baseJnts[3]).replace('wrist_B_Jnt', 'hand_Grp')
    cmds.rename(handCtrl[0], handGrpName)
    handOff = justGrp(handGrpName, 'Grp', 'Off', True)
    constraintName = handCtrlName + 'orientConstraint'
    cmds.pointConstraint(baseJnts[3], handGrpName, mo = False)
    cmds.orientConstraint(fkCtrls[3], handGrpName, mo = False, n = constraintName)
    cmds.orientConstraint(ikCtrl[1], handGrpName, mo = False)
    cmds.orientConstraint(handCtrlName, fkJnts[3], mo = False)
    cmds.orientConstraint(handCtrlName, ikJnts[3], mo = False)
    cmds.parent(handOff, rootCtrl)
    
    cmds.connectAttr(settingsCtrl + '.FkIkSwitch', constraintName + '.' + ikCtrl[1] + 'W1')
    cmds.connectAttr(settingsCtrl + '.IkFkSwitch', constraintName + '.' + fkCtrls[3] + 'W0')
    
    for j in upperArmTwist:
        bindList.append(j)
    for j in lowerArmTwist:
        bindList.append(j)
    bindList.append(baseJnts[0])
    bindList.append(baseJnts[3])
        
    return mainLoc, bindList, armRigGrp, baseJnts, fkOffs, fkCtrls, handCtrlName, handGrpName, lowerArmTwist, upperArmTwist
    
def autoLeg(locList, jntScale, side, lLegJnts, rootCtrl):
    baseJnts = []    
    fkOffs = []
    fkCtrls = []
    bindList = []
    
    mainLocName = side + 'leg_spaceLoc'
    mainLoc = cmds.spaceLocator(n = mainLocName)
    hipTran = cmds.xform(locList[0], q = True, t = True, ws = True)
    cmds.xform(mainLocName, t = hipTran, ws = True)
    cmds.setAttr(mainLocName + 'Shape.localScale', 5, 5, 5)

    legRigGrp = side + 'legRigGrp'
    cmds.group(em = True, n = legRigGrp)
    cmds.setAttr(legRigGrp + '.inheritsTransform', 0)
    
    #Makes and Parents Joints
    for l in locList:
        baseJnts.append(makeJntAt(l, jntScale, '_B_Jnt'))
    for index in range(0, (len(locList)-1)):
        cmds.parent(baseJnts[index + 1], baseJnts[index])
       
    #Orients Joints
    if side == 'L_':
        jntOrient(baseJnts[0], 'lLeg')
    if side == 'R_':
        orientMatch(baseJnts[0], lLegJnts[0])
    setJointAngle(baseJnts[1], '-z')
    cmds.setAttr(baseJnts[3] + '.jointOrientX', 0)
    
    #Settings Control
    settingsName = side + 'legSettings_Ctrl'
    settingsCtrl = makeShape('cube', settingsName)
    settingsGrp = cmds.group(settingsCtrl, n = (side + 'legSettings_Grp'))
    settingsConstraintName = side + 'legSettingsGrp_ParConstraint'
    cmds.parentConstraint(baseJnts[2], settingsGrp, mo = False, n = settingsConstraintName)
    if side == 'L_':
        cmds.setAttr(settingsCtrl + '.translate', -8, -8, 0)
    if side == 'R_':
        cmds.setAttr(settingsCtrl + '.translate', 8, 8, 0)    
    cmds.setAttr(settingsCtrl + '.scale', 3, 3, 3)
    
    cmds.addAttr(settingsCtrl, ln = 'IkFkSwitch', nn = 'Ik/Fk Switch', at = 'float', dv = 1, min = 0, max = 1, k = True, h = False)
    
    #Limb Duplication
    fkJnts = duplicateJntChain(baseJnts, '_B_', '_Fk_')
    ikJnts = duplicateJntChain(baseJnts, '_B_', '_Ik_')

    upperLegTwist = makeLimbTwistJnt(baseJnts[0], 6)

    cmds.select(upperLegTwist[0])
    upperTwistCtrlJnts = makeSplineCtrls(2)
    
    for index, j in enumerate(upperTwistCtrlJnts):
        name = str(j).replace('_00', '')
        upperTwistCtrlJnts[index] = cmds.rename(upperTwistCtrlJnts[index], name)       
    upperTwistCtrlJnts.append(justGrp(upperTwistCtrlJnts[0], 'Jnt', 'Off', True))
    upperTwistCtrlJnts.append(justGrp(upperTwistCtrlJnts[1], 'Jnt', 'Off', True))
    
    upperLegCrv = makeCrvFromChain(upperLegTwist[0], 3, upperLegTwist[0].replace('B_Jnt_00', ''))
    cmds.setAttr(upperLegCrv + '.inheritsTransform', 0)
    cmds.parent(upperLegCrv, legRigGrp)
    
    #UpperLeg Twist Spline
    upperLegIkName = side + 'upperLeg_Ik'
    cmds.select(upperLegTwist[0], upperLegTwist[-1], upperLegCrv)
    cmds.ikHandle(sol = 'ikSplineSolver', c = upperLegCrv, ccv = False, snc = True, pcv = False, n = upperLegIkName)
    cmds.setAttr(upperLegIkName + '.visibility', 0)
    cmds.setAttr(upperLegIkName + '.dTwistControlEnable', 1)
    cmds.setAttr(upperLegIkName + '.dWorldUpType', 4)
    if side == 'L_':
        cmds.setAttr(upperLegIkName + '.dForwardAxis', 0)
    if side == 'R_':
        cmds.setAttr(upperLegIkName + '.dForwardAxis', 1)
    cmds.setAttr(upperLegIkName + '.dWorldUpVectorX', 0)
    cmds.setAttr(upperLegIkName + '.dWorldUpVectorY', 1)
    cmds.setAttr(upperLegIkName + '.dWorldUpVectorZ', 0)
    cmds.setAttr(upperLegIkName + '.dWorldUpVectorEndX', 0)
    cmds.setAttr(upperLegIkName + '.dWorldUpVectorEndY', 1)
    cmds.setAttr(upperLegIkName + '.dWorldUpVectorEndZ', 0)
    cmds.connectAttr(upperTwistCtrlJnts[1] + '.worldMatrix[0]', upperLegIkName + '.dWorldUpMatrix')
    cmds.connectAttr(upperTwistCtrlJnts[0] + '.worldMatrix[0]', upperLegIkName + '.dWorldUpMatrixEnd')
    
    cmds.select(upperTwistCtrlJnts[0], upperTwistCtrlJnts[1], upperLegCrv)
    cmds.skinCluster(tsb = True, dr = 4, mi = 2)
    
    cmds.parentConstraint(baseJnts[0], upperTwistCtrlJnts[3], mo = False)
    cmds.parentConstraint(baseJnts[0], upperTwistCtrlJnts[2], mo = True)
    multName = side + 'upperLeg_Twist_Mult'
    cmds.createNode('multiplyDivide', n = multName)
    cmds.connectAttr(baseJnts[0] + '.rotateX', multName + '.input1X')
    cmds.setAttr(multName + '.input2X', -1)
    cmds.connectAttr(multName + '.outputX', upperTwistCtrlJnts[0] + '.rotateX')
    cmds.parent(upperLegTwist[0], upperLegIkName, legRigGrp)
    
    #Leg Fk Setup
    tempDiv = []
    for j in fkJnts:
        tempDiv.append(makeCtrl(j, 1.5, True))
    
    for index in range(0, len(tempDiv)):
        fkOffs.append(tempDiv[index][0])
        fkCtrls.append(tempDiv[index][1])
                    
    for index in range(0, 4):
        cmds.parent(fkOffs[index+1], fkCtrls[index])
        
    cmds.parent(fkOffs[0], rootCtrl)
    
    #Leg Ik Setup
    cmds.select(ikJnts[0], ikJnts[2])
    legIkName = side + 'leg_Ik'
    cmds.ikHandle(sol = "ikRPsolver", srp = True, s = 'sticky', n = legIkName)
    cmds.setAttr(legIkName + '.v', 0)

    cmds.select(ikJnts[2], ikJnts[3])
    footIkName = side + 'foot_Ik'
    cmds.ikHandle(sol = "ikSCsolver", srp = False, s = 'sticky', n = footIkName)
    cmds.setAttr(footIkName + '.v', 0)

    cmds.select(ikJnts[3], ikJnts[4])
    toeIkName = side + 'toe_Ik'
    cmds.ikHandle(sol = "ikSCsolver", srp = False, s = 'sticky', n = toeIkName)
    cmds.setAttr(toeIkName + '.v', 0)
    
    ikCtrlName = side + 'Ik_foot_Ctrl'
    ikCtrl = cmds.circle(nr = (0, 1, 0), n = ikCtrlName)
    cmds.scale(5, 1, 12, ikCtrl)
    tempAttr = cmds.xform(ikJnts[2], q = True, t = True, ws = True)
    cmds.xform(ikCtrl, t = (tempAttr[0], 0, 0), ws = True)
    cmds.makeIdentity(ikCtrl, apply=True, s=1, t = True, n=2)
    
    legPVName = side + 'knee_PV_Ctrl'
    if side == 'L_':
        pvGrp = pvLocCreate(baseJnts[1], legPVName, 'y', 15)
    if side == 'R_':
        pvGrp = pvLocCreate(baseJnts[1], legPVName, 'y', -15)

    cmds.poleVectorConstraint(legPVName, legIkName)
    cmds.parent(pvGrp, rootCtrl)
    
    #IKFK Blend Setup
    for index, j in enumerate(baseJnts):
        tranBlendName = str(j).replace('B_Jnt', 'Tran_Blnd')
        rotBlendName = str(j).replace('B_Jnt', 'Rot_Blnd')
        cmds.createNode('blendColors', n = tranBlendName)
        cmds.createNode('blendColors', n = rotBlendName)
        cmds.connectAttr(settingsCtrl + '.IkFkSwitch', tranBlendName + '.blender')
        cmds.connectAttr(settingsCtrl + '.IkFkSwitch', rotBlendName + '.blender')
        cmds.connectAttr(fkJnts[index] + '.translate', tranBlendName + '.color1')
        cmds.connectAttr(ikJnts[index] + '.translate', tranBlendName + '.color2')
        cmds.connectAttr(fkJnts[index] + '.rotate', rotBlendName + '.color1')        
        cmds.connectAttr(ikJnts[index] + '.rotate', rotBlendName + '.color2')
        cmds.connectAttr(tranBlendName + '.output', j + '.translate')
        cmds.connectAttr(rotBlendName + '.output', j + '.rotate')
    
    #Cleanup
    cmds.parent(legIkName, footIkName, toeIkName, ikCtrlName)
    cmds.parent(ikCtrlName, rootCtrl)
    cmds.parent(baseJnts[0], fkJnts[0], ikJnts[0], legRigGrp)
    cmds.parent(upperTwistCtrlJnts[2], upperTwistCtrlJnts[3], legRigGrp)
    cmds.parent(settingsGrp, rootCtrl)

    cmds.parentConstraint(mainLoc, ikJnts[0], mo = False)
    cmds.parentConstraint(mainLoc, fkOffs[0], mo = True)
    
    for j in upperLegTwist:
        bindList.append(j)
    for index in range(1, 4):
        bindList.append(baseJnts[index])
    
    return baseJnts, bindList, legRigGrp, mainLoc, upperLegTwist
    
def autoHand(locList, jntScale, side, wrist, lHandJnts):
    baseJnts = []
    for l in locList:
        baseJnts.append(makeJntAt(l, jntScale, '_B_Jnt'))
    for index, j in enumerate(baseJnts):
        if index > -1 and index < 4:
            cmds.parent(baseJnts[index + 1], baseJnts[index])
        if index > 4 and index < 9:
            cmds.parent(baseJnts[index + 1], baseJnts[index])
        if index > 9 and index < 14:
            cmds.parent(baseJnts[index + 1], baseJnts[index])
        if index > 14 and index < 19:
            cmds.parent(baseJnts[index + 1], baseJnts[index])
        if index > 19 and index < 24:
            cmds.parent(baseJnts[index + 1], baseJnts[index])
    for index in range(0, 21, 5):
        if side == 'L_':
            jntOrient(baseJnts[index], 'lArm')
        if side == 'R_':
            jntOrient(baseJnts[index], 'rArm')            
        cmds.parent(baseJnts[index], wrist)

    if side == 'R_':
        orientMatch(baseJnts[0], lHandJnts[0])
        orientMatch(baseJnts[5], lHandJnts[5])
        orientMatch(baseJnts[10], lHandJnts[10])
        orientMatch(baseJnts[15], lHandJnts[15])
        orientMatch(baseJnts[20], lHandJnts[20])

    return baseJnts

def selectBind(*args):
    if cmds.objExists('bindSet'):
        cmds.select('bindSet')
    else:
        cmds.warning("Create the Rig first, then bind joints will be available.")

def ehBind(*args):
    joints = cmds.ls(sl = True)
    cmds.delete(joints[-1], ch = True)
    mesh = joints[-1]
    cmds.select(cl = True)
    try:
        cmds.skinCluster(joints, tsb = True, mi = 3, dr = 5)
    except:
        cmds.warning("Joints must be selected first, then Mesh.")

def rootCtrlMake(characterName, characterHeight):
    rootCtrl = characterName + '_Ctrl'
    rootGrp = characterName + '_Grp'
    rigGrp = characterName + '_Rig'
    geoGrp = characterName + '_Geo'
    cmds.circle(nr = (0, 1, 0), sw  = 360, n = rootCtrl)
    cmds.group(n = rootGrp)
    cmds.group(em = True, n = rigGrp)
    cmds.parent(rigGrp, rootGrp)
    cmds.group(em = True, n = geoGrp)
    cmds.parent(geoGrp, rootGrp)
    cmds.scale((characterHeight/5), (characterHeight/5), (characterHeight/5), rootCtrl)
    cmds.makeIdentity(rootCtrl, apply=True, s=1, n=2, r = 1)
    cmds.delete(rootCtrl, ch = True)
    cmds.addAttr(rootCtrl, ln = 'characterScale', at = 'float', dv = 1, k = True, h = False)
    cmds.addAttr(rootCtrl, ln = 'wingScale', at = 'float', dv = 1, k = True, h = False)
    
    return rootCtrl, rootGrp, rigGrp, geoGrp

def setJointAngle(joint, direction):
    if '+x' in direction:
        cmds.setAttr(joint + '.rotateX', 45)
        cmds.select(joint)
        cmds.joint(e = True, spa = True)
        cmds.setAttr(joint + '.rotateX', 0)
    if '-x' in direction:
        cmds.setAttr(joint + '.rotateX', -45)
        cmds.select(joint)
        cmds.joint(e = True, spa = True)  
        cmds.setAttr(joint + '.rotateX', 0)      
    if '+y' in direction:
        cmds.setAttr(joint + '.rotateY', 45)
        cmds.select(joint)
        cmds.joint(e = True, spa = True)    
        cmds.setAttr(joint + '.rotateY', 0)    
    if '-y' in direction:
        cmds.setAttr(joint + '.rotateY', -45)
        cmds.select(joint)
        cmds.joint(e = True, spa = True)  
        cmds.setAttr(joint + '.rotateY', 0)      
    if '+z' in direction:
        cmds.setAttr(joint + '.rotateZ', 45)
        cmds.select(joint)
        cmds.joint(e = True, spa = True)  
        cmds.setAttr(joint + '.rotateZ', 0)      
    if '-z' in direction:
        cmds.setAttr(joint + '.rotateZ', -45)
        cmds.select(joint)
        cmds.joint(e = True, spa = True)
        cmds.setAttr(joint + '.rotateZ', 0)

def mirrorConnect(sel1, sel2, axis):
    if 'Loc' in sel1:
        multName = sel1.replace('Loc', 'Mult')
    if 'PosJnt' in sel1:
        multName = sel1.replace('PosJnt', 'Mult')
    cmds.createNode('multiplyDivide', n = multName)
    if 'x' in axis:
        cmds.setAttr(multName + '.input2X', -1)
    if 'y' in axis:
        cmds.setAttr(multName + '.input2Y', -1)
    if 'z' in axis:
        cmds.setAttr(multName + '.input2Z', -1)
    cmds.connectAttr(sel1 + '.translateX', multName + '.input1X')
    cmds.connectAttr(sel1 + '.translateY', multName + '.input1Y')
    cmds.connectAttr(sel1 + '.translateZ', multName + '.input1Z')
    cmds.connectAttr(multName + '.outputX', sel2 + '.translateX')
    cmds.connectAttr(multName + '.outputY', sel2 + '.translateY')
    cmds.connectAttr(multName + '.outputZ', sel2 + '.translateZ')

def makeJntAt(sel, size, name):
    object = sel
    rad = size
    obTran = cmds.xform(object, q = True, t = True, ws = True)
    obRot = cmds.xform(object, q = True, ro = True, ws = True)
    if 'Pos_Loc' in object:
        jntName = object.replace('Pos_Loc', name)
    if 'B_' in object:
        jntName = object.replace('B_', name)
    cmds.select(cl = True)
    jnt = cmds.joint(rad = rad, n = jntName)
    cmds.xform(jnt, t = obTran, ws = True)
    cmds.xform(jnt, ro = obRot, ws = True)
    return jntName
    
def makeGrpAt(sel, name):
    grp = cmds.group(em = True, n = name)
    selTran = cmds.xform(sel, q = True, t = True, ws = True)
    selRot = cmds.xform(sel, q = True, ro = True, ws = True)
    cmds.select(cl = True)
    cmds.xform(grp, t = selTran, ws = True)
    cmds.xform(grp, ro = selRot, ws = True)

def orientMatch(sel, target):
    cmds.select(sel, hi = True)
    selHi = cmds.ls(sl = True, typ = 'joint')
    cmds.select(target, hi = True)
    targetHi = cmds.ls(sl = True, typ = 'joint')

    for index, s in enumerate(selHi):
        par = cmds.listRelatives(s, p = True)
        children = cmds.listRelatives(s)
        targetX = cmds.getAttr(targetHi[index] + '.jointOrientX')
        if par:
            targetY = cmds.getAttr(targetHi[index] + '.jointOrientY')
            targetZ = cmds.getAttr(targetHi[index] + '.jointOrientZ')
        else:
            targetY = (cmds.getAttr(targetHi[index] + '.jointOrientY') + 180)
            targetZ = ((cmds.getAttr(targetHi[index] + '.jointOrientZ') - 180) * -1)   
        if children:
            if par:
                for c in children:
                    cmds.parent(c, par)
            else:
                for c in children:
                    cmds.parent(c, w = True)
        cmds.setAttr(s + '.jointOrientX', targetX)
        cmds.setAttr(s + '.jointOrientY', targetY)
        cmds.setAttr(s + '.jointOrientZ', targetZ)
        if children:
            for c in children:
                cmds.parent(c, s)
    cmds.select(cl = True)

def jntOrient(sel, rotOrder):
    order = str(rotOrder)
    cmds.select(sel, hi = True)
    sel = cmds.ls(sl = True, typ = 'joint')
    size = len(sel)
    par = cmds.listRelatives(sel[0], p = True)
    reverse = False
    if order == 'lArm':
        aimVector = MVector(-1.0, 0.0, 0.0)
        upVector = MVector(0.0, -1.0, 0.0)
        wUpVector = MVector(0.0, 1.0, 0.0)
        type = 'arm'
    elif order == 'rArm':
        aimVector = MVector(1.0, 0.0, 0.0)
        upVector = MVector(0.0, 1.0, 0.0)
        wUpVector = MVector(0.0, 1.0, 0.0)
        type = 'arm'
    elif order == 'lLeg':
        aimVector = MVector(1.0, 0.0, 0.0)
        upVector = MVector(0.0, -1.0, 0.0)
        wUpVector = MVector(0.0, 1.0, 0.0) 
        type = 'leg'      
    elif order == 'rLeg':
        aimVector = MVector(-1.0, 0.0, 0.0)
        upVector = MVector(0.0, 1.0, 0.0)
        wUpVector = MVector(0.0, 1.0, 0.0)
        type = 'leg'
        reverse = True
    elif order == 'spine':
        aimVector = MVector(1.0, 0.0, 0.0)
        upVector = MVector(0.0, 1.0, 0.0)
        wUpVector = MVector(0.0, 0.0, 1.0)
        type = 'spine'
    if not par:
        parWorld = True
    else:
        parWorld = False

    for index, s in enumerate(sel):
        if index < (size - 1):
            cmds.parent(sel[index + 1], w = True)
            aim = cmds.aimConstraint(sel[index + 1], sel[index], mo = False, aim = (aimVector.x, aimVector.y, aimVector.z), u = (upVector.x,upVector.y, upVector.z), wu = (wUpVector.x, wUpVector.y, wUpVector.z))
            cmds.delete(aim)
            cmds.makeIdentity(s, apply = True, t = 0, r = 1, s = 0, n = 0, pn = 1)
            if type == 'leg':
                if reverse == True:
                    cmds.setAttr(s + '.jointOrientX', -90)
                if reverse == False:
                    cmds.setAttr(s + '.jointOrientX', 90)
            if order == 'lArm':
                cmds.setAttr(s + '.jointOrientX', 0)
        cmds.setAttr(sel[-1] + '.rotateX', 0)
        cmds.setAttr(sel[-1] + '.rotateY', 0)
        cmds.setAttr(sel[-1] + '.rotateZ', 0)
    for index, s in enumerate(reversed(sel)):
        if index < (size - 1):
            cmds.parent(sel[index + 1], sel[index])
    cmds.setAttr(sel[size - 1] + '.jointOrientX', 0)
    cmds.setAttr(sel[size - 1] + '.jointOrientY', 0)
    cmds.setAttr(sel[size - 1] + '.jointOrientZ', 0)
    cmds.select(sel[0])
  
def makeLimbTwistJnt(sel, number):
    twistJnts = []
    child = cmds.listRelatives(sel, type = 'joint')
    if child:
        selDup = cmds.duplicate(sel, po = True)
        childDup = cmds.duplicate(child, po = True)
        cmds.parent(childDup, selDup)
        name = sel.replace('shoulder', 'upperArmTwist')
        cmds.select(selDup)
        jntSegCreate(number, 'B_Jnt')
        cmds.select(selDup, hi = True)
        tempJnts = cmds.ls(sl = True)
        for index in range(0, number + 1):
            numberedName = name + '_0' + str(index)
            twistJnts.append(cmds.rename(tempJnts[index], numberedName))
            rad = cmds.getAttr(twistJnts[index] + '.radius')
            cmds.setAttr(twistJnts[index] + '.radius', (rad * 3/5))
        par = cmds.listRelatives(sel, p = True)
        if par:
            cmds.parent(twistJnts[0], w = True)
        return twistJnts
    else:
        cmds.warning("No child found for twist segments.")

def makeCtrl(sel, radius, makeConstraint):
    selTran = cmds.xform(sel, q = True, t = True, ws = True)
    selRot = cmds.xform(sel, q = True, ro = True, ws = True)
    selRad = cmds.getAttr(sel + '.radius')
    ctrlRad = selRad * radius
    if 'Ctrl_Jnt' in sel:
        ctrlName = sel.replace('_Jnt', '')
        grpName = sel.replace('_Jnt', '_Off')
    if 'B_Jnt' in sel:
        grpName = sel.replace('B_Jnt', 'Off')
        ctrlName = sel.replace('B_Jnt', 'Ctrl')
    if 'Jnt' in sel:
        grpName = sel.replace('Jnt', 'Off')
        ctrlName = sel.replace('Jnt', 'Ctrl')
    else:
        ctrlName = sel + '_Ctrl'
        grpName = sel + '_Off'
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

def makeCrvFromChain(sel, number, name):
    pos = []
    cmds.select(sel, hi = True)
    selChain = cmds.ls(sl = True)
    start = cmds.xform(selChain[0], q = True, t = True, ws = True)
    end = cmds.xform(selChain[-1], q = True, t = True, ws = True)

    pos.append(start)
    for index in range(0, number):
        mid = [0, 0, 0]
        mid[0] = (end[0] - start[0]) / (number + 1) * (index + 1) + start[0]
        mid[1] = (end[1] - start[1]) / (number + 1) * (index + 1) + start[1]
        mid[2] = (end[2] - start[2]) / (number + 1) * (index + 1) + start[2]
        pos.append(mid)
    pos.append(end)
    
    if number == 0:
        curveDegree = 1
        knots = [0, 1]
    if number == 1:
        curveDegree = 1
        knots = [0, 1, 2]
    else:
        curveDegree = 3
        knot = curveDegree + number - 1
        knots = []
        for index in range(0, knot - 1):
            if index < 3:
                knots.append(0)
            else:
                knots.append(int(index - 2))
        for index in range(0, 3):
            knots.append(knot - 3)
        
    spineCrvName = name + 'Crv'
    cmds.curve(p = pos, n = spineCrvName, d = curveDegree, k = knots)
    return spineCrvName

def parGrp(sel, typeString):
    type = typeString
    object = sel
    grpTran = cmds.xform(object, query=True, t =True, worldSpace = True)
    grpRot = cmds.xform(object, query=True, ro =True, worldSpace = True)
    if type == 'Wing' or type == 'wing':
        grpName = str(object).replace('Jnt', 'Jnt_Par')
    elif type == 'Par' or type == 'par':
        grpName = str(object).replace('Ctrl', 'Par')
    elif type == 'Off' or type == 'off':
        grpName = str(object).replace('Ctrl', 'Off')
    elif type == 'Prx' or type == 'prx':
        grpName = str(object).replace('Ctrl', 'Prx')
    else:
        grpName = str(object).replace('Ctrl', 'Grp')
    ctrlGrp = cmds.group(em = True, n = grpName)
    cmds.xform(ctrlGrp, t = grpTran, worldSpace = True)
    cmds.xform(ctrlGrp, ro = grpRot, worldSpace = True)
    cmds.parent(object, grpName)
    return grpName
                                            
def justGrp(sel, current, new, parent):
    objectTran = cmds.xform(sel, q = True, t = True, ws = True)
    objectRot = cmds.xform(sel, q = True, ro = True, ws = True)
    par = cmds.listRelatives(sel, p = True)
    grpName = sel.replace(current, new)
    cmds.group(em = True, n = grpName)
    if par:
        cmds.parent(grpName, par)
    cmds.xform(grpName, t = objectTran, ws = True)
    cmds.xform(grpName, ro = objectRot, ws = True)
    if parent == True:
        cmds.parent(sel, grpName)
    return grpName

def justGrpn():
    get = cmds.ls(sl = True)
    sel = get[0]
    objectTran = cmds.xform(sel, q = True, t = True, ws = True)
    objectRot = cmds.xform(sel, q = True, ro = True, ws = True)
    par = cmds.listRelatives(sel, p = True)
    grpName = cmds.group(em = True)
    if par:
        cmds.parent(grpName, par)
    cmds.xform(grpName, t = objectTran, ws = True)
    cmds.xform(grpName, ro = objectRot, ws = True)
    cmds.parent(sel, grpName)
    return grpName

def makeFeather(sel, index):
    object = sel
    num = index
    cmds.select(cl = True)
    if '32' in str(sel):
        name = object.replace('wing', 'feather').replace('Pnt', 'B').replace('32', str(num))
        childName = name.replace('B', 'End').replace('32', str(num))
        grpName = object.replace('wing', 'wingFeather').replace('Pnt_Jnt', 'Grp').replace('32', str(num))
        parName = object.replace('wing', 'wingFeather').replace('Pnt_Jnt', 'Par').replace('32', str(num))
    else: 
        name = object.replace('wing', 'feather').replace('Pnt', 'B')
        childName = name.replace('B', 'End')
        grpName = object.replace('wing', 'wingFeather').replace('Pnt_Jnt', 'Grp')
        parName = object.replace('wing', 'wingFeather').replace('Pnt_Jnt', 'Par')
    cmds.joint(n = name)
    cmds.joint(n = childName)
    cmds.select(cl = True)
    cmds.group(em = True, n = parName)
    cmds.group(parName, n = grpName)
    cmds.parent(name, parName)
    cmds.parent(grpName, object)
    cmds.xform(grpName, t = (0,0,0))
    #if num < 8:
     #   cmds.xform(grpName, ro = (0,180,0))
    #else:
    cmds.xform(grpName, ro = (0, 0, 0))

    featherLengthList = [4.837125, 7.603119, 10.041428, 12.536321, 14.800365, 17.032899,
    19.17551, 21.223598, 23.105806, 23.879093, 24.262061, 24.078812, 23.507744, 23.161271, 22.599805,
    22.329762, 22.100591, 21.926852, 21.94863, 22.086331, 22.264769, 22.316846, 22.472283, 22.563871, 
    22.568632, 22.472012, 22.357701, 22.132585, 21.992272, 21.839708, 21.554895, 21.299925, 21.019754, 
    21.243217, 21.476129, 21.847872, 22.125137, 22.51703, 22.906303, 23.444456, 24.013072, 24.552076, 
    25.23615, 26.069493, 26.730022, 27.517584, 28.262699, 29.12234, 30 ]
    
    cmds.xform(childName, t = (featherLengthList[index],0,0))
    
    return name
        
def hideAttr(sel, list):
    object = str(sel)
    attrs = list
    if 't' in attrs:
        cmds.setAttr(object + '.translateX', k = False, cb = False, l = True)
        cmds.setAttr(object + '.translateY', k = False, cb = False, l = True)
        cmds.setAttr(object + '.translateZ', k = False, cb = False, l = True)
    if 'r' in attrs:
        cmds.setAttr(object + '.rotateX', k = False, cb = False, l = True)
        cmds.setAttr(object + '.rotateY', k = False, cb = False, l = True)
        cmds.setAttr(object + '.rotateZ', k = False, cb = False, l = True)
    if 's' in attrs:
        cmds.setAttr(object + '.scaleX', k = False, cb = False, l = True)
        cmds.setAttr(object + '.scaleY', k = False, cb = False, l = True)
        cmds.setAttr(object + '.scaleZ', k = False, cb = False, l = True)        
    if 'v' in attrs:
        cmds.setAttr(object + '.visibility', k = False, cb = False, l = True)

def makeSplineCtrls(num):
    ctrls = num
    sel = cmds.ls(sl = True)
    baseName = str(sel[0]).replace("[u'", '').replace("']",'')
    cmds.duplicate()
    cmds.select(hi = True)
    selChain = cmds.ls(sl = True)
    selSize = len(selChain)
    jntRad = cmds.getAttr(selChain[0] + ".radius")
    newRad = jntRad * 1.5
    hasPar = cmds.listRelatives(sel[0], p = True)
    ctrlJnts = []
    
    if ctrls == 5:
        for s in reversed(selChain):
            cmds.select(s)
            if s == selChain[0]:
                if hasPar != None:
                    cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_01')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            elif s == selChain[(selSize - 1)]:
                cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_05')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            elif s == selChain[((selSize -1)/4)]:
                cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_02')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            elif s == selChain[((selSize -1)/2)]:
                cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_03')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            elif s == selChain[((selSize -1)/4*3)]:
                cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_04')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            else:
                cmds.parent(w = True)
                cmds.delete()
    elif ctrls ==3:
        for s in reversed(selChain):
            cmds.select(s)
            if s == selChain[0]:
                if hasPar != None:
                    cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_Start')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            elif s == selChain[(selSize - 1)]:
                cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_End')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            elif s == selChain[((selSize -1)/2)]:
                cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_Mid')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            else:
                cmds.parent(w = True)
                cmds.delete()
        temp = ctrlJnts[1]
        ctrlJnts[1] = ctrlJnts[2]
        ctrlJnts[2] = temp
    elif ctrls == 2:
        for s in reversed(selChain):
            cmds.select(s)
            if s == selChain[0]:
                if hasPar != None:
                    cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_Start')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            elif s == selChain[(selSize - 1)]:
                cmds.parent(w = True)
                name = baseName.replace('B_Jnt', 'Ctrl_Jnt_End')
                tempSel = cmds.ls(sl = True)
                cmds.setAttr(tempSel[0] + ".radius", newRad)
                cmds.rename(name)
                ctrlJnts.append(name)
            else:
                cmds.parent(w = True)
                cmds.delete()
        cmds.parent(ctrlJnts[0], ctrlJnts[1])
        cmds.setAttr(ctrlJnts[0] + '.jointOrientX', 0)
        cmds.setAttr(ctrlJnts[0] + '.jointOrientY', 0)
        cmds.setAttr(ctrlJnts[0] + '.jointOrientZ', 0)
        cmds.parent(ctrlJnts[0], w = True)
    else:
        cmds.warning("Wrong number of controls submitted, must be 2, 3, or 5")
        
    return ctrlJnts
    
def setRotPivTo(sel, target):
    objectTran = cmds.xform(target, q = True, t = True, ws = True)
    cmds.move(objectTran[0], objectTran[1], objectTran[2], sel + '.rotatePivot', sel + '.scalePivot', rpr = True)
    
def parJnt(sel, name):
    selJnt = sel
    cmds.select(selJnt)
    jntName = name
    tran = cmds.xform(selJnt, q = True, t = True, worldSpace = True)
    rot = cmds.xform(selJnt, q = True, ro = True, worldSpace = True)
    newJnt = cmds.duplicate(n = jntName)
    cmds.xform(selJnt, t = tran, worldSpace = True)
    cmds.xform(selJnt, t = tran, worldSpace = True)
    cmds.parent(newJnt, selJnt)
    return newJnt

def jntSegCreate(num, name):
    suffix = name
    selJnt = cmds.ls(sl = True)
    name = str(selJnt).replace("[u'", '').replace("']",'').replace('B_Jnt', suffix)
    cmds.select(hi = True)
    newJnts = []
    selSize = len(selJnt)
    
    for index, s in enumerate(selJnt):
        cmds.select(s)
        cmds.pickWalk(d = 'down')
        selChild = cmds.ls(sl = True)
        cmds.select(selChild[0])
        childTx = cmds.getAttr(selChild[0] + ".tx")
        childJnt = cmds.getAttr(s + ".radius")
        cmds.pickWalk(d = 'up')
        getNumber = num
        
        if getNumber < 2:
            cmds.warning("Must create at least one segment.")
        else:
            sel = cmds.ls(sl = True)
            distX = childTx/float(getNumber)
            for x in range(0, int(getNumber)):
                if getNumber == 2:
                    cName = name
                else:
                    cName = name + "_%02d" % x
                if x == (getNumber - 1):
                    endJnt = cmds.joint(rad = childJnt, o = (0,0,0), n = cName)
                else:
                    newJnts.append(cmds.joint(rad = childJnt, o = (0,0,0), n = cName))
                cmds.move(float(distX), 0, 0, r = True, ls = True)
            cmds.delete(endJnt)
            cmds.parent(selChild[0], newJnts[-1])
            cmds.select(cl = True)            
            return endJnt
        
def doGrp(sel, input):
    level = input
    object = sel
    grpTran = cmds.xform(object, query=True, t =True, worldSpace = True)
    grpRot = cmds.xform(object, query=True, ro =True, worldSpace = True)

    if level == '1':
        grpName = str(object).replace('Jnt', 'Grp')
        ctrlGrp = cmds.group(em = True, n = grpName)
        ctrlName = str(object).replace('_Jnt', '')
        ctrl = cmds.circle(nr = (0,1,0), n = ctrlName)
        cmds.xform(ctrlGrp, t = grpTran, worldSpace = True)
        cmds.xform(ctrlGrp, ro = grpRot, worldSpace = True)
        if 'Ctrl_01' in ctrlName:
            cmds.scale(1.3, 1.3, 1.3, ctrl)
        else:
            cmds.scale(1.5, 1, 1, ctrl)
         
    elif level == '2':
        grpName = str(object).replace('Ctrl_Grp_01', 'Main_Ctrl_Grp')
        ctrlGrp = cmds.group(em = True, n = grpName)
        ctrlName = str(object).replace('Ctrl_Grp_01', 'Main_Ctrl')
        ctrl = cmds.circle(nr = (0,1,0), n = ctrlName)
        cmds.addAttr(ctrl, ln = 'featherLength', at = 'float', dv = 1, h = False, k = True)
        cmds.xform(ctrlGrp, t = grpTran, worldSpace = True)
        cmds.xform(ctrlGrp, ro = grpRot, worldSpace = True)
        if '00_Main' in ctrlName or '08_Main' in ctrlName or '20_Main' in ctrlName or '32_Main' in ctrlName or '48_Main' in ctrlName:
            cmds.scale(2.2, 2.2, 2.2, ctrl)
        else:
            cmds.scale(1.7, 1.7, 1.7, ctrl)
        
    elif level == '3':
        grpName = str(object).replace('Ctrl_Jnt', 'Master_Ctrl_Grp')
        ctrlGrp = cmds.group(em = True, n = grpName)
        ctrlName = str(object).replace('Ctrl_Jnt', 'Master_Ctrl')
        ctrl = cmds.circle(nr = (0,1,0), n = ctrlName)
        cmds.xform(ctrlGrp, t = grpTran, worldSpace = True)
        cmds.xform(ctrlGrp, ro = grpRot, worldSpace = True)
        if '_01' in ctrlName:
            cmds.scale(1.8, 1.8, 1.8, ctrl)
        else:
            cmds.scale(1.8, 1.3, 1.3, ctrl)        

    cmds.xform(ctrl, t = grpTran, worldSpace = True)
    cmds.xform(ctrl, ro = grpRot, worldSpace = True)  
    cmds.select(ctrl)
    cmds.select(ctrlGrp, add = True)
    cmds.parent()
    tempAttr = cmds.getAttr(str(ctrlName) + '.translateX')
    if 'Ctrl_01' in ctrlName or 'Main_Ctrl' in ctrlName:
        if '32' in ctrlName or '33' in ctrlName or '34' in ctrlName or '35' in ctrlName or '36' in ctrlName or '37' in ctrlName or '38' in ctrlName or '39' in ctrlName or '40' in ctrlName or '41' in ctrlName or '42' in ctrlName or '43' in ctrlName or '44' in ctrlName or '45' in ctrlName or '46' in ctrlName or '47' in ctrlName or '48' in ctrlName:
            cmds.makeIdentity(ctrl, apply=True, s=1, n=2 )
            cmds.move(3, 0, 0, ctrl, ls= True, r = True)
            testAttr = ctrlName + '.rotatePivot'
            cmds.move(-3, 0, 0, testAttr, ls = True, r = True)
    elif '32_Master_Ctrl_01' in ctrlName:
        cmds.makeIdentity(ctrl, apply=True, s=1, n=2 )
        cmds.move(3, 0, 0, ctrl, ls= True, r = True)
        testAttr = ctrlName + '.rotatePivot'
        cmds.move(-3, 0, 0, testAttr, ls = True, r = True)        
    cmds.makeIdentity(ctrl, apply=True, t=1, r=1, s=1, n=2 )
    cmds.delete(ctrl, ch = True)
    returnList = [ctrlName, grpName]
    return returnList
    
def connectTRS(sel1, sel2, type):
    if 't' in type:
        cmds.connectAttr(sel1 + ".translate", sel2 + ".translate")
    if 'r' in type:
        cmds.connectAttr(sel1 + ".rotate", sel2 + ".rotate")
    if 's' in type:
        cmds.connectAttr(sel1 + ".scale", sel2 + ".scale")

def connectTRSn(type):
    sel = cmds.ls(sl = True)
    
    sel1 = sel[0]
    sel2 = sel[1]
    if 't' in type:
        cmds.connectAttr(sel1 + ".translate", sel2 + ".translate")
    if 'r' in type:
        cmds.connectAttr(sel1 + ".rotate", sel2 + ".rotate")
    if 's' in type:
        cmds.connectAttr(sel1 + ".scale", sel2 + ".scale")
    
def bellCurve(number, total):
    results = []
    num = float(number)
    tot = float(total)
    percent = int(round(num/tot*50, 0))
    
    if percent == 0:
        results.append(0.0)
        results.append(100-results[0])
        return results
    elif percent == 1:
        results.append(0.118)
        results.append(100-results[0])
        return results        
    elif percent == 2:
        results.append(0.467)
        results.append(100-results[0])
        return results              
    elif percent == 3:
        results.append(1.037)
        results.append(100-results[0])
        return results        
    elif percent == 4:
        results.append(1.818)
        results.append(100-results[0])
        return results      
    elif percent == 5:
        results.append(2.8)
        results.append(100-results[0])
        return results
    elif percent == 6:
        results.append(3.974)
        results.append(100-results[0])
        return results           
    elif percent == 7:
        results.append(5.331)
        results.append(100-results[0])
        return results           
    elif percent == 8:
        results.append(6.861)
        results.append(100-results[0])
        return results
    elif percent == 9:
        results.append(8.554)
        results.append(100-results[0])
        return results         
    elif percent == 10:
        results.append(10.4)
        results.append(100-results[0])
        return results
    elif percent == 11:
        results.append(12.39)
        results.append(100-results[0])
        return results
    elif percent == 12:
        results.append(14.515)
        results.append(100-results[0])
        return results
    elif percent == 13:
        results.append(16.765)
        results.append(100-results[0])
        return results
    elif percent == 14:
        results.append(19.13)
        results.append(100-results[0])
        return results
    elif percent == 15:
        results.append(21.6)
        results.append(100-results[0])
        return results
    elif percent == 16:
        results.append(24.166)
        results.append(100-results[0])
        return results
    elif percent == 17:
        results.append(26.819)
        results.append(100-results[0])
        return results        
    elif percent == 18:
        results.append(29.549)
        results.append(100-results[0])
        return results        
    elif percent == 19:
        results.append(32.346)
        results.append(100-results[0])
        return results      
    elif percent == 20:
        results.append(35.2)
        results.append(100-results[0])
        return results  
    elif percent == 21:
        results.append(38.102)
        results.append(100-results[0])
        return results        
    elif percent == 22:
        results.append(41.043)
        results.append(100-results[0])
        return results
    elif percent == 23:
        results.append(44.013)
        results.append(100-results[0])
        return results
    elif percent == 24:
        results.append(47.002)
        results.append(100-results[0])
        return results
    elif percent == 25:
        results.append(50.0)
        results.append(100-results[0])
        return results
    elif percent == 26:
        results.append(52.998)
        results.append(100-results[0])
        return results
    elif percent == 27:
        results.append(55.987)
        results.append(100-results[0])
        return results
    elif percent == 28:
        results.append(58.957)
        results.append(100-results[0])
        return results
    elif percent == 29:
        results.append(61.898)
        results.append(100-results[0])
        return results
    elif percent == 30:
        results.append(64.8)
        results.append(100-results[0])
        return results
    elif percent == 31:
        results.append(67.654)
        results.append(100-results[0])
        return results
    elif percent == 32:
        results.append(70.451)
        results.append(100-results[0])
        return results 
    elif percent == 33:
        results.append(73.181)
        results.append(100-results[0])
        return results 
    elif percent == 34:
        results.append(75.834)
        results.append(100-results[0])
        return results
    elif percent == 35:
        results.append(78.4)
        results.append(100-results[0])
        return results
    elif percent == 36:
        results.append(80.87)
        results.append(100-results[0])
        return results 
    elif percent == 37:
        results.append(83.235)
        results.append(100-results[0])
        return results
    elif percent == 38:
        results.append(85.485)
        results.append(100-results[0])
        return results
    elif percent == 39:
        results.append(87.61)
        results.append(100-results[0])
        return results
    elif percent == 40:
        results.append(89.6)
        results.append(100-results[0])
        return results
    elif percent == 41:
        results.append(91.466)
        results.append(100-results[0])
        return results
    elif percent == 42:
        results.append(93.139)
        results.append(100-results[0])
        return results
    elif percent == 43:
        results.append(94.669)
        results.append(100-results[0])
        return results
    elif percent == 44:
        results.append(96.026)
        results.append(100-results[0])
        return results
    elif percent == 45:
        results.append(97.2)
        results.append(100-results[0])
        return results
    elif percent == 46:
        results.append(98.182)
        results.append(100-results[0])
        return results
    elif percent == 47:
        results.append(98.963)
        results.append(100-results[0])
        return results
    elif percent == 48:
        results.append(99.533)
        results.append(100-results[0])
        return results
    elif percent == 49:
        results.append(99.882)
        results.append(100-results[0])
        return results
    elif percent == 50:
        results.append(100)
        results.append(100-results[0])
        return results
    elif percent == 51:
        results.append(99.882)
        results.append(100-results[0])
        return results
    elif percent == 52:
        results.append(99.533)
        results.append(100-results[0])
        return results
    elif percent == 53:
        results.append(98.963)
        results.append(100-results[0])
        return results
    elif percent == 54:
        results.append(98.182)
        results.append(100-results[0])
        return results
    elif percent == 55:
        results.append(97.2)
        results.append(100-results[0])
        return results
    elif percent == 56:
        results.append(96.026)
        results.append(100-results[0])
        return results
    elif percent == 57:
        results.append(94.669)
        results.append(100-results[0])
        return results
    elif percent == 58:
        results.append(93.139)
        results.append(100-results[0])
        return results
    elif percent == 59:
        results.append(91.446)
        results.append(100-results[0])
        return results
    elif percent == 60:
        results.append(89.6)
        results.append(100-results[0])
        return results
    elif percent == 61:
        results.append(87.61)
        results.append(100-results[0])
        return results
    elif percent == 62:
        results.append(85.485)
        results.append(100-results[0])
        return results
    elif percent == 63:
        results.append(83.235)
        results.append(100-results[0])
        return results
    elif percent == 64:
        results.append(80.87)
        results.append(100-results[0])
        return results
    elif percent == 65:
        results.append(78.4)
        results.append(100-results[0])
        return results
    elif percent == 66:
        results.append(75.834)
        results.append(100-results[0])
        return results
    elif percent == 67:
        results.append(73.181)
        results.append(100-results[0])
        return results
    elif percent == 68:
        results.append(70.451)
        results.append(100-results[0])
        return results
    elif percent == 69:
        results.append(67.654)
        results.append(100-results[0])
        return results
    elif percent == 70:
        results.append(64.8)
        results.append(100-results[0])
        return results
    elif percent == 71:
        results.append(61.898)
        results.append(100-results[0])
        return results
    elif percent == 72:
        results.append(58.957)
        results.append(100-results[0])
        return results
    elif percent == 73:
        results.append(55.987)
        results.append(100-results[0])
        return results
    elif percent == 74:
        results.append(52.998)
        results.append(100-results[0])
        return results
    elif percent == 75:
        results.append(50)
        results.append(100-results[0])
        return results
    elif percent == 76:
        results.append(47.002)
        results.append(100-results[0])
        return results
    elif percent == 77:
        results.append(44.013)
        results.append(100-results[0])
        return results
    elif percent == 78:
        results.append(41.043)
        results.append(100-results[0])
        return results
    elif percent == 79:
        results.append(38.102)
        results.append(100-results[0])
        return results
    elif percent == 80:
        results.append(35.2)
        results.append(100-results[0])
        return results
    elif percent == 81:
        results.append(32.346)
        results.append(100-results[0])
        return results
    elif percent == 82:
        results.append(29.549)
        results.append(100-results[0])
        return results
    elif percent == 83:
        results.append(26.819)
        results.append(100-results[0])
        return results
    elif percent == 84:
        results.append(24.166)
        results.append(100-results[0])
        return results
    elif percent == 85:
        results.append(21.6)
        results.append(100-results[0])
        return results
    elif percent == 86:
        results.append(19.13)
        results.append(100-results[0])
        return results
    elif percent == 87:
        results.append(16.765)
        results.append(100-results[0])
        return results
    elif percent == 88:
        results.append(14.515)
        results.append(100-results[0])
        return results
    elif percent == 89:
        results.append(12.39)
        results.append(100-results[0])
                
def duplicateJntChain(sel, old, new):
    newJnts = []
    newJntNames = []
    for s in sel:
        newName = str(s).replace(old, new)
        newJnts.append(cmds.duplicate(s, po = True, n = newName))
        newJntNames.append(newName)
    for index in range(0, (len(newJnts) - 1)):
        cmds.parent(newJnts[index + 1], newJnts[index])
    return newJntNames
        
def pvLocCreate(sel, locName, direction, amount):
    locTran = cmds.xform(sel, q = True, t = True, ws = True)
    locRot = cmds.xform(sel, q = True, ro = True, ws = True)
    loc = cmds.spaceLocator(n = locName)
    grpName = locName.replace('Ctrl', 'Grp')
    locGrp = cmds.group(em = True, n = grpName)
    cmds.parent(locName, grpName)
    cmds.xform(locGrp, t = locTran, ws = True)
    cmds.xform(locGrp, ro = locRot, ws = True)
    cmds.setAttr(locName + '.rotate', 0, 0, 0)
    if 'x' in direction:
        cmds.setAttr(locName + '.translate', amount, 0, 0)
    if 'y' in direction:
        cmds.setAttr(locName + '.translate', 0, amount, 0)
    if 'z' in direction:
        cmds.setAttr(locName + '.translate', 0, 0, amount)
    cmds.makeIdentity(loc, apply=True, s=1, t = True, n=2)
    cmds.setAttr(locName + '.localScale', 4, 4, 4)
    return locGrp
    
def makeShape(shape, name):
    if shape == 'cube' or shape == 'Cube':
        curve = cmds.curve(d = 1, p = [(0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5)], n = name)
    return curve