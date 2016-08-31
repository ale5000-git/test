#!/usr/bin/env python

# Compatibility layer
def fix_builtins():
    import sys;
    override_dict = {};

    def _print(*args, **kwargs):
        opt = {"sep": " ", "end": "\n", "file": sys.stdout, "flush": False};
        for key in kwargs:
            if(key in opt):
                opt[key] = kwargs[key];
            else:
                raise TypeError("'"+key+"' is an invalid keyword argument for this function");
        opt["file"].write(opt["sep"].join(val for val in args));
        if(opt["end"] != ""): opt["file"].write(opt["end"]);
        if opt["flush"]: opt["file"].flush();

    def _sorted(list):
        print("CUSTOM SORTED");
        list.sort();
        return list;

    sys.stdout.write(type(__builtins__.get["print"]));
    sys.stdout.write(str(__builtins__.get["print"]));
    _print("'", end="");
    _print("abc", "def", flush=False, end="");
    _print("'", end="");
    _print();
    sys.exit();

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

    if builtins_dict.get("sorted") is None:
        override_dict["sorted"] = _sorted;
    builtins_dict.update(override_dict);

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
