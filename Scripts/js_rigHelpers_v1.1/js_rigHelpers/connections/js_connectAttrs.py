'''

jsConnectAttrs

'''

# Elaborate UI to allow quick batch connecting of attributes.

import maya.cmds as mc
import sys as sys
import ast as ast

def jsCA_driverTrans():
    
    getDriverTrans = mc.ls (sl = True)
    length = len (getDriverTrans)
    
    if length == 0:
        mc.textField (jsCA_getDriverTrans_TF, e = True, text = 'Driver Objects')
        mc.warning ('Selection cannot be zero')
    
    else:    
        getDriverTransStr = str(getDriverTrans)
        getDriverTransStr = getDriverTransStr.replace ("u'", "")
        getDriverTransStr = getDriverTransStr.replace ("[", "")
        getDriverTransStr = getDriverTransStr.replace ("]", "")
        getDriverTransStr = getDriverTransStr.replace ("'", "")
        getDriverTransStr = getDriverTransStr.replace ("[", "")
        mc.textField (jsCA_getDriverTrans_TF, e = True, text = getDriverTransStr)
        
        sys.stdout.write ('Enabled zig-zag connect mode. Make sure number of driver and driven objects are the same.')

def jsCA_drivenTrans():
        
    getDrivenTrans = mc.ls (sl = True)
    length = len (getDrivenTrans)
    
    if length == 0:
        mc.textField (jsCA_getDrivenTrans_TF, e = True, text = 'Driven Objects')
        mc.warning ('Selection cannot be zero')
    
    else:
        getDrivenTransStr = str(getDrivenTrans)
        getDrivenTransStr = getDrivenTransStr.replace ("u'", "")
        getDrivenTransStr = getDrivenTransStr.replace ("[", "")
        getDrivenTransStr = getDrivenTransStr.replace ("]", "")
        getDrivenTransStr = getDrivenTransStr.replace ("'", "")
        getDrivenTransStr = getDrivenTransStr.replace ("[", "")
        mc.textField (jsCA_getDrivenTrans_TF, e = True, text = getDrivenTransStr)    
        
def jsCA_driverAttrs():
    
    getDriverAttrs = mc.channelBox ('mainChannelBox', q=True, sma=True)
    length = len (getDriverAttrs)
    
    if length == 0 or length is None:
        mc.textField (jsCA_getDriverAttrs_TF, e = True, text = 'Driver Attributes (from channel box)')
        mc.warning ('Selection must be 1')
    
    elif length > 1:
        mc.warning ('Selection must be 1')
    
    else:
        
        getDriverAttrsStr = str (getDriverAttrs)
        getDriverAttrsStr = getDriverAttrsStr.replace ("u'", "")
        getDriverAttrsStr = getDriverAttrsStr.replace ("[", "")
        getDriverAttrsStr = getDriverAttrsStr.replace ("]", "")
        getDriverAttrsStr = getDriverAttrsStr.replace ("'", "")
        getDriverAttrsStr = getDriverAttrsStr.replace ("[", "")
        mc.textField (jsCA_getDriverAttrs_TF, e = True, text = getDriverAttrsStr)
        
def jsCA_drivenAttrs():
    
    getDrivenAttrs = mc.channelBox ('mainChannelBox', q=True, sma=True)
    length = len (getDrivenAttrs)
    
    if length == 0:
        mc.textField (jsCA_getDrivenAttrs_TF, e = True, text = 'Driven Attributes (from channel box)')
        mc.warning ('Selection cannot be zero')
    
    else:
        
        getDrivenAttrsStr = str (getDrivenAttrs)
        getDrivenAttrsStr = getDrivenAttrsStr.replace ("u'", "")
        getDrivenAttrsStr = getDrivenAttrsStr.replace ("[", "")
        getDrivenAttrsStr = getDrivenAttrsStr.replace ("]", "")
        getDrivenAttrsStr = getDrivenAttrsStr.replace ("'", "")
        getDrivenAttrsStr = getDrivenAttrsStr.replace ("[", "")
        mc.textField (jsCA_getDrivenAttrs_TF, e = True, text = getDrivenAttrsStr)

