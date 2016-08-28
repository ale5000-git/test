#!/usr/bin/env python
import os;
import subprocess;

import libs.compat as CompatLayer;
#CompatLayer.fix_all();

import sys;
print("0: "+str(sys.modules.__builtin__))
print("1: "+str(__builtins__));
#import __builtin__;
#print("2: "+str(__builtin__));
print("3: "+str(sorted));

#dir_list = tuple(sorted(os.listdir(".")));
#print(dir_list);

try:
    subprocess.check_output(["java", "-v"], stderr=subprocess.STDOUT);
except subprocess.CalledProcessError as e:
    print(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep+"Out: "+e.output.decode("utf-8").strip());
