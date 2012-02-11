#!/usr/bin/env python2
'''
File: merge_snips.py
Author: Benjamin Kober
Description: Script used for merging of SnipMate Snippets.
'''
import os
import re

snipname_rx = re.compile(r"^\./([^/]+)/?(.*)/(.+)\.snippet$")
old_type    = ""
old_sub     = ""
sub_num     = 0
snip_file   = None

for f_name in os.popen("find . -name *.snippet"):
    f_name       = f_name.strip()
    snip_type    = snipname_rx.match(f_name).group(1)
    snip_sub     = snipname_rx.match(f_name).group(2)
    snip_trigger = snipname_rx.match(f_name).group(3)
    if old_sub != snip_sub:
        sub_num = 0
    if old_type != snip_type:
        if snip_file:
            snip_file.close()
        sub_num = 0
        f_path = snip_type + ".snippets"
        snip_file = open(f_path, "w+")
        #print "fn: %s type: %s sub: %s" % (f_name, snip_type, snip_sub)
        #print "fn: %s.snippets" % snip_type
    source = open(f_name, "r")
    if snip_sub:
        sub_num = sub_num + 1
        num_str = " #%d" % sub_num
        #print "snippet " + snip_sub + " " + snip_trigger + num_str
        snip_file.write("snippet " + snip_sub + " " + snip_trigger + num_str)
        snip_file.write("\n")
    else:
        sub_num = 0
        #print "snippet " + snip_trigger
        snip_file.write("snippet " + snip_trigger)
        snip_file.write("\n")
    for line in source:
        line = line.strip()
        #print "\t" + line
        snip_file.write("\t" + line)
        snip_file.write("\n")
    #print "\n"
    snip_file.write("\n")
    old_type = snip_type
    old_sub  = snip_sub
    source.close()
