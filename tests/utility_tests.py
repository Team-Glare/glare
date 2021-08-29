import sys
import os

# Add the root directory to the system path
# This is so we can import any subdirectories of that root directory - i.e. glare/utility.py
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from glare.utility.py import inc

def test_inc():
    num = 1
    return True