def jsCA_pickQDriver():
    
    getQDriverObj = mc.ls (sl = True)[0]
    getQDriverAttrs = mc.channelBox ('mainChannelBox', q=True, sma=True)
    length = len (getQDriverAttrs)
    
    if length == 0 or length is None:
        mc.textField (jsCA_getQDriver_TF, e = True, text = 'driver.attr (from channel box)')
        mc.warning ('Selection must be 1')
    
    else:
        
        getQDriverAttrsStr = str (getQDriverAttrs)
        getQDriverAttrsStr = getQDriverAttrsStr.replace ("u'", "")
        getQDriverAttrsStr = getQDriverAttrsStr.replace ("[", "")
        getQDriverAttrsStr = getQDriverAttrsStr.replace ("]", "")
        getQDriverAttrsStr = getQDriverAttrsStr.replace ("'", "")
        getQDriverAttrsStr = getQDriverAttrsStr.replace ("[", "")
        getQDriverAttrsStr = '%s.%s' %(getQDriverObj, getQDriverAttrsStr)
        mc.textField (jsCA_getQDriver_TF, e = True, text = getQDriverAttrsStr)

def jsCA_pickQDriven():
    
    getQDrivenObj = mc.ls (sl = True)[0]
    getQDrivenAttrs = mc.channelBox ('mainChannelBox', q=True, sma=True)
    length = len (getQDrivenAttrs)
    
    if length == 0 or length is None:
        mc.textField (jsCA_getQDriven_TF, e = True, text = 'driver.attr (from channel box)')
        mc.warning ('Selection must be 1')
    
    else:
        
        getQDrivenAttrsStr = str (getQDrivenAttrs)
        getQDrivenAttrsStr = getQDrivenAttrsStr.replace ("u'", "")
        getQDrivenAttrsStr = getQDrivenAttrsStr.replace ("[", "")
        getQDrivenAttrsStr = getQDrivenAttrsStr.replace ("]", "")
        getQDrivenAttrsStr = getQDrivenAttrsStr.replace ("'", "")
        getQDrivenAttrsStr = getQDrivenAttrsStr.replace ("[", "")
        getQDrivenAttrsStr = '%s.%s' %(getQDrivenObj, getQDrivenAttrsStr)
        mc.textField (jsCA_getQDriven_TF, e = True, text = getQDrivenAttrsStr)

def jsCA_QC():
    
    jsCA_QDriver_TF_q = mc.textField (jsCA_getQDriver_TF, q = True, tx = True)
    jsCA_QDriven_TF_q = mc.textField (jsCA_getQDriven_TF, q = True, tx = True)
    
    jsCA_strList = str(jsCA_QDriven_TF_q)
    split_excludeFirst = jsCA_strList.split ('.')
    excludeFirst = jsCA_strList.replace (split_excludeFirst[0], '')
    excludeFirst = excludeFirst.replace ('.', '')
    
    jsCA_qAttrs = "['%s']" %excludeFirst
    jsCA_qAttrs = jsCA_qAttrs.replace (", ", "', '")
    jsCA_qAttrs = ast.literal_eval(jsCA_qAttrs)
    
    for attr in jsCA_qAttrs:
        
        mc.connectAttr (jsCA_QDriver_TF_q, '%s.%s' %(split_excludeFirst[0], attr))
    
