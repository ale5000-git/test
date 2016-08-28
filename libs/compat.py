#!/usr/bin/env python

# Compatibility layer
def fix_builtins():
    def _sorted(list):
        print("CUSTOM SORTED");
        list.sort();
        return list;

    try:
        if __builtins__.get("sorted") is None:
            __builtins__.update(sorted=_sorted);
        print("CUSTOM 1");
    except AttributeError:
        try:
            import builtins;
            print("CUSTOM 2");
        except ImportError:
            import __builtin__ as builtins;
            print("CUSTOM 3");
        if getattr(builtins, "sorted", None) == None:
            builtins.sorted=_sorted;

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
