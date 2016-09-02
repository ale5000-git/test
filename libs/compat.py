# Compatibility layer
#
# Copyright (C) 2016  ale5000
# License: GNU Lesser General Public License v3+

def fix_builtins():
    import sys;
    override_dict = {};
    orig_print = None;
    used_print = None;

    if(__builtins__.__class__ is dict):
        builtins_dict = __builtins__;
    else:
        try:
            import builtins;
        except ImportError:
            import __builtin__ as builtins;
        builtins_dict = builtins.__dict__;

    def _print_wrapper(*args, **kwargs):
        orig_print("PRINT WRAPPER");
        flush = kwargs.get("flush", False);
        if "flush" in kwargs: del kwargs["flush"];
        orig_print(*args, **kwargs);
        if flush: kwargs.get("file", sys.stdout).flush();

    def _print_full(*args, **kwargs):
        opt = {"sep": " ", "end": "\n", "file": sys.stdout, "flush": False};
        for key in kwargs:
            if(key in opt):
                opt[key] = kwargs[key];
            else:
                raise TypeError("'"+key+"' is an invalid keyword argument for this function");
        opt["file"].write(opt["sep"].join(str(val) for val in args)+opt["end"]);
        if opt["flush"]:
            opt["file"].flush();

    def _sorted(list):
        list.sort();
        return list;

    # Function 'print' (also aliased as print_)
    if sys.version_info >= (3, 3):
        used_print = builtins_dict.get("print");
    else:
        if sys.version_info >= (2, 6):
            orig_print = builtins_dict.get("print");
            used_print = _print_wrapper;
        else:
            used_print = _print_full;
        override_dict["print"] = used_print;
    override_dict["print_"] = used_print;
    # Function 'sorted'
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
