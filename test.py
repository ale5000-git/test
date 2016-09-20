#!/usr/bin/env python
import sys;
import os;
import subprocess;

curdir = os.getcwd();
sys.path.insert(1, curdir+os.sep+"libs");

import compatlayer;
compatlayer.fix_all();

try:
    out = subprocess.check_output(["java", "-versionX"], stderr=subprocess.STDOUT);
    print_(os.linesep+os.linesep+"Output: "+out.decode());
except subprocess.CalledProcessError as e:
    print_(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print_("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep);
    print_("Out: "+e.output.decode("utf-8").strip()+os.linesep+"Out: "+e.stdout.decode("utf-8").strip()+os.linesep+"Err: "+str(e.stderr));
