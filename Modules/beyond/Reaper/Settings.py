# Step 1 - RemoteControl.py Action and its Cmd ID
# =======================================================================

Reaper_RemoteControl_CmdID = '_RS4f2f870dd222ceb7bbc3c77f7f5dd2ac4a09074c' # Will this change?

# From Reaper's "Actions/Show Action List…" press "ReaScript: New/load…"
# Find and select "...\Modules\beyond\Reaper\RemoteControl.py"
# Back on the Actions list, you will see "Custom: RemoteControl.py"
# Right click on the Actions list and check "Show action IDs"
# Find the "Cmd ID" column for "Custom: RemoteControl.py"
# Enter that Cmd ID number above.
#
# NOTE that this number will shift and change when a previously defined 
# Action is deleted or a Reaper extension like SWS is un/installed.
#
# In that case, look up the changed Cmd ID from Actions and update it above.
#
# In the future, when Reaper's OSC supports the stable "Custom ID", 
# this will no longer be an issue.  In the mean time, try to setup
# RemoteControl.py early on, so that any Actions you may add or delete
# afterwards will not change its Cmd ID.




# Step 2 - Reaper's OSC and Addresses
# =======================================================================

Reaper_OSC_Address = ("192.168.0.23", 8000)
External_Program_Address = ("127.0.0.1", 8001)

# From Reaper's "Options/Preferences" select "Control Surfaces" page.
#
# If the "Control Surfaces" has an item beginning with "OSC:", you have 
# a preexisting OSC setup, see below.
#
# Press "Add" and select "OSC (Open Sound Control)".
#
# Make sure the "Pattern config:" is set to Default.
#
# Check and Activate "Receive on port:"
#
# The default Port of 8000 and the "localhost" addresses here are fine
# for connecting to Reaper locally on the same computer only.  If you need 
# to connect to Reaper across a network, change these addresses to match 
# Reaper and where External Programs will be running.
# 
# 
# Preexisting OSC Setup:
# ======================
# 
# If your "Pattern config:" is not Default, make sure you have the following
# line in your Pattern config file:
# 
# ACTION i/action t/action/@
# 
# Or, you may setup another Default OSC configuration as above on 
# another Port and enter that Port above.




# Step 3 - Python Executable
# =======================================================================

Python = r"C:\Program Files\Python37\pythonw.exe"
# Enter the path of your preferred Python executable
#
# On Windows, example:
# Python = r"C:\Python34\pythonw.exe"
# Keep the r" to preserve the \'s
#
# On OSX, example:
# Python = "/Library/Frameworks/Python.framework/Versions/3.4/Resources/Python.app/Contents/MacOS/Python"
#
# This will allow you to launch External beyond.Reaper programs as
# Reaper Actions bound to keyboard shortcuts, menus and toolbars.