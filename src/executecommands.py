import subprocess

def ExecuteAppleCommand(scripts: str, absPath: str) -> None:

    if absPath == None:
        pass # do relative path instead
    if scripts == None:
        raise ValueError("must have a parameter")

    for script in scripts:
        fullScriptWithPath = ""
        for index,arg in enumerate(script.split()):
            if index == 1:
                fullScriptWithPath += absPath + "/src/scripts/"
            fullScriptWithPath += arg + " "
        process = subprocess.Popen(fullScriptWithPath.split(), stdout=subprocess.PIPE)
