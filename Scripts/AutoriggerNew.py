import pymel.core.datatypes as dt
import pymel.core as pm

def templateSetup(*template):
    for t in template:
        if t.get('type') == 'Arm':
            for j in t['joints']:
                joint = pmc.joint(n = j.get('name'), r = 1)
                joint.translate.set(j.get('pos'))
                joint.jointOrient.set(j.get('ori'))
                print j.get('ori')

clavicleLPos = dt.Vector(4.328, 146.095, -3.051)
clavicleLRot = dt.Vector(0, 0, 0)
clavicleLOri = dt.Vector(0, 0, 162.409)
clavicleL = {'name':'clavicle_L_B_Jnt', 'order':'xyz', 'pos':clavicleLPos, 'rot':clavicleLRot, 'ori':clavicleLOri}
shoulderLPos = dt.Vector(-7.772, 0, 0)
shoulderLRot = dt.Vector(0, 0, 0)
shoulderLOri = dt.Vector(0, 0, -30.983)
shoulderL = {'name':'shoudler_L_B_Jnt', 'order':'xyz', 'pos':shoulderLPos, 'rot':shoulderLRot, 'ori':shoulderLOri}
armLJoints = [clavicleL, shoulderL]
arm1 = {'name':'Arm_01', 'type':'Arm', 'joints':armLJoints}

template = [arm1]

templateSetup(*template)








armR = {'shoulderL': 'Left_Shoulder', 'shoulderR': 'Right_Shoulder'}

templateSetup(armR)

def test_args_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

# first with *args
args = ("two", 3,5)
test_args_kwargs(*args)

# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)

lis=[1, 2, 3, 4]
dic={'a': 10, 'b':20}

def test(*args, **kwargs):
    print(kwargs)

test(lis)

def func(**stuff):
    print(stuff)

func(one = 1, two = 2)

def k(**kwargs):
    if 'a' in  kwargs:
        print kwargs['a']
    if 'b' in kwargs:
        print kwargs['b']
    if 'leg2' in kwargs:
        print 'leg2'

d={'a':30,'b':40}
k(**d)

['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']



