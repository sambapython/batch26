'''
import sys
print "sys imported"
sys.path.append('/home/tcloudost/Desktop')
print sys.path
import f1
print f1.__file__
print f1.fun()

import f2
print "app.py output"
print f2.fun()
'''
'''
import f2
print f2.fun()
print f2.fun1()
'''
'''
import batch27
print batch27.file1.fun()
'''
'''
from batch27 import file1,file2
print file1.fun()
print file2.fun()
'''
'''
import batch27
print batch27.file1.fun()
print batch27.file2.fun()
'''
#from batch27 import file1
#from batch27 import *
'''
import f2
print f2.a
'''
'''
from f2 import *
print a 
print b 
print a+b
a=20000
print fun2()
'''
import batch27
print batch27.file1.file4.fun()

