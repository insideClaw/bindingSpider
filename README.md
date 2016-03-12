Bindings Spider
======

Dynamically map open windows to function keys for easy access. Avoids having to alt-tab through numerous windows to reach something commonly used (right now) windows, like the document editor or browser. 
Can be called both for setting and calling saved windows; designed to be invoked via environmental keybinds.

##To use:
1. Download and extract to a suitable place for the script.
2. chmod 755 /path/to/spider.py
3. Navigate to keyboard settings. For Gnome3 you can invoke "gnome-control-center keyboard". For each key slot desired, set a pair of bindings:

>/path/to/spider.py set F2
	Assign to Alt+F2
>/path/to/spider.py trigger F2
	Assign to F2

Check -h for full syntax.

##Idea:
Personally used to set current window with Alt+F2 and later invoke it with F2 and so on. 
Can quickly assign a pattern related to the task at hand and avoid getting lost in the midst of windows.

Core functionality works and solution alleviates the problem addressed.

* Note if the title of the mapped window changes and no longer includes the original name, the spider fetches nothing.
* Possible change to allow interactive title setting, for now edit /tmp/<key>.binding directly if needed.
