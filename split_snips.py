#!/usr/bin/env python2
'''
Script zum Aufspalten von SnipMate Snippets.
'''
import os
import re

dir_rx = re.compile(r"^(.+)\.snippets$")

snipp_rx = re.compile(r"^snippet\s+(\S+)")
comment_rx = re.compile(r"^#")
clear_rx = re.compile(r"^\s*$")
scode_rx = re.compile(r"^\t(.*\S)\s*$")

for file in os.popen("ls *.snippets"):
    file = file.strip()
    dir_path = dir_rx.match(file).group(1)
    #os.mkdir(dir_path)
    snippet = None
    source = open(file, "r")
    for line in source:
        if clear_rx.match(line):
            continue
        if comment_rx.match(line):
            print "comment:", line
            continue
        match = snipp_rx.match(line)
        if match:
            if snippet:
                snippet.close()
            #print "beginn:", line
            snippath = dir_path + "/" + match.group(1) + ".snippet"
            #print "filename:", snippath
            snippet = open(snippath, "w")
            continue
        match = scode_rx.match(line)
        if match:
            #print "code:", line
            #print "out:", match.group(1)
            snippet.write(match.group(1) + '\n')
            continue
        print "unmatched:", line
    source.close()

#out = open("log.py", "w")
#for line in _ih:
#    print line
#    out.write(line)
#out.close()
