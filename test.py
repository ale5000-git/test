#!/usr/bin/env python
import os;
import subprocess;

import libs.compat as CompatLayer;
CompatLayer.fix_all();

#dir_list = tuple(sorted(os.listdir(".")));
#print(dir_list);

try:
    out = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT);
    print(os.linesep+os.linesep+"Good: "+out);
except subprocess.CalledProcessError as e:
    print(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep+"Out: "+e.output.decode("utf-8").strip());

try:
    
    out = subprocess.check_output(["7za", "-h"], stderr=subprocess.STDOUT);
    print(os.linesep+os.linesep+"Good: "+out);
except subprocess.CalledProcessError as e:
    print(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep+"Out: "+e.output.decode("utf-8").strip());

try:
    out = subprocess.check_output(["7za", "-v"], stderr=subprocess.STDOUT);
    print(os.linesep+os.linesep+"Good: "+out);
except subprocess.CalledProcessError as e:
    print(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep+"Out: "+e.output.decode("utf-8").strip());