def jsCA_execute():
    
    getDriverTrans = mc.textField (jsCA_getDriverTrans_TF, q = True, text = True)
    getDriverTrans = "['%s']" %getDriverTrans
    getDriverTrans = getDriverTrans.replace (", ", "', '")
    getDriverTrans = ast.literal_eval(getDriverTrans)
    
    getDrivenTrans = mc.textField (jsCA_getDrivenTrans_TF, q = True, text = True)
    getDrivenTrans = "['%s']" %getDrivenTrans
    getDrivenTrans = getDrivenTrans.replace (", ", "', '")
    getDrivenTrans = ast.literal_eval(getDrivenTrans)
    
    getDriverAttrs = mc.textField (jsCA_getDriverAttrs_TF, q = True, text = True)
    getDriverAttrs = "['%s']" %getDriverAttrs
    getDriverAttrs = getDriverAttrs.replace (", ", "', '")
    getDriverAttrs = ast.literal_eval(getDriverAttrs)
    
    getDrivenAttrs = mc.textField (jsCA_getDrivenAttrs_TF, q = True, text = True)
    getDrivenAttrs = "['%s']" %getDrivenAttrs
    getDrivenAttrs = getDrivenAttrs.replace (", ", "', '")
    getDrivenAttrs = ast.literal_eval(getDrivenAttrs)
    
    len_driverTrans = len(getDriverTrans)
    len_drivenTrans = len(getDrivenTrans)
    len_driverAttrs = len(getDriverAttrs)
    len_drivenAttrs = len(getDrivenAttrs)
    
    if 'object, object, object...' in getDriverTrans or 'object, object, object...' in getDrivenTrans or 'attr' in getDriverAttrs or 'attr, attr, attr...' in getDrivenAttrs:
        
        mc.warning ('Please fill all fields')
        pass
    
    else:
        
        if len_driverTrans == 1 and len_drivenTrans == 1:
            
            for attr in getDrivenAttrs:
                lock = mc.getAttr ('%s.%s' %(getDrivenTrans[0], attr), l = True)
                if lock == False:
                    mc.connectAttr ('%s.%s' %(getDriverTrans[0], getDriverAttrs[0]), '%s.%s' %(getDrivenTrans[0], attr))
        
        elif len_driverTrans > 1 and len_driverTrans == len_drivenTrans:
            
            count = 0
            
            for obj in getDrivenTrans:
                               
                for attr in getDrivenAttrs:
                    
                    if count <= len_driverTrans - 1:
                        
                        lock = mc.getAttr ('%s.%s' %(obj, attr), l = True)
                        if lock == False:
                            print count
                            mc.connectAttr ('%s.%s' %(getDriverTrans[count], getDriverAttrs[0]), '%s.%s' %(obj, attr))
                            
                count = count + 1
                            
                        #if count == len_driverTrans - 1:
                            
        elif len_driverTrans > 1 and len_drivenTrans < len_driverTrans:
            
            mc.warning ('Driver count must be either 1 or match driven count')
        
        elif len_driverTrans == 1 and len_drivenTrans > 1:
            
            for obj in getDrivenTrans:
                               
                for attr in getDrivenAttrs:
                    
                    lock = mc.getAttr ('%s.%s' %(obj, attr), l = True)
                    if lock == False:
                        mc.connectAttr ('%s.%s' %(getDriverTrans[0], getDriverAttrs[0]), '%s.%s' %(obj, attr))
            
            
            
