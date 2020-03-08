import os
import sys

def get_script_path():
    print (os.path.dirname(os.path.realpath(sys.argv[0])))

get_script_path()