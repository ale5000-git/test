#!/usr/bin/env python

# Compatibility layer
def fix_builtins():
    import sys;
    override_dict = {};
    orig_print = None;

    def _print(*args, **kwargs):
        flush = kwargs.get("flush", False);
        if "flush" in kwargs: del kwargs["flush"];
        orig_print(*args, **kwargs);
        if flush: kwargs.get("file", sys.stdout).flush();

    def _sorted(list):
        print("CUSTOM SORTED");
        list.sort();
        return list;

    if(__builtins__.__class__ is dict):
        builtins_dict = __builtins__;
        print("CUSTOM 1");
    else:
        try:
            import builtins;
            print("CUSTOM 2");
        except ImportError:
            import __builtin__ as builtins;
            print("CUSTOM 3");
        builtins_dict = builtins.__dict__;

    if sys.version_info < (3, 3):
        orig_print = builtins_dict.get("print");
        override_dict["print"] = _print;
    if builtins_dict.get("sorted") is None:
        override_dict["sorted"] = _sorted;
    builtins_dict.update(override_dict);
    del override_dict;

def fix_subprocess():
    import subprocess;

    class _ExtendedCalledProcessError(subprocess.CalledProcessError):
        def __init__(self, returncode, cmd, output=None, stderr=None):
            try:
                super(self.__class__, self).__init__(returncode=returncode, cmd=cmd, output=output);
            except TypeError:
                super(self.__class__, self).__init__(returncode=returncode, cmd=cmd);
                self.output = output;
            if getattr(self, "stdout", False) == False: self.stdout = output;
            self.stderr = stderr;

    def _check_output(*popenargs, **kwargs):
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
            raise _ExtendedCalledProcessError(returncode=ret_code, cmd=cmd, output=stdout_data, stderr=None);
        return stdout_data;

    try:
        from subprocess import check_output;
    except ImportError:
        subprocess.check_output = _check_output;

def fix_all(override_all=False):
    fix_builtins();
    fix_subprocess();
