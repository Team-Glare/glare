import sys
import os

# Add the root directory to the system path
# This is so we can import any subdirectories of that root directory - i.e. glare/utility.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from glare.utility.py import inc, dec

def test_inc():
    num = 0
    assert inc(num) == 1
    assert inc(inc(num)) == 2

def test_dec():
    num = 1
    assert dec(num) == 0
    assert dec(dec(num)) == -1
