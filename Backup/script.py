#!/usr/bin/env python
import sys;
import os;
import subprocess;

curdir = os.getcwd();
sys.path.insert(1, curdir+os.sep+"libs");

import pycompatlayer;
pycompatlayer.fix_all();

def func1(object):
    """This class docstring"""
    return True

try:
    out = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT);
    #print_(os.linesep+os.linesep+"Output: "+out.decode());
except subprocess.CalledProcessError as e:
    pass
    #print_(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    #print_("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep);
    #print_("Out: "+e.output.decode("utf-8").strip()+os.linesep+"Out: "+e.stdout.decode("utf-8").strip()+os.linesep+"Err: "+str(e.stderr));

#if sys.version_info >= (3, 3):
    #print_(1)
#else:
    #print_(2)
