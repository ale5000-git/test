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

def check(*args, **kwargs):
	if "stdout" in kwargs:
		raise ValueError("stdout argument not allowed, "
						 "it will be overridden.")
	process = os.popen(*args)
	print process.read()

def check_call(*args, **kwargs):
	if "stdout" in kwargs:
		raise ValueError("stdout argument not allowed, "
						 "it will be overridden.")
	process = os.popen(*args)
	print process.read()

def check_output(*args, **kwargs):
	if "stdout" in kwargs:
		raise ValueError("stdout argument not allowed, "
						 "it will be overridden.")
	process = os.popen(*args)
	return process.read()
