import sys
import os
from Modules.FileReader import FileReader

file = os.path.join('conf',str(sys.argv[1]))
f = FileReader(file)