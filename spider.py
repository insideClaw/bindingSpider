#!/usr/bin/env python
import subprocess
import argparse
'''Dynamically map open windows to function keys for easy access. Can be called both for setting and calling saved windows.
Designed to be invoked via environment-wide keybindings.'''

parser = argparse.ArgumentParser(description='-=- Run with arguments of "<mode[set|trigger]>" and "<button>"')
parser.add_argument("mode")
parser.add_argument("button")
args = parser.parse_args()

destDir = "/tmp/"

def saveWindowToKey (window, button):
	'''Takes the name of a window, the keybind desired and saves for future use.'''
	saveFile = open(destDir + button + ".binding", 'w')
	saveFile.write(window)
	saveFile.close()
	print("-=- Window " + window + " mapped to " + button + ".")

def triggerWindowOnKey (button):
	'''Given a keybind button, raises the window mapped to it (if any)'''
	saveFile = open(destDir + button + ".binding", 'r')
	desiredWindow = saveFile.read()
	raiseWindowCmd = "wmctrl -i -a " + desiredWindow
	subprocess.Popen(raiseWindowCmd, shell=True, stdout=subprocess.PIPE)

# Allows for being called as both a setter and a getter, defined with ARG1
if args.mode == "set":
	activeWindowName = subprocess.Popen("xdotool getactivewindow getwindowname", shell=True, stdout=subprocess.PIPE).stdout.read().strip()
	activeWindowID = subprocess.Popen("wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | \
		awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/') | cut -f1 -d ' '", shell=True, stdout=subprocess.PIPE).stdout.read().strip()
	saveWindowToKey(activeWindowID, args.button)
	messageCmd  = "notify-send 'Binding set.' '" + args.button + " -> " + activeWindowName + "'"
	subprocess.Popen(messageCmd, shell=True, stdout=subprocess.PIPE)

elif args.mode == "trigger":
	triggerWindowOnKey(args.button)





