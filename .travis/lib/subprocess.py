#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class CalledProcessError(Exception):
	"""Raised when a process run by check_call() or check_output()
	returns a non-zero exit status."""

	def __init__(self, returncode, cmd, output=None, stderr=None):
		self.returncode = returncode
		self.cmd = cmd
		self.output = output
		self.stdout = output
		self.stderr = stderr

class ExtCalledProcessError(subprocess.CalledProcessError):
	"""Raised when a process run by check_call() or check_output()
	returns a non-zero exit status."""

	def __init__(self, returncode, cmd, output=None, stderr=None):
		try:
			super(ExtCalledProcessError, self).__init__(returncode=returncode,
														cmd=cmd, output=output, stderr=stderr)
		except TypeError:
			try:
				super(ExtCalledProcessError, self).__init__(returncode=returncode,
															cmd=cmd, output=output)
			except TypeError:
				super(ExtCalledProcessError, self).__init__(returncode=returncode,
															cmd=cmd)
				self.output = output
			self.stdout = output
			self.stderr = stderr

def check(*args, **kwargs):
	if "stdout" in kwargs:
		raise ValueError("stdout argument not allowed, "
						 "it will be overridden.")
	process = subprocess.Popen(stdout=subprocess.PIPE, *args, **kwargs)
	stdout_data, __ = process.communicate()
	ret_code = process.poll()
	if ret_code is None:
		raise RuntimeWarning("The process is not yet terminated.")
	if ret_code:
		cmd = kwargs.get("args")
		if cmd is None:
			cmd = args[0]
		raise ExtCalledProcessError(returncode=ret_code, cmd=cmd, output=stdout_data)
	return stdout_data

def check_call(*args, **kwargs):
	if "stdout" in kwargs:
		raise ValueError("stdout argument not allowed, "
						 "it will be overridden.")
	process = subprocess.Popen(stdout=subprocess.PIPE, *args, **kwargs)
	stdout_data, __ = process.communicate()
	ret_code = process.poll()
	if ret_code is None:
		raise RuntimeWarning("The process is not yet terminated.")
	if ret_code:
		cmd = kwargs.get("args")
		if cmd is None:
			cmd = args[0]
		raise ExtCalledProcessError(returncode=ret_code, cmd=cmd, output=stdout_data)
	return stdout_data

def _check_output(*args, **kwargs):
	if "stdout" in kwargs:
		raise ValueError("stdout argument not allowed, "
						 "it will be overridden.")
	process = subprocess.Popen(stdout=subprocess.PIPE, *args, **kwargs)
	stdout_data, __ = process.communicate()
	ret_code = process.poll()
	if ret_code is None:
		raise RuntimeWarning("The process is not yet terminated.")
	if ret_code:
		cmd = kwargs.get("args")
		if cmd is None:
			cmd = args[0]
		raise ExtCalledProcessError(returncode=ret_code, cmd=cmd, output=stdout_data)
	return stdout_data
