All started here https://www.hanselman.com/blog/UsingVisualStudioCodeToProgramCircuitPythonWithAnAdaFruitNeoTrellisM4.aspx 

To get VSCode working:

1.  Install VSCode  https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=-blog-scottha
2.  Install Supported Python (3.7.2 64bit in this case)   https://www.python.org/downloads/
3.  Install Python VSCode Extension  https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=-blog-scottha
4.  Intalled pylint when prompted from Pythong Extension

Everything was working fine in terms of saving to CPX, but the libraries would not load or autocomplete in linter.

To fix:
Download the latest libraries of .py files from the py zip   https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest
Once extracted, I put the lib and examples folders in in C:\Users\Jared\Documents\CircuitPython\Latest
In new lib and example folders I put an empty  __init__.py  file
Then in Environment Variables I created PYTHONPATH  and explicitely gave it lib and examples folders separately

Moving forward, similarly to when I update the CPX, I will just update this latest folder and merge/overwrite all new files

Additionaly, not sure if it needed it, in my User settings.json for VSCode, I added:
"python.autoComplete.extraPaths": [
	"C:\\Users\\Jared\\Documents\\CircuitPython\\Latest\\lib",
        "C:\\Users\\Jared\\Documents\\CircuitPython\\Latest\\examples"
]


One issue with pip not working because examples were getting in the way of standard naming conventions.


To get the serial console working, I also needed Arduino IDE 