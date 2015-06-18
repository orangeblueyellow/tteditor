# This is a hack fix to get the graphics pipes to load with my
# hacked up Panda3D.
try:
    import libpandadx9
except:
    pass

try:
    import libpandadx8
except:
    pass

try:
    import libpandagl
except:
    pass

print 'DirectStart: Starting the game.'

from direct.showbase import ShowBase
base = ShowBase.ShowBase()
