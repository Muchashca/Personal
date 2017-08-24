import pymel.core as pmc
import sys
import types

def syspath():
	print 'sys.path:'
	for p in sys.path:
		print p
		
def info(obj):
	"""Prints information about the object."""
	
	lines = ['Info for %s' % obj.name(), 'Attributes:']
	
	# Get the name of all attributes 
	for a in obj.listAttr():
		lines.append('    ' + a.name())
	attrs = '\n'.join(lines)
	print attrs
	
	children = pmc.listRelatives(obj, c = True, typ = 'transform')
	lines = ['Children of %s' %obj.name(), 'Children:']
	for c in children:
		lines.append('    ' + c.name())
	childList = '\n'.join(lines)
	print childList
	
	parents = pmc.listRelatives(obj, p = True, typ = 'transform')
	lines = ['Parent of %s' %obj.name(), 'Parent:']
	for p in parents:
		lines.append('    ' + p.name())
	parentList = '\n'.join(lines)
	print parentList
	
	shapes = pmc.listRelatives(obj, s = True)
	lines = ['Shape of %s' %obj.name(), 'Shapes:']
	if len(shapes) > 0:
		for s in shapes:
			lines.append('    ' + s.name())
		shapesList = '\n'.join(lines)
		print shapesList
	else:
		print 'No shapes'
		
# Function converts a python object to a PyMEL help query url.
	# If the object is a string,
		# return a query string for a help search.
	# If the object is a PyMEL object,
		# return the appropriate url tail.
		# PyMEL functions, modules, types, and instances,
		# and methods are all valid.
	# Non-PyMEL objects return None.

def _py_to_helpstr(obj):
    if isinstance(obj, basestring):
        return 'search.html?q=%s' % (obj.replace(' ', '+'))
    if not _is_pymel(obj):
        return None
    if isinstance(obj, types.ModuleType):
        return ('generated/%(module)s.html#module-%(module)s' %
                dict(module=obj.__name__))
    if isinstance(obj, types.MethodType):
        return ('generated/classes/%(module)s/'
                '%(module)s.%(typename)s.html'
                '#%(module)s.%(typename)s.%(methname)s' % dict(
                    module=obj.__module__,
                    typename=obj.im_class.__name__,
                    methname=obj.__name__))
    if isinstance(obj, types.FunctionType):
        return ('generated/functions/%(module)s/'
                '%(module)s.%(funcname)s.html'
                '#%(module)s.%(funcname)s' % dict(
                    module=obj.__module__,
                    funcname=obj.__name__))
    if not isinstance(obj, type):
        obj = type(obj)
    return ('generated/classes/%(module)s/'
            '%(module)s.%(typename)s.html'
            '#%(module)s.%(typename)s' % dict(
                module=obj.__module__,
                typename=obj.__name__))
				
# Function takes a python object and returns a full help url.
	# Calls the first function.
	# If first function returns None, 
		# just use built in 'help' function.
	# Otherwise, open a web browser to the help page.

def test_py_to_helpstr():
    def dotest(obj, ideal):
		result = _py_to_helpstr(obj)
		assert result == ideal, '%s != %s' % (result, ideal)
    dotest('maya rocks', 'search.html?q=maya+rocks')
    dotest(pmc.nodetypes,
           'generated/pymel.core.nodetypes.html'
           '#module-pymel.core.nodetypes')
    dotest(pmc.nodetypes.Joint,
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint')
    dotest(pmc.nodetypes.Joint(),
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint')
    dotest(pmc.nodetypes.Joint().getTranslation,
           'generated/classes/pymel.core.nodetypes/'
           'pymel.core.nodetypes.Joint.html'
           '#pymel.core.nodetypes.Joint.getTranslation')
    dotest(pmc.joint,
           'generated/functions/pymel.core.animation/'
           'pymel.core.animation.joint.html'
           '#pymel.core.animation.joint')
    dotest(object(), None)
    dotest(10, None)
    dotest([], None)
    dotest(sys, None)
	
def _is_pymel(obj):
    try: # (1)
        module = obj.__module__ # (2)
    except AttributeError: # (3)
        try:
            module = obj.__name__ # (4)
        except AttributeError:
            return None # (5)
    return module.startswith('pymel') # (6)