def jsCA_t():
                            
    getDriverTrans = mc.textField (jsCA_getDriverTrans_TF, q = True, text = True)
    getDriverTrans = "['%s']" %getDriverTrans
    getDriverTrans = getDriverTrans.replace (", ", "', '")
    getDriverTrans = ast.literal_eval(getDriverTrans)
    print getDriverTrans[0]
    
    getDrivenTrans = mc.textField (jsCA_getDrivenTrans_TF, q = True, text = True)
    getDrivenTrans = "['%s']" %getDrivenTrans
    getDrivenTrans = getDrivenTrans.replace (", ", "', '")
    getDrivenTrans = ast.literal_eval(getDrivenTrans)
    print getDrivenTrans[0]
    
    getDriverAttrs = mc.textField (jsCA_getDriverAttrs_TF, q = True, text = True)
    getDriverAttrs = "['%s']" %getDriverAttrs
    getDriverAttrs = getDriverAttrs.replace (", ", "', '")
    getDriverAttrs = ast.literal_eval(getDriverAttrs)
    print getDriverAttrs[0]
    
    getDrivenAttrs = mc.textField (jsCA_getDrivenAttrs_TF, q = True, text = True)
    getDrivenAttrs = "['%s']" %getDrivenAttrs
    getDrivenAttrs = getDrivenAttrs.replace (", ", "', '")
    getDrivenAttrs = ast.literal_eval(getDrivenAttrs)
    print getDrivenAttrs[0]
    
    len_driverTrans = len(getDriverTrans)
    len_drivenTrans = len(getDrivenTrans)
    len_driverAttrs = len(getDriverAttrs)
    len_drivenAttrs = len(getDrivenAttrs)
    
    if len_driverTrans == 1:
            
        for obj in getDrivenTrans:
            lock = mc.getAttr ('%s.tx' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.tx' %getDriverTrans[0], '%s.tx' %obj)
            lock = mc.getAttr ('%s.ty' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.ty' %getDriverTrans[0], '%s.ty' %obj)
            lock = mc.getAttr ('%s.tz' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.tz' %getDriverTrans[0], '%s.tz' %obj)
    
    elif len_driverTrans > 1 and len_driverTrans == len_drivenTrans:
        
        count = 0
        
        for obj in getDrivenTrans:
            
            if count <= len_driverTrans - 1:
                lock = mc.getAttr ('%s.tx' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.tx' %getDriverTrans[count], '%s.tx' %obj)
                lock = mc.getAttr ('%s.ty' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.ty' %getDriverTrans[count], '%s.ty' %obj)
                lock = mc.getAttr ('%s.tz' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.tz' %getDriverTrans[count], '%s.tz' %obj)
                
                count = count + 1
                        
    elif len_driverTrans > 1 and len_driverTrans != len_drivenTrans:
        
        mc.warning ('Driver count must be either 1 or match driven count')

def jsCA_r():
                            
    getDriverTrans = mc.textField (jsCA_getDriverTrans_TF, q = True, text = True)
    getDriverTrans = "['%s']" %getDriverTrans
    getDriverTrans = getDriverTrans.replace (", ", "', '")
    getDriverTrans = ast.literal_eval(getDriverTrans)
    print getDriverTrans[0]
    
    getDrivenTrans = mc.textField (jsCA_getDrivenTrans_TF, q = True, text = True)
    getDrivenTrans = "['%s']" %getDrivenTrans
    getDrivenTrans = getDrivenTrans.replace (", ", "', '")
    getDrivenTrans = ast.literal_eval(getDrivenTrans)
    print getDrivenTrans[0]
    
    getDriverAttrs = mc.textField (jsCA_getDriverAttrs_TF, q = True, text = True)
    getDriverAttrs = "['%s']" %getDriverAttrs
    getDriverAttrs = getDriverAttrs.replace (", ", "', '")
    getDriverAttrs = ast.literal_eval(getDriverAttrs)
    print getDriverAttrs[0]
    
    getDrivenAttrs = mc.textField (jsCA_getDrivenAttrs_TF, q = True, text = True)
    getDrivenAttrs = "['%s']" %getDrivenAttrs
    getDrivenAttrs = getDrivenAttrs.replace (", ", "', '")
    getDrivenAttrs = ast.literal_eval(getDrivenAttrs)
    print getDrivenAttrs[0]
    
    len_driverTrans = len(getDriverTrans)
    len_drivenTrans = len(getDrivenTrans)
    len_driverAttrs = len(getDriverAttrs)
    len_drivenAttrs = len(getDrivenAttrs)
    
    if len_driverTrans == 1:
            
        for obj in getDrivenTrans:
            lock = mc.getAttr ('%s.rx' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.rx' %getDriverTrans[0], '%s.rx' %obj)
            lock = mc.getAttr ('%s.ry' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.ry' %getDriverTrans[0], '%s.ry' %obj)
            lock = mc.getAttr ('%s.rz' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.rz' %getDriverTrans[0], '%s.rz' %obj)
    
    elif len_driverTrans > 1 and len_driverTrans == len_drivenTrans:
        
        count = 0
        
        for obj in getDrivenTrans:
            
            if count <= len_driverTrans - 1:
                lock = mc.getAttr ('%s.rx' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.rx' %getDriverTrans[count], '%s.rx' %obj)
                lock = mc.getAttr ('%s.ry' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.ry' %getDriverTrans[count], '%s.ry' %obj)
                lock = mc.getAttr ('%s.rz' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.rz' %getDriverTrans[count], '%s.rz' %obj)
                
                count = count + 1
                        
    elif len_driverTrans > 1 and len_driverTrans != len_drivenTrans:
        
        mc.warning ('Driver count must be either 1 or match driven count')

def jsCA_s():
                            
    getDriverTrans = mc.textField (jsCA_getDriverTrans_TF, q = True, text = True)
    getDriverTrans = "['%s']" %getDriverTrans
    getDriverTrans = getDriverTrans.replace (", ", "', '")
    getDriverTrans = ast.literal_eval(getDriverTrans)
    print getDriverTrans[0]
    
    getDrivenTrans = mc.textField (jsCA_getDrivenTrans_TF, q = True, text = True)
    getDrivenTrans = "['%s']" %getDrivenTrans
    getDrivenTrans = getDrivenTrans.replace (", ", "', '")
    getDrivenTrans = ast.literal_eval(getDrivenTrans)
    print getDrivenTrans[0]
    
    getDriverAttrs = mc.textField (jsCA_getDriverAttrs_TF, q = True, text = True)
    getDriverAttrs = "['%s']" %getDriverAttrs
    getDriverAttrs = getDriverAttrs.replace (", ", "', '")
    getDriverAttrs = ast.literal_eval(getDriverAttrs)
    print getDriverAttrs[0]
    
    getDrivenAttrs = mc.textField (jsCA_getDrivenAttrs_TF, q = True, text = True)
    getDrivenAttrs = "['%s']" %getDrivenAttrs
    getDrivenAttrs = getDrivenAttrs.replace (", ", "', '")
    getDrivenAttrs = ast.literal_eval(getDrivenAttrs)
    print getDrivenAttrs[0]
    
    len_driverTrans = len(getDriverTrans)
    len_drivenTrans = len(getDrivenTrans)
    len_driverAttrs = len(getDriverAttrs)
    len_drivenAttrs = len(getDrivenAttrs)
    
    if len_driverTrans == 1:
            
        for obj in getDrivenTrans:
            lock = mc.getAttr ('%s.sx' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.sx' %getDriverTrans[0], '%s.sx' %obj)
            lock = mc.getAttr ('%s.sy' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.sy' %getDriverTrans[0], '%s.sy' %obj)
            lock = mc.getAttr ('%s.sz' %obj, l = True)
            if lock == False:
                mc.connectAttr ('%s.sz' %getDriverTrans[0], '%s.sz' %obj)
    
    elif len_driverTrans > 1 and len_driverTrans == len_drivenTrans:
        
        count = 0
        
        for obj in getDrivenTrans:
            
            if count <= len_driverTrans - 1:
                lock = mc.getAttr ('%s.sx' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.sx' %getDriverTrans[count], '%s.sx' %obj)
                lock = mc.getAttr ('%s.sy' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.sy' %getDriverTrans[count], '%s.sy' %obj)
                lock = mc.getAttr ('%s.sz' %obj, l = True)
                if lock == False:
                    mc.connectAttr ('%s.sz' %getDriverTrans[count], '%s.sz' %obj)
                
                count = count + 1
                        
    elif len_driverTrans > 1 and len_driverTrans != len_drivenTrans:
        
        mc.warning ('Driver count must be either 1 or match driven count')

# Create UI

jsCA_winHide = 'jsCA_createWin'
jsCA_winTitleHide = 'Connect Attributes'
mc.windowPref (jsCA_winHide, width = 200, height = 200)

if (mc.window (jsCA_winHide, exists = True)):
    mc.deleteUI (jsCA_winHide)

mc.window (jsCA_winHide, rtf = True, width = 200, height = 200, title = jsCA_winTitleHide, s = True)
mc.columnLayout (adj = True, rs = 2)

mc.text (' ')
mc.text ('Normal/Batch Connect', al = 'center', fn = 'boldLabelFont')
mc.text (' ')

mc.rowColumnLayout (rowSpacing = (2,1), nc = 2)

jsCA_getDriverTrans_TF = mc.textField (bgc = (.15,.15,.15), w=200, ed = 1, text = 'object, object, object...')
mc.button (l = 'Pick Driver Object', c = 'jsCA_driverTrans()')

jsCA_getDriverAttrs_TF = mc.textField (bgc = (.15,.15,.15), w=200, ed = 1, text = 'attr')
mc.button (l = 'Pick Driver Attribute', c = 'jsCA_driverAttrs()')

jsCA_getDrivenTrans_TF = mc.textField (bgc = (.15,.15,.15), w=200, ed = 1, text = 'object, object, object...')
mc.button (l = 'Pick Driven Object', c = 'jsCA_drivenTrans()')

jsCA_getDrivenAttrs_TF = mc.textField (bgc = (.15,.15,.15), w=200, ed = 1, text = 'attr, attr, attr...')
mc.button (l = 'Pick Driven Attribute', c = 'jsCA_drivenAttrs()')

mc.setParent ('..')

mc.text (' ')
mc.button (l = 'Connect', c = 'jsCA_execute()')
mc.button (l = 'Connect Translate ', c = 'jsCA_t()')
mc.button (l = 'Connect Rotate', c = 'jsCA_r()')
mc.button (l = 'Connect Scale', c = 'jsCA_s()')
mc.button (l = 'Connect Translate/Rotate/Scale', c = ('jsCA_t(), jsCA_r(), jsCA_s()'))

mc.text (' ')
mc.text ('Quick Connect', al = 'center', fn = 'boldLabelFont')
mc.text (' ')
mc.rowColumnLayout (rowSpacing = (2,1), nc = 2)
jsCA_getQDriver_TF = mc.textField (bgc = (.15,.15,.15), w=200, ed = 1, text = 'object.attr')
mc.button (w = 115, l = 'Pick Driver + Attr', c = 'jsCA_pickQDriver()')
jsCA_getQDriven_TF = mc.textField (bgc = (.15,.15,.15), w=200, ed = 1, text = 'object.attr, attr, attr...')
mc.button (w = 115, l = 'Pick Driven + Attr', c = 'jsCA_pickQDriven()')

mc.setParent ('..')

mc.text (' ')
mc.button (l = 'Quick Connect', c = 'jsCA_QC()')

mc.showWindow (jsCA_winHide)