#!/usr/bin/env python
import subprocess;

def initialize():
    class ExtendedCalledProcessError(subprocess.CalledProcessError):
        def __init__(self, returncode, cmd, output=None, stderr=None):
            try:
                super(self.__class__, self).__init__(returncode, cmd, output);
            except TypeError:
                super(self.__class__, self).__init__(returncode, cmd);
                self.output = output;
            if getattr(self, "stdout", False) == False: self.stdout = output;
            self.returncode += 1;###########
            self.stderr = stderr;
    subprocess.ExtendedCalledProcessError = ExtendedCalledProcessError;

#if "check_output" not in dir(subprocess):
    def check_output(*popenargs, **kwargs):
        if "stdout" in kwargs:
            raise ValueError("stdout argument not allowed, it will be overridden.");
        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs);
        stdout_data, __ = process.communicate();
        ret_code = process.poll();
        if ret_code is None:
            raise RuntimeWarning("The process is not yet terminated.");
        if ret_code:
            cmd = kwargs.get("args");
            if cmd is None:
                cmd = popenargs[0];
            raise subprocess.CalledProcessError(returncode=ret_code, cmd=cmd, output=stdout_data, stderr=None);
        return stdout_data;
    subprocess.check_output2 = check_output;



import os;
initialize();
def test(one = True):
    if one: return subprocess.check_output(["java", "-v"], stderr=subprocess.STDOUT);
    return subprocess.check_output2(["java", "-v"], stderr=subprocess.STDOUT);


try:
    test(False);
except subprocess.CalledProcessError as e:
    print(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep+"Out1: "+str(e.output).strip()+os.linesep+"Out2: "+str(e.stdout).strip()+os.linesep+"Err: "+str(e.stderr).strip());

print(os.linesep+os.linesep+os.linesep);

try:
    pass#test(True);
except subprocess.CalledProcessError as e:
    print(os.linesep+os.linesep+"E: "+str(e)+os.linesep);
    print("Return: "+str(e.returncode)+os.linesep+"Cmd: "+str(e.cmd)+os.linesep+str(e.output).strip()+os.linesep+str(""));#e.output.decode("utf-8").strip()
