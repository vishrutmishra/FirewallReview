import sys
import os
from Modules.FileReader import File

file = os.path.join('conf',str(sys.argv[1]))
f = File(file)
f.read()