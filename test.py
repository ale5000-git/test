#!/usr/bin/env python
import os;
import subprocess;
import libs.compat as CompatLayer;
CompatLayer.subprocess();

try:
    subprocess.check_output(["java", "-v"], stderr=subprocess.STDOUT);
except subprocess.CalledProcessError as e:
    print(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep+"Out: "+e.output.decode("utf-8").strip());

dir_list = tuple(sorted(os.listdir(dir)));
print(dir_list);
