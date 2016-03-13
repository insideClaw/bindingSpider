Binding Spider
======

Dynamically map open windows to function keys for easy access. Avoids having to alt-tab through numerous windows to reach commonly used windows (at present), like the document editor or browser. 
Can be called both for setting and calling saved windows; designed to be invoked via environmental keybinds.

##To use:
1. Download and extract to a suitable place for the script.
2. chmod 755 /path/to/spider.py
3. Navigate to keyboard settings. For Gnome3 you can invoke "gnome-control-center keyboard". For each key slot desired, set a pair of bindings:

>/path/to/spider.py set F2
 
* Assign to Alt+F2

>/path/to/spider.py trigger F2

* Assign to F2

Press the Setter key on a favorite window, do something else, press the Trigger key to focus back to it.

Check -h for full syntax.

##Idea:
Personally used to set current window with Alt+F2 and later invoke it with F2 and so on. 
Can quickly assign a pattern related to the task at hand and avoid getting lost in the midst of windows.

Core functionality works and solution alleviates the problem addressed.

* Uses /tmp/KEY.binding to store bindings, kept in Hexadecimal identity format "wmctrl" window manager style.
