import idlelib
import os
from subprocess import *

# print(os.getcwd())

#open demp.py
demo_fil = os.path.join(os.getcwd(),'demo.py')
if os.path.exists(demo_fil):
	idle_bat = idlelib.__file__.replace('__init__.py','idle.bat')
	Popen(f'{idle_bat} "{demo_fil}"')

