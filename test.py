#!/usr/bin/env python
import os, sys, platform, subprocess, tempfile, shutil;

out = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT);
print("out: '" + out.decode().rstrip() + "'" + os.linesep);
