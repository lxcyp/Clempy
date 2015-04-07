#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# clemplaying.py
# Uses dbus to gather information about the current playing track. Modification of anowplaying.py to add proper unicode support.

import sys
import dbus, optparse, shutil, subprocess
from subprocess import call, check_output

if __name__ == "__main__":
	# Check for running clementine
	output = check_output(["ps","-A"]).decode('utf-8')
	if 'clementine' not in output: 
		sys.exit()	
		print("Clementine is not running. Quitting.")

	bus = dbus.SessionBus()
	clementine = bus.get_object('org.mpris.clementine', '/Player')
	clementinedict = clementine.GetMetadata()
	
	#Parser
	usage = "Usage: %prog [options]"
	parser = optparse.OptionParser(usage=usage)
	parser.add_option('-a', '--artist', action='store_true', help='Artist name')
	parser.add_option('-t',  '--title', action='store_true', help='Track title')
	parser.add_option('-l', '--album', action='store_true', help='Album name')
	parser.add_option('-c', '--cover', metavar='filename', help='copy cover art')


	#Get options
	(opts, args) = parser.parse_args()
	if opts.artist and 'artist' in clementinedict:
		print(clementinedict['artist'])
	if opts.title and 'title' in clementinedict:
		print(clementinedict['title'])
	if opts.album and 'album' in clementinedict:
		print(clementinedict['album'])
	if opts.cover:
		cover = clementinedict['arturl']
		if cover != "":
			try:
				shutil.copyfile(cover.replace('file://', ''), opts.cover)
				print ("")
			except Exception as e:
				print (e)
		else:
			pritnt ("")
