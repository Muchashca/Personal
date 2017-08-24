def ehToolboxCreate():
    import maya.cmds as cmds
    import maya.mel as mel

    if cmds.window('ehToolbox', ex = True):
        cmds.deleteUI('ehToolbox')
    ehToolbox = cmds.window('ehToolbox', widthHeight=(200, 150) )

    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 5), (tabs, 'left', 5), (tabs, 'bottom', 5), (tabs, 'right', 5)))

    child1 = cmds.rowColumnLayout(numberOfColumns=4)
    cmds.symbolButton(image='square.xpm', c = jntChainFromSelection, ann = 'Joint Chain From Selection')
    jntModeBtn = cmds.symbolButton(image='square.xpm', c = jointOrientModeToggle, ann = 'Joint Orient Mode: Right click to manually select mode')
    jntModePopup = cmds.popupMenu(parent=jntModeBtn, ctl=False, button=3)
    jntModeitem1 = cmds.menuItem(l='Joint Orient Mode On', c = jointOrientModeOn)
    jntModeitem2 = cmds.menuItem(l='Joint Orient Mode Off', c = jointOrientModeOff)
    cmds.symbolButton(image='square.xpm', c = selNextSkinJnt, ann = 'Next Skin Joint', en = False)
    cmds.symbolButton(image='square.xpm', c = selectHi, ann = 'Select Hierarchy')
    cmds.symbolButton(image='square.xpm', c = sceneAnalyzerCreate, ann = 'Scene Analyzer')
    connectBtn = cmds.symbolButton(image='square.xpm', c = lambda x: connectTRSn('trsv'), ann = 'Connect Transform: Left click for all, right click for individual channels')
    connectPopup = cmds.popupMenu(parent=connectBtn, ctl=False, button=3)
    connectitem1 = cmds.menuItem(l='Connect Translate', c = lambda x: connectTRSn('t'))
    connectitem2 = cmds.menuItem(l='Connect Rotate', c = lambda x: connectTRSn('r'))
    connectitem3 = cmds.menuItem(l='Connect Scale', c = lambda x: connectTRSn('s'))
    connectitem4 = cmds.menuItem(l='Connect Visibility', c = lambda x: connectTRSn('v'))
    ctrlBtn = cmds.symbolButton(image='square.xpm', c = lambda x: makeCtrl(True), ann = 'Make Simple Control: Right click for no constraint')
    ctrlPopup = cmds.popupMenu(parent=ctrlBtn, ctl=False, button=3)
    connectitem1 = cmds.menuItem(l='Unconstrained Control', c = lambda x: makeCtrl(False))
    cmds.symbolButton(image='square.xpm', c = basicAutoRigger, ann = 'WIP Autorigger')


    cmds.setParent( '..' )

    cmds.tabLayout( tabs, edit=True, tabLabel=(child1, 'One'))

    #cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'One'), (child2, 'Two'), (child3, 'Three')))

    cmds.dockControl(area='left', content=ehToolbox, allowedArea='all')

ehToolboxCreate()