#!/usr/bin/env python
import subprocess
import argparse
'''Dynamically map open windows to function keys for easy access. Can be called both for setting and calling saved windows.
Designed to be invoked via environment-wide keybindings.'''

parser = argparse.ArgumentParser(description='Run with arguments of "<mode[set|trigger]>" "<button[F2-F4]>"')
parser.add_argument("mode")
parser.add_argument("button")
args = parser.parse_args()

destDir = "/tmp/"

def saveWindowToKey (window, button):
	saveFile = open(destDir + button + ".binding", 'w')
	saveFile.write(window)
	saveFile.close()
	print("-=- Window " + window + " mapped to " + button + ".")

def triggerWindowOnKey (button):
	saveFile = open(destDir + button + ".binding", 'r')
	desiredWindow = saveFile.read()
	raiseWindowCmd = "wmctrl -a " + desiredWindow
	subprocess.Popen(raiseWindowCmd, shell=True, stdout=subprocess.PIPE)

if args.mode == "set":
	activeWindow = subprocess.Popen("xdotool getactivewindow getwindowname", shell=True, stdout=subprocess.PIPE).stdout.read().strip()
	saveWindowToKey(activeWindow, args.button)
	messageCmd  = "notify-send 'Binding set.' '" + args.button + " -> " + activeWindow + "'"
	subprocess.Popen(messageCmd, shell=True, stdout=subprocess.PIPE)

elif args.mode == "trigger":
	triggerWindowOnKey(args.button)





