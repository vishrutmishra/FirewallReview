import sys
import os
from Modules.File import File

file = os.path.join('conf',str(sys.argv[1]))
f = File(file)