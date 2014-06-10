#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def copyspecial(specialdir,dirlist):
  for dir in dirlist:
    filelist=''
    filenames=os.listdir(dir)
    for filename in filenames:
      if re.search(r'.+__\w+__.',filename):
        filelist=filelist+' '+filename
    print filelist
    os.mkdir(specialdir)
    cmd='cp '+filelist+' '+specialdir
    (status,output)=commands.getstatusoutput(cmd)
    if status:
      sys.stderr.write('there was an copy error:'+output)
      print 
      sys.exit(1)
    return
 

def zipspecial(specialzip,dirlist):
  for dir in dirlist:
    filelist=''
    filenames=os.listdir(dir)
    for filename in filenames:
      if re.search(r'.+__\w+__.',filename):
        filelist=filelist+' '+filename
    cmd='zip -j '+specialzip+' '+filelist
    (status,output)=commands.getstatusoutput(cmd)
    if status:
      sys.stderr.write('there was an zip error:'+output)
      print 
      sys.exit(1)
    return




def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir:
    print todir
    copyspecial(todir,args)
  if tozip:
    zipspecial(tozip,args)

  
if __name__ == "__main__":
  main()
