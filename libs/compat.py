#!/usr/bin/env python

# Compatibility layer
def subprocess():
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
